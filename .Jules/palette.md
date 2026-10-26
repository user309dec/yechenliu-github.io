## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2026-10-26 - Respect prefers-reduced-motion in JS animations
**Learning:** While CSS animations can be disabled via media queries, JavaScript-driven animations (like setInterval/setTimeout text reveals) inherently bypass these CSS rules. Users with motion sensitivities were still subjected to the JS text scramble effect even with prefers-reduced-motion enabled.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript before initializing custom DOM animations, and provide an immediate fallback state if true.
