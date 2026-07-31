## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JS Animation Fallbacks for Reduced Motion
**Learning:** While CSS handles declarative animation reduction, JavaScript-driven animations (like high-frequency text scrambles) can cause motion sickness if not explicitly stopped.
**Action:** Always wrap JS-driven animation logic with `if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;` to provide an immediate static fallback.
