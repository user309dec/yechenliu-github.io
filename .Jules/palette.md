## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-10-26 - JS-Driven Animations and Prefers-Reduced-Motion

**Learning:** While declarative CSS animations are easily disabled via `@media (prefers-reduced-motion: reduce)`, JavaScript-driven animations (like rapid text scrambling effects) bypass CSS rules and must be manually suppressed in the logic to prevent triggering motion sickness or vestibular discomfort.
**Action:** Always verify `window.matchMedia("(prefers-reduced-motion: reduce)").matches` in scripts before executing high-frequency visual updates or staggered content reveals, providing an immediate fallback state if true.
