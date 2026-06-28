## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-06-28 - ARIA Labels for Stylistic Punctuation
**Learning:** In minimal design systems, stylistically punctuated text links (like `[home]`) cause screen readers to read the punctuation verbatim (e.g., "left bracket home right bracket"), producing auditory clutter.
**Action:** Always add descriptive `aria-label` attributes to such links to override the visually stylistic text and ensure a clean screen reader experience.
