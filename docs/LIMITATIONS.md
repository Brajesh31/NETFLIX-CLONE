# Known Limitations

## Product scope
This is a static page, not a streaming service. Sign-in, language selection, email calls to action, download UI, and FAQ rows are presentation-only. There is no account, catalogue, search, recommendations, subscription, payment, playback service, form submission, or persistence.

## Markup and accessibility
- p1, p2, and p3 are non-standard custom-looking tags and should be replaced with semantic HTML.
- Several sections use generic div elements rather than semantic landmarks.
- Some controls visually imply actions that are not implemented.
- Accessibility has not been formally audited.
- Decorative video has no explicit user pause control.

## CSS and responsive behavior
- Fixed section heights can create excess whitespace or clipping.
- FAQ styles repeat positional selectors and are brittle when rows change.
- Video overlays use absolute positioning and fixed offsets.
- Some dimensions are fixed in pixels.
- A small-screen image rule affects broad descendant selectors.

## Performance and media
Media sizes should be reviewed for mobile bandwidth. No image optimization, media transcoding, or browser automation pipeline exists. Autoplay and media decoding vary by device.

## Rights and brand
Third-party-style branding and entertainment assets are present. The MIT license applies to original source code only. The repository does not establish rights to redistribute third-party media.

## Security
There is no backend or credential processing. Keep it that way unless a separately designed and reviewed service is introduced. A backend would require threat modeling, secure authentication, authorization, validation, abuse controls, privacy disclosures, and secret management.
