## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-02 - Respect prefers-reduced-motion in JS animations
**Learning:** CSS media queries for `prefers-reduced-motion` don't automatically pause JavaScript-driven animations (like `setInterval` or `requestAnimationFrame`). These can cause motion sickness for sensitive users even if CSS animations are disabled.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` inside JavaScript animation loops or initialization functions to halt them appropriately.
