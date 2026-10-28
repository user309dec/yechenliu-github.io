## 2024-01-01 - Disable JS Animations for Reduced Motion
**Learning:** CSS `@media (prefers-reduced-motion: reduce)` rules do not automatically pause or disable animations driven purely by JavaScript (like `setTimeout`/`setInterval` based text scrambling).
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript before initiating dynamic JS-driven animations.
