## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-08-07 - JS Animations and prefers-reduced-motion
**Learning:** While CSS media queries handle declarative animations, JS-driven animations (like high-frequency text scrambles) bypass these CSS rules. They must explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` to provide an immediate fallback and avoid causing motion sickness.
**Action:** Always conditionally bypass JS-driven animation logic with a `prefers-reduced-motion` check for users who prefer reduced motion.
