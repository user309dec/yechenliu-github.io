## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JS Animation Reduced Motion
**Learning:** CSS `@media (prefers-reduced-motion: reduce)` media queries do not automatically stop JavaScript-driven animations (like `setTimeout`, `setInterval`, or custom frame loops). Users who enable reduced motion might still experience rapid scrambling effects unless explicitly disabled in the script.
**Action:** When implementing custom JavaScript animations, explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in the JS logic to bypass or adjust animations accordingly to ensure full accessibility compliance.
