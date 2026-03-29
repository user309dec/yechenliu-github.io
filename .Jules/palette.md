## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-12 - Explicit JS Checks for Reduced Motion
**Learning:** CSS `@media (prefers-reduced-motion: reduce)` rules do not automatically stop JavaScript-driven animations like `setInterval` or `setTimeout` (used for the text scramble effect).
**Action:** When adding JavaScript-driven animations, explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to skip or disable animations, ensuring accessibility settings are universally respected.
