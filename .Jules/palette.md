## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-21 - Respect prefers-reduced-motion in JS animations
**Learning:** While CSS handles declarative animation reduction, JavaScript-driven text scramble effects completely ignore standard CSS media queries, causing motion sickness for users who have requested reduced motion.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` before initializing high-frequency JS-driven DOM manipulation animations.
