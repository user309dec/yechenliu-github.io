## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2026-10-06 - Respect reduced motion in JS animations
**Learning:** While CSS animations handle `prefers-reduced-motion` declaratively, JavaScript-driven animations (like text scrambles) require explicit `window.matchMedia("(prefers-reduced-motion: reduce)").matches` checks to provide an immediate fallback state and avoid causing motion sickness.
**Action:** Always verify `prefers-reduced-motion` in JS-driven animations and provide a static alternative or immediate transition.
