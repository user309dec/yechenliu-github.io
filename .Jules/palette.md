## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-06-06 - ARIA Labels for Stylized Links
**Learning:** In minimal design systems, links are often wrapped in stylistic punctuation (e.g., `[home]`). Screen readers announce this punctuation (e.g., "left bracket home right bracket"), causing auditory clutter and reducing clarity.
**Action:** Always provide an overriding `aria-label` attribute (e.g., `aria-label="home"`) on stylistically punctuated text links to ensure a clean, understandable auditory experience.
