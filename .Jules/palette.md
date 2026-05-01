## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Reduced Motion for JS Animations & Smooth Scroll
**Learning:** CSS `prefers-reduced-motion` only targets CSS animations and transitions automatically. It does not stop JS-driven animations (like `setTimeout`/`setInterval` based text scrambling) or native `scroll-behavior: smooth` in all browsers without explicit overrides.
**Action:** Explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to bypass JavaScript animations, and enforce `scroll-behavior: auto !important` in the reduced motion CSS media query.
