## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.
## 2024-05-18 - Stylistic Bracket Links Accessibility
**Learning:** In minimal/terminal design systems, stylistically punctuated text links (like `[home]`) cause auditory clutter for screen reader users by reading out the punctuation (e.g. "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to links decorated with stylistic punctuation to override the visual text.
