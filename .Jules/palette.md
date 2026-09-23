## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-03 - Respecting prefers-reduced-motion in JS animations
**Learning:** While CSS handles reduced motion well for declarative animations via `@media`, JavaScript-driven animations (like high-frequency text scrambling) can slip through and cause motion sickness if not explicitly checked in the script logic.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JavaScript before initiating dynamic visual effects, providing an immediate static fallback if true.
