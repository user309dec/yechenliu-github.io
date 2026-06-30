## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-10-24 - Screen Reader Clutter from Stylized Links

**Learning:** In minimal design systems, text links are often stylistically punctuated (e.g. `[home]`). Screen readers will announce the punctuation verbatim (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide clean auditory navigation.
