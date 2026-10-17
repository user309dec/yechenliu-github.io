## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-17 - JS Animation Accessibility
**Learning:** JavaScript-driven animations (like the high-frequency text scramble effect) must explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within the JS logic to provide an immediate fallback state, as declarative CSS media queries cannot stop them.
**Action:** Always check `prefers-reduced-motion` in JS when implementing dynamic visual effects, and bypass the animation loops if true.
