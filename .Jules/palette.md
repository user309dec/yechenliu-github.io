## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-07 - Reduced Motion Fallbacks for JavaScript Animations

**Learning:** While CSS media queries (`@media (prefers-reduced-motion: reduce)`) can easily manage declarative animations, JavaScript-driven animations (like high-frequency text scramble effects) require explicit JS checks via `window.matchMedia`. Without this, users with vestibular disorders might still experience motion sickness from JS animations even if CSS animations are disabled.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JavaScript logic for dynamic animations to provide an immediate fallback state.
