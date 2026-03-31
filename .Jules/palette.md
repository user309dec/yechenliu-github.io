## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-03-31 - Respecting reduced motion in JS-driven animations
**Learning:** CSS `prefers-reduced-motion` media queries only prevent CSS animations and transitions; they do not automatically stop or bypass JavaScript-driven animations (like those relying on `setInterval` or `setTimeout`).
**Action:** When implementing JS-driven UI effects or animations, always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to bypass or adjust the behavior for users who prefer reduced motion, ensuring elements are immediately accessible and visible.
