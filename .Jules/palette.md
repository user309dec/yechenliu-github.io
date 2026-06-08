## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-08 - Descriptive ARIA Labels for Punctuated Links
**Learning:** The minimal design uses stylized links wrapped in brackets (e.g., `[home]`). While visually striking, screen readers announce this punctuation verbatim, creating unnecessary auditory clutter.
**Action:** Add descriptive `aria-label` attributes (e.g., "Home") to stylistically punctuated links to ensure clean, meaningful announcements for screen reader users without altering the visual design.
