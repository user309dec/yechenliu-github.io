## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-08-19 - Respect prefers-reduced-motion in JS animations
**Learning:** While CSS media queries successfully manage declarative animations, JavaScript-driven animations (like high-frequency text scramble effects) bypass these CSS rules. If left unchecked, they can cause motion sickness for users who have requested reduced motion.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic before initializing JS-driven animations, providing an immediate fallback state.
