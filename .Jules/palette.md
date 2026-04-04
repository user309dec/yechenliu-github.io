## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-15 - Respect prefers-reduced-motion in JS animations
**Learning:** CSS media queries for `prefers-reduced-motion` only affect CSS animations and transitions (e.g. `animation-duration: 0.01ms`). They do not automatically stop JavaScript-driven animations, such as `setInterval` or `requestAnimationFrame`, causing potential accessibility and vestibular issues.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript when implementing JS-driven animations to bypass or adapt them.
