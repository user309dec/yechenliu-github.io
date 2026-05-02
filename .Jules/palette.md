## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Handling JavaScript Animations & Smooth Scrolling with Reduced Motion
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically halt JavaScript-driven animations (e.g., custom decode scrambles using `setInterval` or `setTimeout`) or native smooth scrolling (`scroll-behavior: smooth`). Relying solely on CSS animation resets leaves users vulnerable to motion triggers from JS or layout scrolling.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript initialization to bypass animation logic, and explicitly add `scroll-behavior: auto !important` inside the reduced motion CSS block to disable smooth scrolling.
