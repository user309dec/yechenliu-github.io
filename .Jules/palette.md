## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-07-08 - Accessible Stylized Links
**Learning:** In minimalist designs, stylistically punctuated text links like "[home]" create auditory clutter for screen reader users by reading the punctuation verbatim.
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated text links to override the visual punctuation for screen readers.
