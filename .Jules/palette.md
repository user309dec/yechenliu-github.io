## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-09 - Screen Reader Clutter on Stylistic Links
**Learning:** In minimal design systems, stylistically punctuated text links (like `[home]`) produce auditory clutter for screen reader users, who hear the punctuation announced verbatim (e.g., "left bracket home right bracket").
**Action:** Add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide clear, concise auditory feedback.
