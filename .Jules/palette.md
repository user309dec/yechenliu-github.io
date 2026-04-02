## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-04-02 - Respecting prefers-reduced-motion in JavaScript
**Learning:** While CSS `prefers-reduced-motion` can disable CSS animations, it does not automatically stop JavaScript-driven animations (like `setTimeout` or `setInterval`). These must be explicitly evaluated using `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to bypass or adjust the JS logic.
**Action:** Always check and explicitly handle `prefers-reduced-motion` for any custom animations built entirely or partially in JavaScript.
