## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-04-28 - CSS and JS Animation Synchronization with prefers-reduced-motion
**Learning:** Adding a `@media (prefers-reduced-motion: reduce)` media query in CSS that zeroes out `animation-duration` and `transition-duration` does not stop JavaScript-driven animations (like using `setTimeout` or `requestAnimationFrame`) or native browser behaviors like `scroll-behavior: smooth`.
**Action:** When implementing reduced motion, explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to bypass programmatic animations, and add `scroll-behavior: auto !important` to the reduced motion CSS media query.
