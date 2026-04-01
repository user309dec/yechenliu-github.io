## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## $(date +%Y-%m-%d) - Reduced Motion in JavaScript Animations
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop or bypass JavaScript-driven animations (like `setTimeout`, `setInterval`, or `requestAnimationFrame`). Users enabling reduced motion may still experience triggering or disorienting effects if logic is handled exclusively in JS.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to conditionally bypass complex, time-based visual manipulations or animations.
