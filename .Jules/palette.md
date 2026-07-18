## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-07-18 - ARIA Labels for Punctuated Text Links
**Learning:** In minimal design systems, stylistically punctuated text links (like `[home]`) can create auditory clutter for screen reader users by announcing the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated text links to override the visual text and provide a clean, descriptive announcement for screen readers.
