## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-03-20 - Respecting prefers-reduced-motion in JavaScript
**Learning:** CSS `@media (prefers-reduced-motion: reduce)` rules do not automatically stop or disable JavaScript-driven animations (like `setTimeout`, `setInterval`, or custom frame loops). Relying solely on CSS media queries leaves users with cognitive or vestibular disorders exposed to potentially triggering JS animations.
**Action:** When implementing JavaScript-based animations or delayed reveals, explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to bypass or adjust the animation logic, ensuring a consistent and safe experience for all users.
