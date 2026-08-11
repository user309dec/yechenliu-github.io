## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JavaScript-Driven Animations and Reduced Motion
**Learning:** While CSS animations natively respond to `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like text scrambling) do not automatically stop, which can cause severe motion sickness for vulnerable users.
**Action:** Always explicitly evaluate `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript animation initialization logic to immediately halt or bypass the effect and provide a static fallback.
