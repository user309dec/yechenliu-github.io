## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-03-15 - prefers-reduced-motion in JavaScript Interval Animations
**Learning:** CSS media queries for `prefers-reduced-motion: reduce` only stop CSS transitions and animations. They do not halt custom JavaScript animations running via `setInterval` or `requestAnimationFrame`. Assistive motion constraints require explicit JS logic to disable them, otherwise the user's OS-level motion preference is violated for dynamic UI effects like text scrambling.
**Action:** When implementing any JavaScript-driven continuous animation or effect, explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` to bail out or provide an instant fallback.
