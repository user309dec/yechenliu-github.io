## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-03 - Descriptive ARIA labels for punctuated links
**Learning:** In minimal design systems, stylistically punctuated text links (like `[home]`) cause auditory clutter for screen reader users by announcing punctuation verbatim.
**Action:** Add descriptive `aria-label` attributes to override the visually stylistic text and provide clear, unpunctuated link text for screen readers.
