## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-05 - Respect prefers-reduced-motion for JavaScript Animations
**Learning:** JavaScript-driven animations (like text scrambles or interval updates) bypass CSS `@media (prefers-reduced-motion: reduce)` queries. This can trigger vestibular disorders even if the user has requested reduced motion at the OS level.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript before initializing custom animation loops or timeouts, and provide a static fallback state.
