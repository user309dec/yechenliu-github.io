## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-25 - ARIA Labels for Stylistic Links
**Learning:** In minimal design systems, text links are often stylistically punctuated (e.g., `[home]`). This creates auditory clutter for screen reader users who hear the punctuation read verbatim.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to stylistically punctuated links to override the visual text for assistive technologies.
