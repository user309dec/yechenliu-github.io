## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylized Link Auditory Clutter
**Learning:** In minimal/terminal-like design systems, text links are often stylistically punctuated (e.g., `[home]`, `[github]`). Screen readers announce this punctuation verbatim ("left bracket home right bracket"), creating unnecessary auditory clutter for non-sighted users.
**Action:** Ensure stylistically punctuated text links have descriptive `aria-label` attributes added (e.g., `aria-label="home"`) to override the visually stylistic text for screen readers.
