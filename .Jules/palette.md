## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-11-08 - Enforce prefers-reduced-motion for JavaScript Animations

**Learning:** While CSS `@media (prefers-reduced-motion: reduce)` effectively handles CSS transitions and animations, it does not automatically stop JavaScript-driven animations (like text scrambling or intervals). These must be explicitly checked and disabled in JS to ensure a fully accessible experience for users sensitive to motion.
**Action:** Always use `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to conditionally execute complex JS animations, ensuring consistency with CSS motion preferences.
