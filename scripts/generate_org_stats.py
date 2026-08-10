#!/usr/bin/env python3
"""Generate CookieBob organization stats cards as SVGs.

Reads live data from the GitHub REST API and renders two cards in the
CookieBob banner theme:

  profile/assets/stats.svg       Repos, stars, forks, open issues, streaks
  profile/assets/top-langs.svg   Top programming languages

Uses only the Python standard library so it runs on any runner without
dependency installation.
"""

import json
import os
import urllib.request
from datetime import date, datetime, timedelta, timezone
from html import escape

ORG = os.environ.get("ORG", "CookieBob-Programming")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_DIR = os.environ.get("OUT_DIR", "profile/assets")
API = "https://api.github.com"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

BG1 = "#1f2733"
BG2 = "#2c3644"
BORDER = "#3e4a5a"
ACCENT = "#7ea6e0"
TITLE = "#e8eef5"
TEXT = "#b8c4d4"
MUTED = "#8494a8"
BAR_COLORS = ["#7ea6e0", "#5f7ea6", "#93a8c9", "#4a5f7d", "#8ab4f8", "#c3d0e4"]


def api(path):
    url = API + path
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = "token " + TOKEN
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def api_all(path):
    """Fetch every page of a paginated endpoint."""
    items = []
    page = 1
    while True:
        sep = "&" if "?" in path else "?"
        batch = api(f"{path}{sep}per_page=100&page={page}")
        if not batch:
            return items
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def fetch_stats():
    repos = [r for r in api_all(f"/orgs/{ORG}/repos?type=public") if not r["fork"]]

    total_stars = sum(r["stargazers_count"] for r in repos)
    total_forks = sum(r["forks_count"] for r in repos)
    open_issues = sum(r["open_issues_count"] for r in repos)

    langs = {}
    commit_dates = set()
    total_commits = 0
    for repo in repos:
        name = repo["name"]
        try:
            language_bytes = api(f"/repos/{ORG}/{name}/languages")
            for language, size in language_bytes.items():
                langs[language] = langs.get(language, 0) + size
        except Exception:
            primary = repo.get("language")
            if primary:
                langs[primary] = langs.get(primary, 0) + 1
        try:
            commits = api_all(f"/repos/{ORG}/{name}/commits")
            total_commits += len(commits)
            for commit in commits:
                raw = commit.get("commit", {}).get("author", {}).get("date")
                if raw:
                    commit_dates.add(raw[:10])
        except Exception:
            pass

    return {
        "repos": len(repos),
        "stars": total_stars,
        "forks": total_forks,
        "issues": open_issues,
        "commits": total_commits,
        "langs": sorted(langs.items(), key=lambda kv: kv[1], reverse=True),
        "streak_current": current_streak(commit_dates),
        "streak_longest": longest_streak(commit_dates),
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def current_streak(days):
    if not days:
        return 0
    day = date.today()
    if day.isoformat() not in days:
        day -= timedelta(days=1)
    streak = 0
    while day.isoformat() in days:
        streak += 1
        day -= timedelta(days=1)
    return streak


def longest_streak(days):
    if not days:
        return 0
    ordered = sorted(days)
    best = run = 1
    for prev, cur in zip(ordered, ordered[1:]):
        run = run + 1 if _next_day(prev) == cur else 1
        best = max(best, run)
    return best


def _next_day(iso):
    d = datetime.strptime(iso, "%Y-%m-%d").date()
    return (d + timedelta(days=1)).isoformat()


def _fmt(number):
    return f"{number:,}"


def rounded_rect(x, y, w, h, rx):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"'


def header(w, h, title):
    return (
        f'<defs>'
        f'<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" stop-color="{BG1}"/><stop offset="100%" stop-color="{BG2}"/>'
        f'</linearGradient>'
        f'<filter id="blur" x="-60%" y="-60%" width="220%" height="220%">'
        f'<feGaussianBlur stdDeviation="22"/>'
        f'</filter>'
        f'</defs>'
        f'{rounded_rect(0, 0, w, h, 18)} fill="url(#bg)" stroke="{BORDER}" stroke-width="1.5"/>'
        f'<circle cx="{w - 26}" cy="24" r="54" fill="{ACCENT}" opacity="0.26" filter="url(#blur)"/>'
        f'<circle cx="26" cy="{h - 30}" r="42" fill="{ACCENT}" opacity="0.14" filter="url(#blur)"/>'
        f'<circle cx="22" cy="24" r="5" fill="{ACCENT}"/>'
        f'<text x="36" y="30" font-family="{FONT}" font-size="18" font-weight="700" fill="{TITLE}">{escape(title)}</text>'
        f'<line x1="16" y1="46" x2="{w - 16}" y2="46" stroke="{BORDER}" stroke-width="1"/>'
    )


def metric(x, y, value, label):
    return (
        f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-size="30" '
        f'font-weight="800" fill="{ACCENT}">{escape(_fmt(value))}</text>'
        f'<text x="{x}" y="{y + 22}" text-anchor="middle" font-family="{FONT}" font-size="13" '
        f'fill="{TEXT}">{escape(label)}</text>'
    )


def render_stats(data):
    w, h = 470, 242
    cells = [
        (data["repos"], "Repositories"),
        (data["stars"], "Stars"),
        (data["forks"], "Forks"),
        (data["issues"], "Open Issues"),
    ]
    centers = [74, 181, 289, 396]
    body = header(w, h, "CookieBob · Organization Stats")
    for (value, label), cx in zip(cells, centers):
        body += metric(cx, 112, value, label)

    body += f'<line x1="16" y1="156" x2="{w - 16}" y2="156" stroke="{BORDER}" stroke-width="1"/>'
    body += (
        f'<text x="74" y="190" text-anchor="middle" font-family="{FONT}" font-size="26" '
        f'font-weight="800" fill="{ACCENT}">{_fmt(data["streak_current"])}</text>'
        f'<text x="74" y="212" text-anchor="middle" font-family="{FONT}" font-size="12" '
        f'fill="{TEXT}">Current streak (days)</text>'
        f'<text x="235" y="190" text-anchor="middle" font-family="{FONT}" font-size="26" '
        f'font-weight="800" fill="{ACCENT}">{_fmt(data["streak_longest"])}</text>'
        f'<text x="235" y="212" text-anchor="middle" font-family="{FONT}" font-size="12" '
        f'fill="{TEXT}">Longest streak (days)</text>'
        f'<text x="396" y="190" text-anchor="middle" font-family="{FONT}" font-size="26" '
        f'font-weight="800" fill="{ACCENT}">{_fmt(data["commits"])}</text>'
        f'<text x="396" y="212" text-anchor="middle" font-family="{FONT}" font-size="12" '
        f'fill="{TEXT}">Commits</text>'
    )
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="CookieBob stats">{body}</svg>'


def render_langs(data):
    top = data["langs"][:6]
    total = sum(size for _, size in top)
    n = len(top)
    w = 470
    h = 70 + n * 30 + 14
    body = header(w, h, "Top Languages")
    if not top:
        body += (
            f'<text x="16" y="86" font-family="{FONT}" font-size="14" fill="{TEXT}">'
            f'No public languages found yet.</text>'
        )
    else:
        bar_w = 300
        x_bar = 110
        x_pct = 468
        y = 70
        for i, (name, size) in enumerate(top):
            pct = round(size / total * 100, 1) if total else 0
            width = max(2, int(bar_w * pct / 100))
            color = BAR_COLORS[i % len(BAR_COLORS)]
            body += (
                f'<text x="16" y="{y + 12}" font-family="{FONT}" font-size="14" fill="{TEXT}">{escape(name)}</text>'
                f'<rect x="{x_bar}" y="{y}" width="{bar_w}" height="14" rx="7" fill="{BG1}" stroke="{BORDER}" stroke-width="1"/>'
                f'<rect x="{x_bar}" y="{y}" width="{width}" height="14" rx="7" fill="{color}"/>'
                f'<text x="{x_pct}" y="{y + 12}" text-anchor="end" font-family="{FONT}" font-size="13" '
                f'font-weight="700" fill="{TITLE}">{pct}%</text>'
            )
            y += 30
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="CookieBob top languages">{body}</svg>'


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    data = fetch_stats()
    with open(os.path.join(OUT_DIR, "stats.svg"), "w") as fh:
        fh.write(render_stats(data))
    with open(os.path.join(OUT_DIR, "top-langs.svg"), "w") as fh:
        fh.write(render_langs(data))
    print(
        f"repos={data['repos']} stars={data['stars']} forks={data['forks']} "
        f"issues={data['issues']} commits={data['commits']} "
        f"streak={data['streak_current']}/{data['streak_longest']} langs={len(data['langs'])}"
    )


if __name__ == "__main__":
    main()
