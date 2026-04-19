## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-04-19 - Respecting prefers-reduced-motion in JavaScript and Native Scrolling
**Learning:** Adding a CSS `@media (prefers-reduced-motion: reduce)` block with `animation-duration: 0.01ms` is not enough. Native smooth scrolling (`scroll-behavior: smooth`) and JavaScript-driven animations (like `setTimeout` loops) do not automatically stop. Motion-sensitive users will still experience unwanted movement.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to bypass custom animations, and enforce `scroll-behavior: auto !important` in the reduced motion CSS media query.
