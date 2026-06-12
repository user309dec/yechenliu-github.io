## 2024-05-15 - Focus Visible Styles for Link Navigation

**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-16 - ARIA labels for punctuated text links

**Learning:** In minimal/terminal-like designs, text links are often wrapped in punctuation like "[home]" for style. Screen readers announce this auditory clutter ("left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes to stylistically punctuated links to override the visual text and provide a clean auditory experience for screen reader users.
