## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-08-10 - JavaScript Animation Accessibility
**Learning:** While declarative CSS animations (like `.scramble-line`) are successfully managed by `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like the high-frequency text scramble effect in `decode()`) require explicit checks using `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within the JS logic to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always test JavaScript animations with `prefers-reduced-motion: reduce` enabled. When using JS for visual effects, implement an early return condition using `window.matchMedia()` at the start of the function.
