## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-08-27 - Respect prefers-reduced-motion in JS animations
**Learning:** While CSS handles declarative animation reduction well, high-frequency JavaScript animations (like text scrambling) bypass CSS media queries. These can cause severe discomfort for users with vestibular disorders.
**Action:** Always check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JS logic before executing complex DOM-mutating animations, providing a static fallback if true.
