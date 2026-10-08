## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-08 - Respecting Reduced Motion in JS Animations
**Learning:** High-frequency JS text scramble animations can trigger motion sickness, and unlike CSS animations, they aren't automatically mitigated by global CSS media queries.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in JavaScript before running imperative animations, returning early to provide a static fallback.
