## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - prefers-reduced-motion interactions with JS and CSS
**Learning:** CSS `prefers-reduced-motion: reduce` stops CSS animations, but does not stop JS-driven animations (like timeouts or decoding text effects) or native CSS `scroll-behavior: smooth`.
**Action:** Always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to manually bypass animations, and explicitly enforce `scroll-behavior: auto !important` in the reduced motion CSS media query.
