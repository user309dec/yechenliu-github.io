## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2025-02-14 - Aria Labels for Punctuated Text Links
**Learning:** Stylistically punctuated text links (like `[home]`) can produce auditory clutter for screen readers, as they may read the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Add descriptive `aria-label` attributes to these links to provide a clean auditory experience while preserving the visual style.
