## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-04-09 - Reduced Motion Accessibility in JS & Smooth Scrolling
**Learning:** CSS `prefers-reduced-motion` doesn't automatically stop JavaScript-driven animations (like `setInterval` or `setTimeout`) or HTML `scroll-behavior: smooth`. Screen reader or motion-sensitive users may still trigger disruptive animations.
**Action:** Always explicitly check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to bypass motion logic, and ensure `scroll-behavior: auto` is added to the reduced motion CSS media query.
