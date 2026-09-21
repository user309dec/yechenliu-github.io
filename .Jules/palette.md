## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-10-24 - JS Animation prefers-reduced-motion Fallbacks
**Learning:** While CSS animations can be managed via `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like high-frequency text scrambles) require explicit JS checks to respect user preferences and avoid motion sickness.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JS logic before initiating complex text or element animations.
