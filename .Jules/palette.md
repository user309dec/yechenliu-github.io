## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-08-04 - JavaScript Animation and Reduced Motion
**Learning:** While CSS media queries successfully stop declarative CSS animations when users prefer reduced motion, custom JavaScript-driven animations (like `setInterval` text scrambles) bypass CSS restrictions entirely. This can unintentionally trigger motion sickness.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript animation logic to provide immediate, static fallback states for users sensitive to motion.
