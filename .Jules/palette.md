## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-09-30 - JS Animations and Reduced Motion
**Learning:** While CSS `@media (prefers-reduced-motion: reduce)` effectively disables declarative CSS animations, it does not stop JavaScript-driven animations like text scrambling. These high-frequency visual updates can still trigger motion sickness for users who have requested reduced motion.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JavaScript before initializing JS-driven animations, providing an immediate fallback state for those users.
