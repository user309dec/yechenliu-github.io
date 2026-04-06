## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-13 - Reduced Motion in JS Animations
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JavaScript-driven animations (like `setTimeout` or `setInterval`). This meant users requesting reduced motion still saw the text scramble decode animation, which can trigger vestibular issues.
**Action:** When implementing JS-driven animations, explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in the script to conditionally skip the animation logic and render the final state immediately.
