## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-10-12 - Disable JS-driven text scramble animation for prefers-reduced-motion
**Learning:** While CSS media queries successfully pause declarative animations, JavaScript-driven animations (like high-frequency text scramble effects) bypass these rules and can still cause motion sickness for users who prefer reduced motion.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JS animation logic to provide an immediate fallback state.
