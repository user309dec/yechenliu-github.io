## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-22 - Respect prefers-reduced-motion in JS Animations

**Learning:** While CSS media queries effectively manage declarative animations, JavaScript-driven animations (like the text scramble effect) bypass CSS. They must explicitly check window.matchMedia("(prefers-reduced-motion: reduce)").matches in the JS logic to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always check window.matchMedia for any JS-driven animations and provide a fast-path fallback when reduced motion is preferred.
