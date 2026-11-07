## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2026-11-07 - Respecting User Motion Preferences in JS Animations
**Learning:** JS animations (using setTimeout/setInterval) inherently bypass CSS @media queries for reduced motion.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before starting JS animations to enforce accessibility preferences.
