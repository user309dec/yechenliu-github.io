## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-20 - Stylistically Punctuated Text Links
**Learning:** In minimal or terminal-like design systems, text links are often stylistically punctuated (like `[home]`). This causes screen readers to produce auditory clutter by announcing the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Ensure stylistically punctuated text links have descriptive `aria-label` attributes added. This overrides the visually stylistic text for screen reader users.
