<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="1280" height="380" viewBox="0 0 1280 380" role="img" aria-label="CookieBob Banner">
  <defs>
    <linearGradient id="cbBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3a1d0e"/>
      <stop offset="45%" stop-color="#7a4a21"/>
      <stop offset="100%" stop-color="#d8943f"/>
    </linearGradient>
    <radialGradient id="cbGlow" cx="62%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#ffeec9" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#ffeec9" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="cbChip" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2b1408"/>
      <stop offset="100%" stop-color="#5c3014"/>
    </linearGradient>
    <filter id="cbShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#2b1408" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect width="1280" height="380" fill="url(#cbBg)"/>
  <!-- Pulsing warm glow -->
  <circle cx="760" cy="190" r="210" fill="url(#cbGlow)">
    <animate attributeName="opacity" values="0.55;1;0.55" dur="7s" repeatCount="indefinite"/>
  </circle>
  <!-- Twinkling crumbs -->
  <circle cx="560" cy="120" r="6" fill="#ffeec9" opacity="0.35">
    <animate attributeName="opacity" values="0.15;0.5;0.15" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="720" cy="300" r="5" fill="#ffeec9" opacity="0.3">
    <animate attributeName="opacity" values="0.12;0.45;0.12" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1170" cy="50" r="5" fill="#ffeec9" opacity="0.3">
    <animate attributeName="opacity" values="0.12;0.5;0.12" dur="4.5s" repeatCount="indefinite"/>
  </circle>
  <!-- Floating cookie chips -->
  <g opacity="0.9">
    <circle cx="118" cy="82" r="15" fill="url(#cbChip)">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -14;0 0" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="215" cy="308" r="11" fill="url(#cbChip)" opacity="0.85"/>
    <circle cx="352" cy="58" r="8" fill="url(#cbChip)" opacity="0.7">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -10;0 0" dur="5.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="486" cy="326" r="7" fill="url(#cbChip)" opacity="0.6"/>
    <circle cx="1002" cy="66" r="12" fill="url(#cbChip)">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -10;0 0" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1116" cy="268" r="17" fill="url(#cbChip)" opacity="0.9">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -12;0 0" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1218" cy="118" r="9" fill="url(#cbChip)" opacity="0.75"/>
    <circle cx="942" cy="312" r="7" fill="url(#cbChip)" opacity="0.65"/>
    <circle cx="126" cy="196" r="6" fill="url(#cbChip)" opacity="0.5"/>
  </g>
  <!-- Logo in decorative rings -->
  <circle cx="262" cy="192" r="132" fill="none" stroke="#ffeec9" stroke-opacity="0.4" stroke-width="2.5" stroke-dasharray="8 12" stroke-linecap="round">
    <animateTransform attributeName="transform" type="rotate" from="0 262 192" to="360 262 192" dur="45s" repeatCount="indefinite"/>
  </circle>
  <circle cx="262" cy="192" r="118" fill="none" stroke="#ffeec9" stroke-opacity="0.25" stroke-width="2">
    <animateTransform attributeName="transform" type="rotate" from="360 262 192" to="0 262 192" dur="60s" repeatCount="indefinite"/>
  </circle>
  <circle cx="262" cy="192" r="104" fill="#fff" fill-opacity="0.08"/>
  <circle cx="262" cy="192" r="94" fill="#fff" fill-opacity="0.06"/>
  <image href="https://cookiebob.com/bob.png" x="196" y="126" width="132" height="132" preserveAspectRatio="xMidYMid meet">
    <animateTransform attributeName="transform" type="scale" values="1;1.04;1" dur="5s" repeatCount="indefinite" additive="sum"/>
  </image>
  <text x="470" y="172" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="78" font-weight="800" fill="#fff4dd" filter="url(#cbShadow)">CookieBob</text>
  <text x="472" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="25" font-weight="400" fill="#ffeec9" opacity="0.95">Clean code &amp; modern web engineering.</text>
  <!-- CTA pills -->
  <a href="https://cookiebob.com">
    <rect x="472" y="248" width="226" height="50" rx="25" fill="#fff4dd">
      <animate attributeName="opacity" values="1;0.82;1" dur="3s" repeatCount="indefinite"/>
    </rect>
    <text x="585" y="280" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#4a2a14">cookiebob.com</text>
  </a>
  <a href="https://github.com/CookieBob-Programming">
    <rect x="718" y="248" width="196" height="50" rx="25" fill="none" stroke="#fff4dd" stroke-width="2.5"/>
    <text x="816" y="280" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#fff4dd">GitHub</text>
  </a>
</svg></div>

<div align="center"><a href="https://cookiebob.com"><img src="https://img.shields.io/badge/Website-cookiebob.com-d8943f?style=flat-square&amp;logo=googlechrome&amp;logoColor=white" alt="Website"/></a>
<a href="https://github.com/CookieBob-Programming"><img src="https://img.shields.io/badge/GitHub-CookieBob--Programming-3a1d0e?style=flat-square&amp;logo=github&amp;logoColor=white" alt="GitHub Organization"/></a>
<a href="https://github.com/MarioH1919"><img src="https://img.shields.io/badge/Owner-MarioH1919-7a4a21?style=flat-square&amp;logo=github&amp;logoColor=white" alt="Owner"/></a>
<img src="https://img.shields.io/badge/Open%20Source-Yes-8a5a2b?style=flat-square" alt="Open Source"/></div>

<p align="center"><img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&amp;weight=500&amp;size=26&amp;duration=3500&amp;pause=900&amp;color=D8943F&amp;center=true&amp;vCenter=true&amp;width=720&amp;height=60&amp;lines=Clean+code+%26+modern+web+engineering.;Developer+tools%2C+engines+%26+apps+for+everyone.;Open+source+from+day+one+%F0%9F%8D%AA" alt="Typing SVG"/></p>

---

## 🍪 About CookieBob

CookieBob is a development organization focused on **clean, well-engineered software and performant web experiences**. We build tools, engines, and applications that are reliable, maintainable, and easy to use.

<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="360" height="24" viewBox="0 0 360 24" aria-hidden="true">
<line x1="0" y1="12" x2="138" y2="12" stroke="#e0cdb2" stroke-width="2"/>
<circle cx="160" cy="12" r="6" fill="#8a5a2b"/>
<circle cx="180" cy="12" r="9" fill="#a9713a"><animate attributeName="r" values="6.5;9.5;6.5" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="12" r="6" fill="#8a5a2b"/>
<line x1="222" y1="12" x2="360" y2="12" stroke="#e0cdb2" stroke-width="2"/>
</svg></div>

## ✨ What we focus on

<table>
<tr>
<td width="33%" align="center"><h3>🧩 <strong>Clean code</strong></h3>Readable, testable, and well-structured code that is easy to maintain.</td>
<td width="33%" align="center"><h3>⚡ <strong>Performance &amp; accessibility</strong></h3>Fast, responsive applications that work for everyone.</td>
<td width="33%" align="center"><h3>🌍 <strong>Open source</strong></h3>All of our work is public – free to use, modify, and learn from.</td>
</tr>
</table>

<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="360" height="24" viewBox="0 0 360 24" aria-hidden="true">
<line x1="0" y1="12" x2="138" y2="12" stroke="#e0cdb2" stroke-width="2"/>
<circle cx="160" cy="12" r="6" fill="#8a5a2b"/>
<circle cx="180" cy="12" r="9" fill="#a9713a"><animate attributeName="r" values="6.5;9.5;6.5" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="12" r="6" fill="#8a5a2b"/>
<line x1="222" y1="12" x2="360" y2="12" stroke="#e0cdb2" stroke-width="2"/>
</svg></div>

## 🛠️ Tech stack

<div align="center"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&amp;logo=html5&amp;logoColor=white" alt="HTML5"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&amp;logo=css3&amp;logoColor=white" alt="CSS3"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&amp;logo=javascript&amp;logoColor=2b1408" alt="JavaScript"/>
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&amp;logo=nodedotjs&amp;logoColor=white" alt="Node.js"/>
<br>
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&amp;logo=openjdk&amp;logoColor=white" alt="Java"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python"/>
<br>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&amp;logo=git&amp;logoColor=white" alt="Git"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&amp;logo=githubactions&amp;logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&amp;logo=docker&amp;logoColor=white" alt="Docker"/></div>

<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="360" height="24" viewBox="0 0 360 24" aria-hidden="true">
<line x1="0" y1="12" x2="138" y2="12" stroke="#e0cdb2" stroke-width="2"/>
<circle cx="160" cy="12" r="6" fill="#8a5a2b"/>
<circle cx="180" cy="12" r="9" fill="#a9713a"><animate attributeName="r" values="6.5;9.5;6.5" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="12" r="6" fill="#8a5a2b"/>
<line x1="222" y1="12" x2="360" y2="12" stroke="#e0cdb2" stroke-width="2"/>
</svg></div>

## 📦 Projects

<table>
<tr>
<td width="28%" align="center"><a href="https://github.com/CookieBob-Programming/Super-TMS-Game-Engine"><strong>Super-TMS-Game-Engine</strong></a><br><sub>Game engine built for the TMS.</sub><br><br><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python"/><a href="https://github.com/CookieBob-Programming/Super-TMS-Game-Engine/stargazers"><img src="https://img.shields.io/github/stars/CookieBob-Programming/Super-TMS-Game-Engine?style=social" alt="Stars"/></a></td>
<td width="24%" align="center"><a href="https://github.com/CookieBob-Programming/MMO-Base-for-Web-and-Python-Client"><strong>MMO-Base</strong></a><br><sub>A base for building MMO clients (Web + Python).</sub><br><br><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python"/><a href="https://github.com/CookieBob-Programming/MMO-Base-for-Web-and-Python-Client/stargazers"><img src="https://img.shields.io/github/stars/CookieBob-Programming/MMO-Base-for-Web-and-Python-Client?style=social" alt="Stars"/></a></td>
<td width="24%" align="center"><a href="https://github.com/CookieBob-Programming/termnotes"><strong>termnotes</strong></a><br><sub>A note-taking app for your Linux terminal with tmux.</sub><br><br><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python"/><a href="https://github.com/CookieBob-Programming/termnotes/stargazers"><img src="https://img.shields.io/github/stars/CookieBob-Programming/termnotes?style=social" alt="Stars"/></a></td>
<td width="24%" align="center"><a href="https://github.com/CookieBob-Programming/autovenv"><strong>autovenv</strong></a><br><sub>Automatically uses a shared virtual environment when running Python files.</sub><br><br><img src="https://img.shields.io/badge/Shell-4EAA25?style=flat-square&amp;logo=gnubash&amp;logoColor=white" alt="Shell"/><a href="https://github.com/CookieBob-Programming/autovenv/stargazers"><img src="https://img.shields.io/github/stars/CookieBob-Programming/autovenv?style=social" alt="Stars"/></a></td>
</tr>
</table>

<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="360" height="24" viewBox="0 0 360 24" aria-hidden="true">
<line x1="0" y1="12" x2="138" y2="12" stroke="#e0cdb2" stroke-width="2"/>
<circle cx="160" cy="12" r="6" fill="#8a5a2b"/>
<circle cx="180" cy="12" r="9" fill="#a9713a"><animate attributeName="r" values="6.5;9.5;6.5" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="12" r="6" fill="#8a5a2b"/>
<line x1="222" y1="12" x2="360" y2="12" stroke="#e0cdb2" stroke-width="2"/>
</svg></div>

## 👤 Owner

<p align="center"><a href="https://github.com/MarioH1919"><img src="https://github.com/MarioH1919.png" width="90" height="90" alt="MarioH1919"/></a><br><strong><a href="https://github.com/MarioH1919">MarioH1919</a></strong><br><sub>Founder &amp; owner of CookieBob</sub><br><img src="https://img.shields.io/badge/GitHub-MarioH1919-7a4a21?style=flat-square&amp;logo=github&amp;logoColor=white" alt="GitHub"/></p>

## 📬 Contact

<div align="center"><a href="https://cookiebob.com"><img src="https://img.shields.io/badge/Website-cookiebob.com-d8943f?style=for-the-badge&amp;logo=googlechrome&amp;logoColor=white" alt="Website"/></a>
<a href="https://github.com/CookieBob-Programming"><img src="https://img.shields.io/badge/GitHub-CookieBob--Programming-3a1d0e?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="GitHub"/></a></div>

---

<div align="center"><svg xmlns="http://www.w3.org/2000/svg" width="360" height="24" viewBox="0 0 360 24" aria-hidden="true">
<line x1="0" y1="12" x2="138" y2="12" stroke="#e0cdb2" stroke-width="2"/>
<circle cx="160" cy="12" r="6" fill="#8a5a2b"/>
<circle cx="180" cy="12" r="9" fill="#a9713a"><animate attributeName="r" values="6.5;9.5;6.5" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="12" r="6" fill="#8a5a2b"/>
<line x1="222" y1="12" x2="360" y2="12" stroke="#e0cdb2" stroke-width="2"/>
</svg><br>
<sub>🍪 CookieBob-Programming · © 2026 · <a href="https://cookiebob.com">cookiebob.com</a></sub></div>
