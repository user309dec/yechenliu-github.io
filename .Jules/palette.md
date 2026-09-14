## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-09-14 - Prefers Reduced Motion for JavaScript Animations
**Learning:** While CSS media queries (`@media (prefers-reduced-motion: reduce)`) can manage declarative CSS animations, JavaScript-driven animations (like high-frequency text scramble effects) ignore CSS rules. Users with motion sensitivity could still be subjected to jarring JS animations.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic for any dynamic DOM animations to provide an immediate fallback state and avoid causing motion sickness.
