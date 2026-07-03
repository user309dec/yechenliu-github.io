## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - ARIA Labels on Stylistically Punctuated Links
**Learning:** Stylistically punctuated text links like `[home]` or `[cv]` create auditory clutter for screen reader users, as the punctuation is often read aloud verbatim (e.g., "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visible text and provide clean, concise auditory announcements.
