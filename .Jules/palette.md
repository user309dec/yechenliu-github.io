## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-01 - JS Animation Accessibility
**Learning:** JS-driven animations bypass CSS `@media` queries for `prefers-reduced-motion`, creating an accessibility issue for users who rely on this setting.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before starting any JS-driven animations.
