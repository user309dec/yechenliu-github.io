## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-10-24 - ARIA Labels for Punctuated Text Links
**Learning:** Minimal/terminal-like design systems often use text links with stylistic punctuation (e.g., `[home]`). Screen readers will announce the punctuation verbatim ("left bracket home right bracket"), creating unnecessary auditory clutter.
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated text links to override the visual text and provide a clean auditory experience for screen reader users.
