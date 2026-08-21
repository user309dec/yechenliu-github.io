## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2025-02-13 - JavaScript Animations and Reduced Motion
**Learning:** While CSS handles `prefers-reduced-motion` for declarative animations, JavaScript-driven animations (like high-frequency text scramble effects) ignore CSS media queries and can cause motion sickness if not explicitly checked in the JS logic.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` before initializing JS-driven animations and provide an immediate fallback state.
