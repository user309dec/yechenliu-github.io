## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-15 - Respect Reduced Motion
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JS-driven animations (like `setTimeout`) or native `scroll-behavior: smooth`.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to bypass custom animation logic, and explicitly set `scroll-behavior: auto !important` in the CSS media query block.
