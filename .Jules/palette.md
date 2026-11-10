## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-10 - Respect prefers-reduced-motion in JS animations
**Learning:** JS animations (like the text scramble effect) inherently bypass CSS `@media` queries for reduced motion, which can cause accessibility issues for users sensitive to motion.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript before running animations or staggered effects, and provide an instant/static fallback state.
