## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-10-09 - JavaScript Animations and Reduced Motion
**Learning:** While CSS media queries handle declarative animations, JS-driven animations (like the high-frequency text scramble effect on load) bypass these stylesheets and can trigger motion sickness for users with vestibular disorders.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic before initializing custom animations, providing an immediate static fallback.
