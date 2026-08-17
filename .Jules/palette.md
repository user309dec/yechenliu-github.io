## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-08-17 - JS-driven Animations and Reduced Motion
**Learning:** While CSS handles `prefers-reduced-motion` for declarative animations natively, JavaScript-driven animations (like high-frequency text scramble effects) bypass CSS checks. This can trigger motion sickness for users with vestibular disorders if no JS-level fallback is provided.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JS animation logic to provide an immediate static fallback state.
