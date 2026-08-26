## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-15 - Respecting prefers-reduced-motion in JS Animations
**Learning:** While CSS handles declarative animations well, JavaScript-driven animations (like text scrambling) bypass CSS rules and require explicit media query checks (`window.matchMedia("(prefers-reduced-motion: reduce)").matches`) to prevent triggering motion sickness for susceptible users.
**Action:** Always check `prefers-reduced-motion` natively within JavaScript logic for any dynamic DOM manipulations or layout thrashing animations to provide an immediate, static fallback.
