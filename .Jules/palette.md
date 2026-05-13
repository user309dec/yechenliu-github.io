## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - ARIA Labels for Stylized Punctuation in Links
**Learning:** In terminal-like or minimal design systems, links are often surrounded by stylized punctuation like brackets (e.g., `[home]`). Screen readers will announce this punctuation verbatim ("left bracket home right bracket"), causing auditory clutter and degrading the UX for visually impaired users.
**Action:** Always add descriptive `aria-label` attributes to override visually stylized text containing non-semantic punctuation, ensuring a clean and direct screen reader experience.
