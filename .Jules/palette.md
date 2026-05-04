## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Respecting Reduced Motion in JS and CSS
**Learning:** CSS media queries like `@media (prefers-reduced-motion: reduce)` do not automatically stop JavaScript-driven animations (e.g. `setTimeout` text scrambling) or smooth scrolling behavior.
**Action:** When working on sites with custom animations, explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to bypass programmatic animations, and add `scroll-behavior: auto !important` to CSS to override smooth scrolling.
