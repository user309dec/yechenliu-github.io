## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-16 - Respect prefers-reduced-motion in JavaScript
**Learning:** While CSS media queries handle declarative animations, JS-driven animations (like text scramblers) must explicitly check window.matchMedia("(prefers-reduced-motion: reduce)").matches to avoid causing motion sickness.
**Action:** Always wrap high-frequency JavaScript animations in a conditional check to provide an immediate static fallback for users who prefer reduced motion.
