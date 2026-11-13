# Troubleshooting

## Page has no styling
Confirm style.css is beside index.html, check the link spelling, inspect the browser Network panel, and hard-refresh after deployment.

## Images are missing
Confirm images/ was deployed, check exact file casing, verify the path exists, and inspect for 404 or decoding errors. Linux hosts are case-sensitive.

## Videos do not autoplay
Autoplay can be restricted by browser policy, data saver, power saver, or user preferences. Confirm the file loads and test manual playback. The page should remain understandable without motion.

## Layout overlaps
Test just above and below 900px, 600px, and 408px. Inspect fixed heights, absolute positioning, and video offsets. Avoid broad image selectors that unintentionally affect unrelated content.

## Local server fails
Choose another port:

```bash
python -m http.server 8080
```

You can also open index.html directly or use another static server.

## Validator reports a missing asset
Run `python scripts/validate_site.py` from the repository root. Compare the reported path with the tracked file and correct the reference or restore the missing asset. Do not remove a reference just to silence the check if the page still needs the resource.

## GitHub Actions fails
Inspect the Validate static site step and run the same Python command locally. Typical causes are missing required files or incorrect local paths.

## External link fails
External support/legal pages are controlled by their owners. Verify the destination and update the URL if it moved. Do not create a lookalike support page.
