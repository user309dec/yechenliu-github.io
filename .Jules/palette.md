## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - prefers-reduced-motion caveats
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JavaScript-driven animations (like `setTimeout`) or native `scroll-behavior: smooth`.
**Action:** Explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to bypass animations, and enforce `scroll-behavior: auto !important` in the reduced motion CSS media query.
