## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-11 - ARIA Labels for Stylistic Links
**Learning:** In minimal or terminal-like design systems, stylistically punctuated text links (like `[home]`) can produce auditory clutter for screen reader users (e.g., announcing "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to override visually stylistic text, ensuring clear and concise auditory feedback.
