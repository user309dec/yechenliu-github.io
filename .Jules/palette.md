## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Handling Reduced Motion in JS and CSS
**Learning:** The site implements a custom scramble-decode text animation in JavaScript and CSS `scroll-behavior: smooth`. The CSS `@media (prefers-reduced-motion: reduce)` media query successfully bypasses CSS-based animations, but it doesn't automatically stop JavaScript-driven `setTimeout` animations or native `scroll-behavior` implementations on the `html` element.
**Action:** Always use `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to conditionally bypass JS-driven animations. In CSS, explicitly override `scroll-behavior: smooth` with `scroll-behavior: auto !important` inside the `prefers-reduced-motion` media query block to ensure comprehensive accessibility for users sensitive to motion.
