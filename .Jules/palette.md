## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Accessible Punctuated Links
**Learning:** In minimal or terminal-like design systems, text links are often stylistically punctuated (like `[home]`). This produces auditory clutter for screen readers by announcing the punctuation verbatim.
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide a clean experience for screen reader users.
