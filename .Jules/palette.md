## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-15 - JS Animations and Reduced Motion
**Learning:** While CSS can handle declarative animations for `prefers-reduced-motion`, JavaScript-driven animations (like the high-frequency text scramble effect on load) bypass CSS rules and can still cause motion sickness for sensitive users.
**Action:** Always wrap JavaScript-driven animations in a `window.matchMedia("(prefers-reduced-motion: reduce)").matches` check to provide an immediate fallback state.
