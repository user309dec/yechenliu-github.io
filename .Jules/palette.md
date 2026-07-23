## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-07-23 - ARIA Labels for Punctuated Text Links
**Learning:** In minimalist designs using bracketed text links like `[home]` or `[cv]`, screen readers will often announce the punctuation (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to stylistically punctuated text links to override the visual text and provide a clean experience for screen reader users.
