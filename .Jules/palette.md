## 2026-03-18 - Respecting `prefers-reduced-motion` in JS
**Learning:** Pure CSS `prefers-reduced-motion` rules do not automatically stop JavaScript-driven animations (like `setInterval` or `setTimeout` loops). In components that programmatically animate text or DOM elements over time, users sensitive to motion will still experience the animations despite their system settings.
**Action:** Always explicitly evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript before initiating interval-based or timeout-based visual effects, and immediately apply the final state if true.

## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
