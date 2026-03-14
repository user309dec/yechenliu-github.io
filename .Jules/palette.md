## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Handling Prefers-Reduced-Motion in JavaScript
**Learning:** The portfolio features a "decode/scramble" text effect implemented in JavaScript. Even though `styles.css` handles the `prefers-reduced-motion: reduce` preference to turn off CSS animations and transitions, the JavaScript animation bypasses this, causing the jarring scramble effect to still run for users who have requested reduced motion. CSS media queries alone cannot pause JS execution.
**Action:** Always verify that JavaScript-driven UI animations manually hook into `window.matchMedia("(prefers-reduced-motion: reduce)").matches` to respect user accessibility preferences and bypass the JS logic entirely when preferred.
