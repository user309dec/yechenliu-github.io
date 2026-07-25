## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - ARIA Labels for Stylized Text Links
**Learning:** Minimalist, terminal-style designs often use punctuated text links (like `[home]`). Screen readers announce this punctuation (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and ensure a clean, understandable screen reader experience.
