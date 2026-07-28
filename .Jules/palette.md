## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-16 - JavaScript Animation prefers-reduced-motion Support
**Learning:** While CSS handles reduced-motion well for declarative animations via `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like `setInterval`-based high-frequency text scramble effects) are completely unaware of these CSS rules and will still execute, potentially causing motion sickness for sensitive users.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` at the start of any JS animation logic and return early or provide an immediate fallback state to ensure a safe, accessible experience.
