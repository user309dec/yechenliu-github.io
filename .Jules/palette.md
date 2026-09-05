## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-09-06 - JS Animation Fallbacks for Reduced Motion

**Learning:** While CSS media queries easily disable declarative animations, JavaScript-driven animations (like the high-frequency text scramble effect) must be explicitly bypassed within the script using `window.matchMedia("(prefers-reduced-motion: reduce)").matches` to prevent motion sickness.
**Action:** Always check `window.matchMedia` for `prefers-reduced-motion` before executing complex, fast-paced JavaScript animations, and provide an immediate fallback state.
