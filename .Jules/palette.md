## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-14 - Punctuated Text Links
**Learning:** Stylistically punctuated text links (like `[home]`) cause screen readers to announce punctuation verbatim (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Always add descriptive `aria-label` attributes to punctuation-heavy text links to provide a cleaner screen reader experience while maintaining the visual style.
