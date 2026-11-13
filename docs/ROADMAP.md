# Roadmap

This is a list of possible improvements, not a delivery commitment.

## Priority 1: Semantics and accessibility
- Replace p1, p2, and p3 with semantic headings and paragraphs.
- Add document landmarks and clear section headings.
- Improve visible focus styles and keyboard behavior.
- Add a reduced-motion strategy for decorative video.
- Clarify that visual placeholders do not perform real actions.
- Review alt text and contrast.

## Priority 2: Responsive reliability
- Replace unnecessary fixed heights with content-driven sizing.
- Consolidate repeated FAQ selectors into reusable classes.
- Make media overlays container-relative.
- Test intermediate widths, landscape phones, and 320px reflow.
- Narrow broad image sizing selectors.

## Priority 3: Performance
- Audit image and video file sizes.
- Provide poster/fallback imagery.
- Consider lazy loading below-the-fold media.
- Verify usefulness with autoplay disabled.

## Priority 4: Quality automation
- Add HTML conformance validation.
- Add reviewed accessibility checks.
- Consider browser smoke tests if project complexity justifies them.
- Consider visual regression tests after layout stabilizes.

Real accounts, streaming, payment, subscriptions, or credential collection are out of scope for incremental UI work. They require separate product, legal, privacy, and security design.
