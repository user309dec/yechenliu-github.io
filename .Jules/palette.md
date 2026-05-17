## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2026-05-17 - Aria-Labels for Stylistically Punctuated Links
**Learning:** In minimal design systems, links are often styled with punctuation like `[home]` or `[projects]`. Screen readers will read the brackets aloud (e.g., "left bracket home right bracket"), creating auditory clutter for visually impaired users.
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide a clean auditory experience.
