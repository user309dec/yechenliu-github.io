## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-15 - Respecting prefers-reduced-motion in JavaScript Animations
**Learning:** CSS media queries for `prefers-reduced-motion` are insufficient when animations are driven by JavaScript (e.g., `setTimeout`, `setInterval`, or canvas drawings). The JS code will continue to execute the animation logic even if CSS transitions are disabled, which can still cause motion or accessibility issues.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to conditionally bypass or reduce custom JS-driven animations and immediately apply the final state.
