## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-15 - CSS prefers-reduced-motion does not stop JS animations
**Learning:** CSS media queries like `prefers-reduced-motion` can disable CSS transitions and animations, but they do not automatically pause or bypass JavaScript-driven animations (such as those using `setTimeout`, `setInterval`, or `requestAnimationFrame`). Users enabling reduced motion will still experience JavaScript animations unless explicitly handled in code.
**Action:** Always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript when implementing JS-based animations or sequential reveals to respect the user's accessibility preferences.
