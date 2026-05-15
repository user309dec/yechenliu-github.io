## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Screen Reader Accessibility for Stylized Punctuation Links
**Learning:** In minimal or terminal-like design systems, text links are often stylized with punctuation (e.g., `[home]`, `[projects]`). Screen readers announce this punctuation verbatim, producing auditory clutter (e.g., "left bracket home right bracket link").
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visually stylistic text and ensure a clean screen reader experience (e.g., `aria-label="home"`).
