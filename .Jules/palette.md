## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JS Animations and prefers-reduced-motion
**Learning:** While CSS media queries can handle declarative CSS animations for users preferring reduced motion, JavaScript-driven animations (like high-frequency text scrambles or canvas effects) do not automatically inherit these preferences. They require explicit `window.matchMedia("(prefers-reduced-motion: reduce)").matches` checks in the JS logic to provide immediate fallback states and prevent motion sickness.
**Action:** Always check `window.matchMedia` before initializing JS-driven animations to ensure accessibility preferences are respected across both CSS and JS.
