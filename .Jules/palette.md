## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-17 - Javascript Animations Should Check `prefers-reduced-motion`
**Learning:** CSS `prefers-reduced-motion` only affects CSS animations and transitions automatically. Any custom JavaScript-driven animations (like the text scramble effect used here) will continue to run unless explicitly disabled by checking `window.matchMedia("(prefers-reduced-motion: reduce)").matches`. Failing to do so can trigger motion sickness or vestibular issues for sensitive users, even if they enabled the OS-level accessibility setting.
**Action:** Always check `window.matchMedia` for `prefers-reduced-motion` before starting complex JS animations, and provide an immediate, motion-free fallback state.
