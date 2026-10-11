## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-11 - JS Animation Accessibility
**Learning:** While CSS handles declarative animations via `@media (prefers-reduced-motion: reduce)`, JS-driven animations (like the text scramble effect) must explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` to bypass animations and provide an immediate fallback state.
**Action:** Always wrap JS-driven UI animations in a check for `prefers-reduced-motion` to avoid causing motion sickness.
