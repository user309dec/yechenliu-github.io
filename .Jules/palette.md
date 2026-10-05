## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2026-10-05 - prefers-reduced-motion for JS Animations
**Learning:** While CSS media queries are effective for declarative animations, JavaScript-driven animations (like high-frequency text scrambles) can easily be overlooked. These can cause severe discomfort for users with motion sensitivities.
**Action:** Always wrap arbitrary JS-driven animation loops or effects in a `window.matchMedia("(prefers-reduced-motion: reduce)").matches` check to provide an immediate fallback state.
