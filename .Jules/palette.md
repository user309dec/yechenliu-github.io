## 2024-05-24 - Screen Reader Verbosity on Stylized Links
**Learning:** In minimal design systems, stylistically punctuated text links (like `[home]`) cause auditory clutter for screen reader users by announcing the punctuation verbatim (e.g., "left bracket home right bracket").
**Action:** Always add descriptive `aria-label` attributes (e.g., `aria-label="home"`) to stylized links to override the visual punctuation and provide clean auditory feedback.
