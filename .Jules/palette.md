## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-03 - JavaScript Animation Accessibility
**Learning:** JavaScript animations (like text scrambles or typewriter effects) inherently bypass CSS `@media (prefers-reduced-motion: reduce)` queries. Users who have requested reduced motion in their OS settings will still be subjected to potentially disorienting JS animations unless explicitly handled in code.
**Action:** Always check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before initializing JavaScript-driven animations, and provide an instant, accessible fallback state.
