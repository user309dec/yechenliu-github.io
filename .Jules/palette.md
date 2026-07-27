## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-07-27 - Reduced Motion in JS Animations
**Learning:** While CSS media queries for `prefers-reduced-motion` handle CSS transitions and animations, JS-driven animations (like the scramble text decode effect) will still run and cause potential accessibility issues (motion sickness/dizziness) if not explicitly checked in the JS code.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` before initiating high-frequency or complex JS animations, providing an immediate fallback state if true.
