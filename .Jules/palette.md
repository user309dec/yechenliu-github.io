## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Handling JavaScript Animations and prefers-reduced-motion
**Learning:** While CSS animations can be disabled using `@media (prefers-reduced-motion: reduce)`, this media query does not automatically stop or prevent JavaScript-driven animations (like `setTimeout`, `setInterval`, or manual DOM manipulations).
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript logic to bypass or safely adjust JS-based animations for users with vestibular disorders.
