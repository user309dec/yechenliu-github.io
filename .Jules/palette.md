## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-21 - JavaScript Animations vs prefers-reduced-motion
**Learning:** While CSS animations handle `prefers-reduced-motion` cleanly via media queries, JavaScript-driven animations (like `setInterval` text scramblers) run independently and ignore CSS rules. This forces unintended motion on users who explicitly opted out via system settings.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` before triggering any JavaScript-based animation logic. Ensure a zero-motion fallback is executed instead.
