## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - JS Animations and Reduced Motion
**Learning:** While CSS media queries successfully manage declarative CSS animations, JavaScript-driven animations (like high-frequency text scramble effects) ignore them. Users with motion sensitivity could still experience motion sickness from JS-driven text scrambling.
**Action:** Always explicitly check `window.matchMedia("(prefers-reduced-motion: reduce)").matches` within JavaScript logic to provide an immediate fallback state and disable intense programmatic animations.
