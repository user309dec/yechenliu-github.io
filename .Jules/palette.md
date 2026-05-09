## 2024-05-15 - Focus Visible Styles for Link Navigation
**Learning:** The portfolio relies on links for both internal section routing and external profiles, but lacked explicit focus states. Keyboard users would only see browser default focus rings, which often have low contrast against custom backgrounds.
**Action:** Always pair `:hover` states with `:focus-visible` styles to ensure consistent, highly visible feedback for keyboard users without affecting the mouse experience.

## 2024-05-24 - Screen Reader Noise from Stylistic Brackets
**Learning:** The portfolio uses a minimalist terminal-like aesthetic with brackets around links (e.g., `[home]`). While visually distinctive, screen readers announce these verbatim as "left bracket home right bracket", causing significant auditory clutter for non-visual users navigating the site.
**Action:** Always provide clean `aria-label` attributes on stylistically punctuated text links to ensure a natural and concise screen reader experience without compromising the visual design.
