## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Reduced Motion Support for JS Animations and Native Scrolling
**Learning:** The `prefers-reduced-motion` CSS media query only affects CSS animations/transitions by default. It does not stop JavaScript-driven animations (like `setInterval` text scrambling) or native CSS properties like `scroll-behavior: smooth`.
**Action:** Always evaluate `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in JavaScript to explicitly bypass JS animation loops. Also enforce `scroll-behavior: auto !important` inside the CSS media query to ensure native smooth scrolling is disabled for users who prefer reduced motion.
