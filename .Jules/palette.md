## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-04-11 - Respecting Reduced Motion in JS and Custom CSS
**Learning:** CSS `prefers-reduced-motion` media queries do not automatically stop JavaScript-driven animations (like `setTimeout`/`setInterval` loops) or native `scroll-behavior: smooth`. Relying solely on CSS media queries leaves JS animations running, which can trigger vestibular disorders.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JS to safely bypass custom animations, and remember to enforce `scroll-behavior: auto !important` in the reduced motion CSS media query.
