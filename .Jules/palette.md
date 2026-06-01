## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - Stylistically Punctuated Text Links
**Learning:** The portfolio features text links styled with brackets (e.g., `[home]`, `[github]`). Screen readers announce these verbatim, creating auditory clutter (e.g., "left bracket home right bracket").
**Action:** In minimal design systems, add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide a cleaner auditory experience for screen reader users.
