## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-20 - Respecting `prefers-reduced-motion` in JS Animations
**Learning:** CSS media queries for `prefers-reduced-motion` do not inherently stop JavaScript-based animations like text scrambling or staggered fade-ins using `setTimeout`.
**Action:** When creating animations driven by JavaScript, explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` to bypass or adjust the animations for an accessible experience.
