## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-09-04 - JS-Driven Animation Fallbacks
**Learning:** The portfolio relies on a high-frequency text scrambling animation. While CSS media queries (`@media (prefers-reduced-motion: reduce)`) handle CSS transitions, the JavaScript-driven scramble effect still runs for users who request reduced motion, which can trigger motion sickness.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic for any dynamic DOM manipulations or animations to provide an immediate static fallback state.
