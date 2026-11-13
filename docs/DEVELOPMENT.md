# Development Guide

## Prerequisites
Use a modern browser. Python 3 is optional for a local server and validation. No Node.js, package manager, build system, or dependency installation is required.

## Clone and run
```bash
git clone https://github.com/Brajesh31/NETFLIX-CLONE.git
cd NETFLIX-CLONE
python -m http.server 8000
```
Open http://localhost:8000. Stop the server with Ctrl+C. If port 8000 is busy, use another port such as 8080.

## Editing
- Edit index.html for page content, metadata, links, and media references.
- Edit style.css for layout, typography, colors, responsive behavior, and overlays.
- Put approved image assets in images/ and video assets in video/.
- Preserve relative paths and exact filename casing.
- Prefer semantic HTML, scoped CSS classes, visible focus styles, and responsive sizing.
- Do not add credential collection, fake sign-in, payment, or membership flows.

## Validate
Run `python scripts/validate_site.py` from the repository root. Then open the page in a browser, inspect console/network errors, check media loading, resize through breakpoints, and test keyboard navigation.

## Contribution workflow
Create a focused branch, make one coherent change, run validation, test affected viewports, capture screenshots for visual changes, update docs, and open a pull request using the repository template.
