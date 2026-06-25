## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-06-25 - ARIA Labels for Stylistic Punctuation
**Learning:** In minimal or terminal-like design systems, stylistic punctuation in text links (like `[home]`) can produce auditory clutter for screen readers (e.g., "left bracket home right bracket").
**Action:** Add descriptive `aria-label` attributes to override the visually stylistic text with clear, punctuation-free announcements.
