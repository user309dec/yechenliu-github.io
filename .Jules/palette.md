## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Respecting prefers-reduced-motion in JavaScript
**Learning:** While CSS `@media (prefers-reduced-motion: reduce)` easily manages declarative animations, JavaScript-driven animations (like a high-frequency text scramble effect) must explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches`. If unchecked, JS animations will continue to play, which can cause motion sickness for sensitive users.
**Action:** Always verify `window.matchMedia` before triggering JavaScript-based layout or text animations, providing an immediate fallback state if reduced motion is requested.
