window.LEGACY_GALLERY = {
  "title": "Legacyify — The overnight demo",
  "subtitle": "Three images. Three actions. Start with the results.",
  "date": "9 SEPTEMBER 2026",
  "note": "Prototype boundaries: clear poses, recognizable canonical identities and readable scene structure. Fine facial geometry and exact logos are not locked. Development sources are synthetic; this is not a held-out reliability qualification.",
  "actions": [
    {
      "id": "character",
      "name": "Character",
      "headline": "Borrow the pose. Keep the character.",
      "summary": "A supplied pose becomes a canonical Legacy character, with explicit separation of pose and identity.",
      "status": "Demonstrated with fidelity limits",
      "boundary": "Best fit: one clear full-body pose, a familiar face angle and one canonical master. Exact facial construction, extreme views and complex hands remain conditional.",
      "command": "Read and use C:\\Users\\galip\\Documents\\Codex\\2026-09-09\\t\\outputs\\legacyify\\workflow\\legacyify-skill\\SKILL.md. Legacyify Character: use my attached image for pose and framing only, and the canonical Legacy male master for identity, proportions, black outfit and illustrated rendering. Keep blunt master-matched fingertips; no invented dark claws. Briefly state any input boundary, then make one image request and show the result before explaining. Record the attempt.",
      "examples": [
        {
          "title": "Borrow a human pose",
          "source": "sources/DEVELOPMENT_HUMAN_POSE.png",
          "output": "selected/character-pose-transfer.png",
          "sourceLabel": "Synthetic pose source",
          "sourceAlt": "Fictional human presenter in a blue shirt making an open-hand gesture.",
          "outputAlt": "Canonical Legacy male lion in black clothing performing the reference pose.",
          "note": "Pose-only transfer with canonical identity, outfit and illustrated rendering. C04 corrects the invented claws from C03; fine face/mane variation remains. Both development calls are disclosed.",
          "outcome": "Practical pass · disclosed revision",
          "attemptId": "C04",
          "record": "records/review-C04.md",
          "extraSources": [
            {
              "src": "sources/LEGACY_MALE_CHARACTER_MASTER.jpg",
              "label": "Male identity authority"
            }
          ]
        },
        {
          "title": "The female, arms folded",
          "source": "sources/LEGACY_FEMALE_CHARACTER_MASTER.jpg",
          "output": "attempts/C02-raw.png",
          "note": "Practical pass for recognizable continuity and a clean new pose. Fine eye, muzzle and hair details vary.",
          "outcome": "Practical pass · fine fidelity varies",
          "attemptId": "C02",
          "record": "records/review-C02.md"
        },
        {
          "title": "The male, welcoming",
          "source": "sources/LEGACY_MALE_CHARACTER_MASTER.jpg",
          "output": "attempts/C01-raw.png",
          "note": "Polished controlled gesture; exact face and mane geometry remain conditional.",
          "outcome": "Conditional",
          "attemptId": "C01",
          "record": "records/review-C01.md"
        },
        {
          "title": "Earlier pose-transfer trial",
          "source": "sources/DEVELOPMENT_HUMAN_POSE.png",
          "output": "attempts/C03-raw.png",
          "note": "The human's wardrobe and identity did not leak. Invented dark claw tips prompted the recorded C04 revision.",
          "outcome": "Conditional · invented claws",
          "attemptId": "C03",
          "record": "records/review-C03.md"
        }
      ]
    },
    {
      "id": "scene",
      "name": "Scene",
      "headline": "Keep the place. Change the medium.",
      "summary": "A readable source scene becomes deliberate pixel art with its important objects and relationships retained.",
      "status": "Practical pass on developed example",
      "boundary": "Best fit: legible scenes with a few salient structures. Fine contours and small details can drift. Exact text, exact logos, survey geometry and a guaranteed native pixel grid are outside this demonstration.",
      "command": "Read and use C:\\Users\\galip\\Documents\\Codex\\2026-09-09\\t\\outputs\\legacyify\\workflow\\legacyify-skill\\SKILL.md. Legacyify Scene: transform my attached scene into deliberate pixel art using Legacy visual discipline. Preserve its spatial story, camera, salient objects, shape families, counts and lighting direction. Inspect and explicitly name fragile details such as round fixtures, paths and required text before one image request. Style-only, no added logos. Show the result before the walkthrough and record the attempt.",
      "examples": [
        {
          "title": "An alpine terrace, in pixels",
          "source": "sources/DEVELOPMENT_ALPINE_TERRACE.png",
          "output": "selected/scene-pixel-terrace.png",
          "sourceLabel": "Synthetic development scene",
          "note": "Practical pass. The round lamp and gentle path survived the targeted S03 revision. Fine geometry varies; the exact native pixel grid is unverified. Style-only: no logo was requested.",
          "outcome": "Practical pass · development revision",
          "attemptId": "S03",
          "record": "records/review-S03.md"
        },
        {
          "title": "The office becomes a game scene",
          "source": "sources/LEGACY_OFFICE_MASTER.jpg",
          "output": "attempts/S01-raw.png",
          "note": "Convincing pixel medium and retained major layout. Secondary branding was intentionally removed. The main emblem is an approximation, not exact canonical geometry.",
          "outcome": "Conditional · emblem fidelity fails",
          "attemptId": "S01",
          "record": "records/review-S01.md",
          "extraSources": [
            {
              "src": "sources/LEGACY_LOGO_MASTER.jpg",
              "label": "Required emblem authority"
            }
          ]
        },
        {
          "title": "Earlier outdoor transfer",
          "source": "sources/DEVELOPMENT_ALPINE_TERRACE.png",
          "output": "attempts/S02-raw.png",
          "note": "The lamp became rectangular and the path/skyline drifted. Kept here so the development revision is visible.",
          "outcome": "Conditional · salient geometry drift",
          "attemptId": "S02",
          "record": "records/review-S02.md"
        }
      ]
    },
    {
      "id": "together",
      "name": "Together",
      "headline": "Give the scene a Legacy presence.",
      "summary": "Canonical illustrated characters inhabit a supplied scene through scale, contact, perspective and shared light.",
      "status": "Integration demonstrated; exact fidelity conditional",
      "boundary": "Best fit: one visible character and simple placement, preserving the source's environmental medium. Two separated characters worked in one exploratory case; touching poses and exact scene reconstruction remain experimental.",
      "command": "Read and use C:\\Users\\galip\\Documents\\Codex\\2026-09-09\\t\\outputs\\legacyify\\workflow\\legacyify-skill\\SKILL.md. Legacyify Together: use my attached image as the environment authority and add one canonical Legacy character in a clearly visible, naturally grounded position. Preserve the supplied environment medium; keep the character illustrated and match perspective, scale, light, contact and shadows. Choose the appropriate canonical master. No added branding. State the placement boundary briefly, make one image request, show the result first and record it.",
      "examples": [
        {
          "title": "A canonical character takes the chair",
          "source": "sources/LEGACY_OFFICE_MASTER.jpg",
          "output": "selected/together-office.png",
          "note": "The illustrated lioness integrates with the rendered office through scale, occlusion and lighting. Exact emblem fidelity fails; face details vary. This is a usable visual candidate, not an exact-brand release.",
          "outcome": "Conditional · integration demonstrated",
          "attemptId": "T01",
          "record": "records/review-T01.md",
          "extraSources": [
            {
              "src": "sources/LEGACY_FEMALE_CHARACTER_MASTER.jpg",
              "label": "Female identity authority"
            },
            {
              "src": "sources/LEGACY_LOGO_MASTER.jpg",
              "label": "Emblem authority"
            }
          ]
        },
        {
          "title": "Two identities, one shared scene",
          "source": "sources/DEVELOPMENT_ALPINE_TERRACE.png",
          "output": "selected/together-two-characters.png",
          "note": "Practical pass in an exploratory two-character extension: distinct identities and coherent ground contact. Figures are larger than the requested 60% of frame height. Background medium was explicitly preserved.",
          "outcome": "Practical pass · exploratory",
          "attemptId": "T03",
          "record": "records/review-T03.md",
          "extraSources": [
            {
              "src": "sources/LEGACY_MALE_CHARACTER_MASTER.jpg",
              "label": "Male authority"
            },
            {
              "src": "sources/LEGACY_FEMALE_CHARACTER_MASTER.jpg",
              "label": "Female authority"
            }
          ]
        },
        {
          "title": "One character outdoors",
          "source": "sources/DEVELOPMENT_ALPINE_TERRACE.png",
          "output": "attempts/T02-raw.png",
          "note": "Strong source-preserving insertion. The requested separate CGI conversion is not demonstrated, and figure scale exceeded the brief. Those misses remain in the record.",
          "outcome": "Conditional · CGI conversion unproven",
          "attemptId": "T02",
          "record": "records/review-T02.md",
          "extraSources": [
            {
              "src": "sources/LEGACY_MALE_CHARACTER_MASTER.jpg",
              "label": "Male authority"
            }
          ]
        }
      ]
    }
  ],
  "walkthrough": [
    {
      "title": "The input carries a role",
      "text": "A human can supply pose without supplying face or clothes. A scene supplies camera and contents. Exact male/female masters supply identity. The office supplies abstract art direction only where assigned; it does not send its furniture into another landscape."
    },
    {
      "title": "One invocation, one raw result",
      "text": "The action inspects the source, names consequential properties, selects a medium and compiles a focused request. It makes one built-in image call and preserves the untouched output. C04 and S03 are openly recorded development revisions, each starting from original authorities; earlier misses remain visible."
    },
    {
      "title": "Practical acceptance and exact fidelity differ",
      "text": "A visually coherent, recognizable result can be useful while missing exact face, brand or geometry requirements. A separate agent reviewed the outputs. These small, changing development examples do not prove a reliability percentage or replace formal held-out evaluation."
    },
    {
      "title": "Try your three images",
      "text": "Attach a clear pose image, a readable scene, and a scene with room for a character in Codex. Use the request under each action. The local gallery cannot generate images itself; the included portable skill and helper make the Codex workflow repeatable without a separately billed API."
    }
  ],
  "attempts": [
    {
      "id": "C01",
      "action": "Character",
      "outcome": "Conditional",
      "note": "Welcoming male; fine face/mane drift.",
      "record": "records/review-C01.md"
    },
    {
      "id": "S01",
      "action": "Scene",
      "outcome": "Conditional",
      "note": "Pixel office; main emblem topology differs.",
      "record": "records/review-S01.md"
    },
    {
      "id": "T01",
      "action": "Together",
      "outcome": "Conditional",
      "note": "Lioness office integration; exact emblem fails.",
      "record": "records/review-T01.md"
    },
    {
      "id": "E01",
      "action": "Synthetic source",
      "outcome": "Setup output",
      "note": "Alpine scene; not a real photo or held-out source.",
      "record": "attempts/E01-prompt.txt"
    },
    {
      "id": "S02",
      "action": "Scene",
      "outcome": "Conditional",
      "note": "Pixel terrace; rectangular lamp and geometry drift.",
      "record": "records/review-S02.md"
    },
    {
      "id": "C02",
      "action": "Character",
      "outcome": "Practical pass",
      "note": "Female crossed arms; fine identity variation remains.",
      "record": "records/review-C02.md"
    },
    {
      "id": "T02",
      "action": "Together",
      "outcome": "Conditional",
      "note": "Strong insertion; CGI conversion unproven, scale miss.",
      "record": "records/review-T02.md"
    },
    {
      "id": "E02",
      "action": "Synthetic source",
      "outcome": "Setup output",
      "note": "Fictional human pose reference.",
      "record": "attempts/E02-prompt.txt"
    },
    {
      "id": "C03",
      "action": "Character",
      "outcome": "Conditional",
      "note": "Pose-only transfer; invented dark claws.",
      "record": "records/review-C03.md"
    },
    {
      "id": "S03",
      "action": "Scene",
      "outcome": "Practical pass",
      "note": "Disclosed S02 revision; round lamp/path retained.",
      "record": "records/review-S03.md"
    },
    {
      "id": "T03",
      "action": "Together",
      "outcome": "Practical pass · exploratory",
      "note": "Two identities separated; figure-height target missed.",
      "record": "records/review-T03.md"
    },
    {
      "id": "C04",
      "action": "Character",
      "outcome": "Practical pass",
      "note": "Disclosed revision: blunt fingertips corrected; source-role isolation retained.",
      "record": "records/review-C04.md"
    }
  ],
  "records": [
    {
      "label": "All attempts and findings",
      "href": "records/ATTEMPT_LEDGER.md"
    },
    {
      "label": "Reusable actions",
      "href": "ACTIONS.md"
    },
    {
      "label": "Portable skill",
      "href": "workflow/legacyify-skill/SKILL.md"
    },
    {
      "label": "Workflow helper",
      "href": "workflow/README.md"
    },
    {
      "label": "Resume plan",
      "href": "records/RESUME.md"
    }
  ],
  "budget": "Account snapshot: 62% remaining at 11:51 UTC; 3 percentage points more used than at the start across the shared account. No refresh redeemed. See the saved budget record for the observed state."
};
