## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-20 - Aria labels for stylistic bracket links
**Learning:** Screen readers produce auditory clutter by announcing stylistically punctuated text links (like `[home]`) verbatim (e.g., "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to override visually stylistic punctuation in minimal or terminal-like design systems.
