## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-07-07 - Screen Reader Output for Bracketed Links
**Learning:** Stylistically punctuated text links (like `[home]`) cause screen readers to announce the punctuation verbatim (e.g., "left bracket home right bracket"), producing auditory clutter in minimal/terminal-like design systems.
**Action:** Always add descriptive `aria-label` attributes to override the visually stylistic text with a clean, punctuation-free accessible name.
