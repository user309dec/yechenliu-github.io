## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Respect prefers-reduced-motion in JS animations
**Learning:** CSS media queries do not automatically stop JS animations. Must explicitly check prefers-reduced-motion.
**Action:** Use window.matchMedia('(prefers-reduced-motion: reduce)').matches in JS.
