# Security Policy

## Project security scope
This repository is a static HTML/CSS demonstration. It has no backend, authentication, database, payment processing, API keys, or account system. The visible sign-in and email call-to-action elements are not functional.

Do not use this project to collect streaming-service credentials or personal information. Do not represent it as an official Netflix website.

## Supported maintenance
Security reports concerning the current default branch are the priority. This project does not publish formal release versions or guarantee a response-time SLA.

## Reporting a vulnerability
Do not publish exploitable details, personal data, or secrets in a public issue.

Use GitHub private vulnerability reporting if enabled for this repository. Otherwise, contact the repository owner privately through GitHub with:
- A concise description of the issue.
- The affected file or page area.
- Reproduction steps that do not expose real user data.
- Potential impact and a safe suggested mitigation, if known.

Allow reasonable time for investigation before public disclosure.

## Security expectations for contributions
- Never commit passwords, API tokens, private keys, session data, or personal information.
- Do not add credential collection or deceptive sign-in/account recovery interfaces.
- Do not add undisclosed tracking or analytics.
- Do not load executable scripts or remote resources without a clear project need and review.
- Do not introduce forms that submit personal data without an explicit privacy and security design.
- Review third-party assets and external links before adding them.
- Keep GitHub Actions permissions limited to what a workflow needs.

## Third-party assets
Brand artwork, logos, images, and videos are not covered by the repository's MIT source-code license. Verify rights and provenance before redistributing or deploying them.

## If a backend is proposed
A backend is outside the current scope. Before implementation, require a threat model, secure authentication design, server-side authorization, input validation, abuse controls, privacy disclosures, secure secret storage, logging policy, and independent review. Never store real account credentials for a third-party service.
