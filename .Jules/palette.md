## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-03-26 - Javascript Animations and Reduced Motion
**Learning:** CSS media queries (`@media (prefers-reduced-motion: reduce)`) can disable CSS transitions and animations, but they have no effect on custom Javascript-driven animations utilizing `setTimeout`, `setInterval`, or `requestAnimationFrame`. If not checked explicitly, these animations will still play for users requesting reduced motion, presenting an accessibility failure.
**Action:** Always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before executing Javascript-driven animations to conditionally bypass or simplify the effect for affected users.
