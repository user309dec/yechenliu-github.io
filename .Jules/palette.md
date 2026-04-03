## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-24 - JavaScript Animations and Reduced Motion
**Learning:** CSS media queries like `prefers-reduced-motion` only automatically stop CSS animations and transitions. They do not automatically pause or bypass JavaScript-driven animations, such as loops run via `setTimeout`, `setInterval`, or `requestAnimationFrame`. If an app relies on JS to handle animations (e.g., text scramble effects), it can become an accessibility issue because the OS-level reduced motion preference is silently ignored by the JS logic.
**Action:** Always manually check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript when scheduling purely decorative, time-based JS effects, and immediately apply the final state if the user prefers reduced motion.
