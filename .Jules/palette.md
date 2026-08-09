## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-24 - Respecting prefers-reduced-motion in JavaScript
**Learning:** While CSS handles `prefers-reduced-motion` well via media queries, JavaScript-driven animations (like the high-frequency scramble decode effect) must explicitly query `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in logic to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always verify JS animations conditionally bypass or reduce motion for users who have requested it.
