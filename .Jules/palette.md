## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-07-29 - JS Animation Reduced Motion Fallback
**Learning:** While CSS media queries handle declarative animations, JS-driven animations (like high-frequency text scrambles) can still trigger motion sickness if they don't explicitly check the user's reduced-motion preference.
**Action:** Always include a `window.matchMedia("(prefers-reduced-motion: reduce)").matches` check inside JS animation logic to provide an immediate static fallback.
