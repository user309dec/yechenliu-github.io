## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-20 - Stylistic Punctuation in Links
**Learning:** In minimal or terminal-like design systems, ensure stylistically punctuated text links (like `[home]`) have descriptive `aria-label` attributes added. This overrides the visually stylistic text and prevents screen readers from producing auditory clutter by announcing the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Always add clean `aria-label`s to links when visually stylizing their text content with ASCII punctuation.
