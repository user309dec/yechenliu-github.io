## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylistically Punctuated Links Auditory Clutter
**Learning:** In minimal design systems, links are sometimes styled with punctuation (like `[home]`). While visually stylistic, this causes screen readers to read the punctuation verbatim (e.g., "left bracket home right bracket"), leading to auditory clutter and a degraded experience for screen reader users.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to stylistically punctuated text links to override the visible text and ensure screen readers read only the meaningful link destination.
