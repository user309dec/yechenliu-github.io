## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - prefers-reduced-motion in JS Animations
**Learning:** While CSS `@media (prefers-reduced-motion: reduce)` successfully manages declarative CSS animations, JavaScript-driven text scramble animations continue to run and can cause motion sickness unless explicitly bypassed.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript animation logic to provide an immediate fallback state and respect user accessibility preferences.
