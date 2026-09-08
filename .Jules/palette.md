## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-18 - Checking for accessibility issues
**Learning:** Found an animated typing cursor and a JavaScript scramble decode reveal animation. The scramble animation does not seem to respect `prefers-reduced-motion` at the JS level (the CSS does disable transitions, but JS intervals will still run and text will still flip).
**Action:** Always check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS-driven animations.
