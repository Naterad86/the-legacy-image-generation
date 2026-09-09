# Gallery validation

**Passed: 49/49 checks.** The final [Legacyify gallery](../index.html) was tested with its actual campaign data: three actions, ten displayed examples, and twelve recorded attempts.

- Character, Scene, and Together load their result and source images; comparison and example selection work.
- Keyboard action navigation and Copy request work. The walkthrough starts closed and opens on demand.
- All 19 displayed local image and record links resolve, including the attempt ledger, reusable actions, and resume plan.
- Desktop, 390-pixel mobile, 320-pixel narrow view, and 200% text enlargement had no page overflow. Mobile comparisons stack with each image's aspect ratio preserved.
- No JavaScript errors or failed file requests occurred. Desktop and mobile screenshots were visually inspected for readable content, correct image display, and layout defects.

Tested in installed Microsoft Edge 152.0.4191.66, running headlessly with an isolated temporary profile. This validates the gallery and its packaging; it does not establish image-generation reliability or replace the individual image evaluations. No source or generated image pixels were changed, and no further images were generated.

## Screenshot evidence

[Character](qa/desktop-character.png) · [Scene](qa/desktop-scene.png) · [Together](qa/desktop-together.png) · [Expanded walkthrough and ledger](qa/desktop-walkthrough.png) · [Mobile source/result comparison](qa/mobile-compare.png)

## Validated snapshot

- Checked at: 2026-09-09T11:55:13.845Z
- Gallery data SHA-256: `f28339bb2ffcfea959fd6800e5ccc01c43df28994a8e9cc5122ee271cb56eb0b`
- The data remained unchanged during the check. Browser contexts closed after testing; no QA service was left running.
