## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-24 - ARIA Labels for Punctuated Text Links
**Learning:** The portfolio uses stylistic punctuation (e.g., "[home]", "[cv]") for links, which causes screen readers to produce auditory clutter by announcing the punctuation verbatim.
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to such links to override the visual text and provide a clean, accessible auditory experience.
