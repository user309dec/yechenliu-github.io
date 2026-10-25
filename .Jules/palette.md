## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-25 - JS Animations Bypassing CSS Reduced Motion
**Learning:** The text scramble effect is implemented purely in JavaScript using `setTimeout` and `setInterval`. While the CSS `@media (prefers-reduced-motion: reduce)` was added to stop CSS transitions and animations, it doesn't automatically stop JavaScript-driven animations. This creates an accessibility issue where users with motion sensitivity still experience the intense text scramble effect.
**Action:** When implementing or modifying JavaScript-driven animations, always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to enforce accessibility preferences, as these JS animations inherently bypass CSS `@media` queries.
