## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylistic Punctuation Auditory Clutter
**Learning:** Stylistically punctuated text links (like `[home]`) cause screen readers to read the punctuation aloud (e.g., "left bracket home right bracket"), creating unnecessary auditory clutter for visually impaired users.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to links that use punctuation purely for visual style, overriding the text content for screen readers.
