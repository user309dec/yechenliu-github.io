## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-04-30 - Respecting Reduced Motion in JS and Scroll Behavior
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JavaScript-driven animations (like `setInterval` or `setTimeout`) or native `scroll-behavior: smooth`. Relying solely on CSS transition suppression can leave users with jarring JS animations or slow scrolling that ignores their OS-level motion preferences.
**Action:** Explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to bypass custom animations (e.g., using early returns), and ensure `scroll-behavior: auto !important` is enforced within the reduced motion CSS media query.
