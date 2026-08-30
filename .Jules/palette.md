## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-15 - Prefers Reduced Motion in JS Animations
**Learning:** While CSS media queries handle declarative animations, JS-driven animations (like high-frequency text scramble effects) need explicit `window.matchMedia("(prefers-reduced-motion: reduce)").matches` checks to prevent motion sickness.
**Action:** Always check `prefers-reduced-motion` in JavaScript logic for custom animations to provide an immediate fallback state.
