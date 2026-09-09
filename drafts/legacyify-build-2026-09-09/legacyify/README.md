# Legacyify — overnight demo

Open **[the demo](index.html)**. Start with Character, Scene, and Together. The source comparisons, extra examples, walkthrough, and complete attempt record are available after the images.

## Three things to try

1. **Character:** borrow a clear human pose while using a canonical Legacy character for identity, build, outfit, and illustration.
2. **Scene:** turn a readable place into deliberate pixel art while retaining its important objects and spatial story.
3. **Together:** integrate a canonical illustrated character into a supplied environment. A two-character extension is also demonstrated.

These are working Codex prototypes. The gallery itself does not generate images. Copy an action request from the gallery and attach your new image in Codex. The [portable skill](workflow/legacyify-skill/SKILL.md) and [workflow helper](workflow/README.md) contain the reusable process. Nothing needs a separately billed API key, and no skill was installed globally.

## Boundaries before the demo

Recognizable identity, pose/reference-role separation, deliberate pixel style, and convincing character integration are demonstrated on the saved examples. Exact face geometry, exact logo geometry, tiny text, survey-level scene reconstruction, and arbitrary unseen inputs are not established. The two-character example is exploratory. Photographic-to-CGI conversion was not demonstrated in T02.

Twelve image calls are accounted for: ten action outputs and two synthetic source images. Four action outputs received a practical pass and six were conditional under separate-agent visual review. This changing development sample is not a reliability benchmark; do not turn those counts into a product success-rate claim. Two final outputs follow openly recorded development revisions. Original outputs were never repaired, cropped or re-encoded.

The human pose and alpine terrace are generated development sources, not real photographs or held-out evaluation examples. Canonical source files were retrieved from the current Drive manifest and verified by SHA256. Historical campaign verdicts and canonical authority remain unchanged.

## Files

- [Recommended fresh-image actions](ACTIONS.md)
- [All attempts and findings](records/ATTEMPT_LEDGER.md)
- [Source strategy and current repository references](records/SOURCE_STRATEGY.md)
- [Exact image-tool call arguments](records/ACTUAL_TOOL_CALLS.json)
- [Resume point](records/RESUME.md)
- [Original source files](sources/)
- [Selected unchanged outputs](selected/)

Keep this folder's structure intact. The HTML, JavaScript and images work locally without network access; image generation still runs through Codex's built-in image tool when you invoke a new action. No assets were published to a public site.
