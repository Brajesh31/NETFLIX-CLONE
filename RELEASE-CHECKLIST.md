# Release and Deployment Checklist

This repository does not currently publish versioned application releases. Use this checklist for a tagged snapshot or public static deployment.

## Scope and content
- [ ] Unofficial educational purpose is clear.
- [ ] No real login, payment, account, or email collection flow is implied.
- [ ] External links and documentation are current.

## Validation
- [ ] python scripts/validate_site.py passes.
- [ ] Page loads from repository root.
- [ ] Local images and videos load.
- [ ] Browser console has no new errors.
- [ ] Desktop, tablet, and mobile layouts reviewed.
- [ ] Keyboard focus, accessible names, and reduced-motion behavior reviewed.

## Rights
- [ ] Distribution rights for images, logos, and videos reviewed.
- [ ] Third-party assets are not represented as covered by MIT.
- [ ] No private or confidential media included.

## Deployment
- [ ] Static publish directory is repository root.
- [ ] HTTPS enabled.
- [ ] Relative asset paths work at deployment base path.
- [ ] Search indexing configuration is intentional.
- [ ] Deployed page smoke-tested.

## After deployment
- [ ] Record URL and commit SHA where appropriate.
- [ ] Check missing assets and unexpected caching.
- [ ] Document remaining limitations.
