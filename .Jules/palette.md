## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylistically Punctuated Text Links
**Learning:** Stylistically punctuated text links (e.g., `[home]`) cause auditory clutter for screen readers as they announce the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** In minimal/terminal design systems, always provide descriptive `aria-label` attributes (e.g., `aria-label="home"`) on stylistically punctuated links to override the visible text for assistive technologies.
