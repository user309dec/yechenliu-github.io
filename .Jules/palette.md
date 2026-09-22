## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-09-22 - Respecting Reduced Motion in JS Animations
**Learning:** While CSS handles declarative animations via `@media (prefers-reduced-motion: reduce)`, custom JavaScript-driven animations (like high-frequency text scrambling) bypass these CSS rules. This can inadvertently trigger motion sickness for users who have explicitly requested reduced motion.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript animation logic to provide an immediate static fallback state for affected users.
