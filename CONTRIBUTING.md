# Contributing

Thank you for considering a contribution. This repository is a static HTML/CSS learning project. Contributions should improve the quality, clarity, accessibility, or maintainability of the page without misrepresenting it as a real streaming service.

## Before starting
- Read this guide and the [Code of Conduct](CODE_OF_CONDUCT.md).
- Check existing issues and pull requests for overlapping work.
- For substantial changes, open an issue first and describe the problem and proposed approach.
- Confirm that any media you intend to add may be distributed in this repository.

## Development environment

No package installation or build command is required. Use a modern browser and optionally Python 3.

```bash
git clone https://github.com/Brajesh31/NETFLIX-CLONE.git
cd NETFLIX-CLONE
python -m http.server 8000
```

Open http://localhost:8000.

Run the local validator before submitting:

```bash
python scripts/validate_site.py
```

## Contribution areas
- Semantic HTML and accessible document structure.
- Responsive layout fixes.
- Clearer CSS organization and maintainable selectors.
- Correct alternative text and keyboard focus behavior.
- Better media fallback and reduced-motion handling.
- Documentation corrections.
- Asset optimization where redistribution rights are clear.
- Improvements to static-site validation.

## Scope and safety
- Keep the project static unless a separate, explicitly approved design adds a backend.
- Do not add real login, password collection, credential forwarding, payment, or subscription flows.
- Do not create deceptive account recovery or support pages.
- Do not add analytics or tracking without transparent disclosure and appropriate consent.
- Do not collect email addresses through visual placeholder fields.
- Do not claim a button or FAQ row works unless its behavior is implemented and tested.
- Do not add assets without checking ownership and distribution permission.

## Code and content expectations
- Prefer semantic HTML elements and meaningful class names.
- Keep CSS rules scoped and avoid fragile positional selectors for new content.
- Preserve relative asset paths and exact file casing.
- Keep text readable at narrow viewport widths and browser zoom.
- Avoid unnecessary dependencies. The current project does not need a frontend framework.
- Keep changes focused. Do not reformat unrelated files.
- Update documentation when structure, behavior, validation, or deployment changes.

## Branch and commit workflow
1. Create a branch from the latest main.
2. Make one focused change.
3. Run `python scripts/validate_site.py`.
4. Test the page in a browser.
5. Check desktop and mobile layouts.
6. Review keyboard behavior and focus visibility.
7. Capture screenshots for visual changes.
8. Commit with a clear message.
9. Open a pull request and complete the repository template.

Suggested branch names: `fix/mobile-overflow`, `feat/semantic-sections`, and `docs/deployment-guide`.

## Pull request requirements

Include the problem, implementation summary, affected files, validation commands and results, browser and viewport sizes checked, screenshots for visual changes, and remaining limitations.

A passing asset validator is not proof of accessibility or visual correctness. Report manual checks accurately.

## Review process

Reviewers may request changes when implementation is unclear, inaccessible, out of scope, unsafe, or unsupported by evidence. Changes that introduce credential collection, deceptive sign-in experiences, unauthorized tracking, or questionable media assets should not be merged.

## Questions

Use GitHub Issues for non-sensitive project questions. Follow [SECURITY.md](SECURITY.md) for sensitive security reports.
