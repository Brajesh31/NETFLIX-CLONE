# Testing Guide

## Automated validation
Run from the repository root:

```bash
python scripts/validate_site.py
```

The script checks required files and local HTML/CSS resource references. It does not prove HTML conformance, accessibility, visual correctness, or browser compatibility.

## Manual browser matrix

| Environment | Suggested viewport | Focus |
|---|---:|---|
| Desktop | 1440 x 900 | Hero, feature rows, footer |
| Laptop | 1280 x 720 | Vertical spacing and media crop |
| Tablet | 768 x 1024 | Stacking and FAQ width |
| Mobile | 390 x 844 | Navigation and wrapping |
| Small mobile | 320 x 700 | Overflow and clipping |

Check just above and below the current CSS breakpoints: 900px, 600px, and 408px.

## Manual checks
- Open through a local HTTP server.
- Confirm stylesheet, images, and videos load.
- Inspect browser console and network errors.
- Verify external links.
- Confirm placeholder controls do not imply real submission or authentication.
- Test keyboard navigation, focus visibility, contrast, zoom, and reduced motion.
- Check the deployed page after hosting.

## Pull request acceptance
- [ ] Validator passes.
- [ ] Browser checks completed for changed areas.
- [ ] Responsive layout reviewed.
- [ ] Local assets load.
- [ ] Keyboard and accessible names reviewed.
- [ ] Screenshots attached for visual changes.
- [ ] Documentation updated.
- [ ] No secrets, personal data, or unauthorized assets added.
