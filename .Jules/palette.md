## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JavaScript Animation and Reduced Motion
**Learning:** While CSS media queries (`@media (prefers-reduced-motion: reduce)`) successfully manage declarative CSS animations, JavaScript-driven animations (like high-frequency text scramble effects) continue to run unless explicitly checked. This can cause motion sickness for users who have requested reduced motion at the OS level.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic for any programmatic animations to provide an immediate fallback state and respect user accessibility preferences.
