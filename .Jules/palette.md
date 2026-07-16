## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-07-16 - Stylistic Link Punctuation
**Learning:** Minimalist or terminal-like designs often punctuate text links with brackets (e.g., `[home]`), causing screen readers to announce the punctuation verbatim (e.g., "left bracket home right bracket"), creating auditory clutter.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to stylistically punctuated links to override the visual text for assistive technologies.
