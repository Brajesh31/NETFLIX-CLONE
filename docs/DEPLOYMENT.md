# Static Deployment

## Hosting model
Any static web host can serve this repository. There is no backend runtime, database, environment variable, or build step. The publish directory is the repository root and the entry point is index.html.

## Required content
Deploy index.html, style.css, images/, video/, and favicon.ico if desired. Uploading only the HTML file will break styles and media.

## Generic procedure
1. Connect the repository or upload the complete static directory.
2. Set the publish directory to the repository root.
3. Leave the build command empty unless the host requires a no-op value.
4. Deploy over HTTPS.
5. Open the deployed page and inspect the Network panel for missing assets.

Provider settings vary. Follow the host's current static-site instructions rather than applying framework-specific build settings.

## Subdirectory hosting
HTML and CSS use relative asset paths. Preserve the directory structure and avoid root-absolute paths unless deployment is guaranteed to be at the domain root. File casing must match exactly on case-sensitive hosts.

## Pre-deployment
- [ ] All required files are included.
- [ ] HTTPS is enabled by the host.
- [ ] Images, videos, and CSS return successful responses.
- [ ] Desktop and mobile layouts are checked.
- [ ] External links are correct.
- [ ] Unofficial educational purpose is clear.
- [ ] Third-party asset rights are reviewed.
- [ ] No real credential or personal-data collection exists.

The current page includes a noindex, nofollow robots directive. Do not remove it without considering brand confusion and the purpose of the deployment. This repository has no application monitoring, server logs, form processing, or account system.
