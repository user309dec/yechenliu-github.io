## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-15 - Explicitly Handle prefers-reduced-motion in JavaScript
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JavaScript-driven animations like `setTimeout` or `setInterval` text effects. If the animation logic continues running under the hood, it breaks the accessibility intent.
**Action:** Always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to explicitly bypass or adjust animation logic.
