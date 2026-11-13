# Accessibility Review

This is a visual demonstration, not a formally audited accessible product. Responsive CSS alone does not establish accessibility.

## Known areas
- The current markup uses non-standard p1, p2, and p3 elements for styled text. Replace them with semantic headings and paragraphs.
- Use header, nav, main, section, and footer landmarks.
- The language and sign-in buttons are not wired to actions. Email fields are not real forms. Clearly identify placeholders and never collect real data.
- FAQ rows are static content, not expandable controls.
- Review image alternative text. Decorative images should not create redundant announcements.
- Decorative videos should not communicate essential information and should respect reduced-motion preferences.
- Keep keyboard focus visible and navigation order logical.
- Check text contrast and test zoom to 200% and reflow at 320 CSS pixels.

## Manual review
1. Navigate with Tab and Shift+Tab only.
2. Inspect landmarks and heading order with a screen reader.
3. Disable or block media and confirm the page remains understandable.
4. Enable reduced motion and inspect decorative motion.
5. Check contrast, zoom, and small-screen reflow.

This document is a checklist, not a claim of WCAG conformance.
