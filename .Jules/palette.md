## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-09-27 - Respect Reduced Motion in JS Animations
**Learning:** While CSS media queries successfully manage declarative animations, high-frequency text scramble effects driven by JavaScript must explicitly check the user's reduced-motion preference within the JS logic to provide an immediate fallback state.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in custom JS animation scripts to avoid causing motion sickness for users who have requested reduced motion.
