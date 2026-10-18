## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-18 - JS Animation Accessibility
**Learning:** While CSS handles declarative animation preferences well, JavaScript-driven animations (like high-frequency text scramble effects) must explicitly check window.matchMedia("(prefers-reduced-motion: reduce)").matches to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always implement explicit JS checks for prefers-reduced-motion when building custom JS animations that bypass CSS transitions.
