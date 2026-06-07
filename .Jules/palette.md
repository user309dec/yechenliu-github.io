## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-07 - Stylistically Punctuated Text Links
**Learning:** In minimal or terminal-like design systems, screen readers produce auditory clutter by announcing text link punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to override the visually stylistic text for screen readers.
