## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2026-10-24 - Respect prefers-reduced-motion in JavaScript Animations
**Learning:** While CSS animations can be globally disabled via `@media (prefers-reduced-motion: reduce)`, complex JavaScript-driven animations (like DOM text scrambling) bypass these CSS rules. They require an explicit `window.matchMedia` check in JS to prevent triggering potentially dizzying motion for sensitive users.
**Action:** Always wrap JavaScript-based visual animations in a `window.matchMedia("(prefers-reduced-motion: reduce)").matches` guard clause to ensure comprehensive accessibility compliance.
