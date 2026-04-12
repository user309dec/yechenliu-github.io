## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-16 - Reduced Motion and JavaScript Animations
**Learning:** CSS media queries like `@media (prefers-reduced-motion: reduce)` do not automatically pause or bypass JavaScript-driven animations (e.g., `setInterval`/`setTimeout`) or native `scroll-behavior: smooth`.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to conditionally skip animation logic, and explicitly add `scroll-behavior: auto !important` inside the reduced motion CSS media block.
