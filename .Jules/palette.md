## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JS Animation Prefers Reduced Motion
**Learning:** While CSS media queries handle declarative animations, JavaScript-driven animations (like high-frequency text scramble effects) must explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within the JS logic to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always wrap JavaScript-based animations or high-frequency DOM manipulations with a reduced-motion media query check to respect OS-level accessibility preferences.
