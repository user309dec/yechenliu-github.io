## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-08-14 - JS Animation Accessibility
**Learning:** While CSS animations can be disabled declaratively via media queries, JavaScript-driven text-scramble effects require explicit `window.matchMedia("(prefers-reduced-motion: reduce)").matches` checks to provide an immediate static fallback.
**Action:** Always wrap JS-based visual effects in prefers-reduced-motion checks to prevent motion sickness and respect user preferences.
