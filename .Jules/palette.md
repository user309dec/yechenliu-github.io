## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-08-15 - JS Animations and prefers-reduced-motion
**Learning:** While CSS declarative animations are correctly managed by `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like the high-frequency text scramble effect) bypass these CSS rules. This can cause severe motion sickness for users who have requested reduced motion.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JavaScript logic before initializing custom animation loops or effects.
