## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-05 - Reduced Motion in JavaScript Animations
**Learning:** CSS `@media (prefers-reduced-motion: reduce)` alone does not automatically stop JavaScript-driven animations (like `setTimeout` delays or `setInterval` loops). The decode scramble effect continued to run, potentially triggering symptoms for users with vestibular disorders.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to conditionally bypass animations, intervals, or timeouts, ensuring an instantly accessible state for users who prefer reduced motion.
