## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - ARIA Labels for Punctuated Text Links
**Learning:** Minimalist or terminal-like designs often use stylistic punctuation around links (like `[home]`), which creates auditory clutter for screen reader users by announcing the brackets verbatim (e.g., "left bracket home right bracket").
**Action:** Explicitly add descriptive `aria-label` attributes to override visually punctuated text, ensuring clean and semantic announcements for assistive technologies.
