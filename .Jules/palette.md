## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Reduced Motion in JS Animations
**Learning:** While CSS `@media (prefers-reduced-motion: reduce)` easily handles declarative animations, JavaScript-driven text scramble animations bypass these CSS rules. This can trigger motion sickness for users who have requested reduced motion at the OS level.
**Action:** Always wrap JavaScript-based animations or sequential delays in a `window.matchMedia("(prefers-reduced-motion: reduce)").matches` check to provide an immediate, static fallback state.
