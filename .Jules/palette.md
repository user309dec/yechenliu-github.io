## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-15 - [Respecting prefers-reduced-motion in JavaScript Animations]
**Learning:** JS-driven animations (e.g., `setInterval`, `setTimeout`, or `requestAnimationFrame`) are not caught by CSS media queries. While CSS animations can be disabled using `@media (prefers-reduced-motion: reduce)`, JavaScript animations require explicit media query checks (`window.matchMedia("(prefers-reduced-motion: reduce)").matches`) to ensure accessibility for motion-sensitive users.
**Action:** When implementing custom JavaScript animations, always add a `matchMedia` check and provide an immediate transition or bypass the animation logic entirely if the user prefers reduced motion.
