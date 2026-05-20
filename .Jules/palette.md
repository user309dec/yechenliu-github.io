## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylistic Punctuation in Links and Screen Readers
**Learning:** The portfolio uses stylistic brackets around links (like `[home]`), which screen readers will announce verbatim (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Add descriptive `aria-label` attributes to override visually stylistic text links, ensuring a cleaner auditory experience for screen reader users.
