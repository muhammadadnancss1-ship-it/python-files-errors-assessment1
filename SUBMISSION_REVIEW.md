# Submission Review

Prepared 15 November 2026 for `python-files-errors-assessment`.

The attached README was read in full. The assessment field in the request still contains `[paste the assessment instructions here]`; no separate official brief or grading rubric was supplied. The task requirements below come from the supplied README and the user's delivery rules. They are not presented as an official marking scheme.

## 1. Requirement Inventory

### Assignment requirements recoverable from the supplied README

| Requirement | Submission location / behavior |
| --- | --- |
| Two independent Python applications | `expense_tracker.py` and `attendance_cleaner.py` |
| Expense menu: add, display, totals, exit | Four choices repeated by `main()` |
| Expenses persist across runs | Load and update `myExpenses1.csv` beside the expense script |
| Exact expense schema | `Date,Item,Amount,Category,Time,day`; case-sensitive headings |
| Required expense text fields | Date, item, category, time, day |
| Valid expense amount | Numeric, finite, zero or greater; retry invalid amounts |
| Category normalization and unique categories | Trim/lowercase for reporting; set comprehension; blank stored values become `uncategorized` |
| Totals by category | `sum()` with a generator expression |
| Safe expense handling | Validate stored data before editing; write temporary file before replacement; update memory after saving |
| Read attendance names from a text file | `attendance.txt`, one name per line |
| Attendance cleaning | List comprehension, `strip()`, `title()`, omit blank names |
| Attendance deduplication and ordering | `set()` followed by `sorted()` |
| Exact attendance output | `attendance_clean.csv` with `Student Name` heading |
| Attendance counts | Original count includes every input line; unique count excludes blank cleaned values |
| Required root files | `expense_tracker.py`, `attendance_cleaner.py`, `attendance.txt`, `README.md` |
| Repository / folder name | `python-files-errors-assessment` |
| Submission format | Public GitHub repository URL submitted on the LMS, as described in the supplied README |
| Official grading criteria and point weights | Not provided; cannot be verified or invented |
| Deadline / LMS course or assignment name | Not provided |

### Additional delivery requirements from the user's prompt

| Requirement | Completion |
| --- | --- |
| Read the source and list requirements before documenting the final work | Completed; source requirements inventoried here |
| Preserve required file names and root layout | Four root files preserved; only `assets/` added |
| Keep each task in its own file | Two separate Python modules |
| Clear names, constants, comments, small reusable functions | Implemented in both programs |
| Real normal, boundary, invalid, individual-failure and combined-failure checks | 58/58 scenarios passed on Python 3.12.14 |
| Verify syntax compilation | Both Python programs compiled successfully |
| README outputs must come from actual executions | Fresh terminal/output captures included in the verification support |
| `banner.svg` | 1000 × 260; white outer canvas, gradient banner, title, subtitle, concept chips, syntax-colored code |
| `overview.svg` | One task card each; file, topic, input, rules, output, concepts |
| One task flowchart per program | `expense_tracker_flow.svg` and `attendance_cleaner_flow.svg` |
| `uml_diagram.svg` | Procedural module view; actual constants, functions, calls, and file dependencies |
| Self-contained SVGs | No external fonts, images, scripts, or linked resources |
| Color semantics | Blue input, purple decision, green success, red errors, amber warning |
| Render and visually inspect all SVGs | All five rendered to PNG; connector overlap corrected and reviewed again |
| Exact opening banner HTML | Present at the start of `README.md` |
| README section order | Overview → folder tree → task sections → UML → concepts → run → samples → tests → author footer |
| Required content in each task section | Summary, rules, flow image, methods table, input validation, expected results |
| Relative repository image paths | All five README images use `assets/...` |
| Clone and run instructions plus alternate launchers | Included; username explicitly remains a placeholder |
| Test-case tables with #, scenario, inputs, expected result | One table per task; all 58 executed cases documented |
| One named repository folder and ZIP | `python-files-errors-assessment/` and `python-files-errors-assessment.zip` |
| Light and dark GitHub-style HTML previews outside the repository | Two offline HTML files with embedded diagrams and a theme switch |
| Short upload checklist | Included at the end of this review and in the delivery message |
| Assumptions and departures disclosed | Listed below |

## 2. What Was Completed

- Rebuilt the README around the requested assessment structure and removed the misleading conceptual class view.
- Matched method tables, file paths, error behavior, diagrams, test cases, and examples to the delivered source.
- Kept the expense menu, CSV schema, amount rules, category reporting, and script-relative data behavior.
- Enabled strict quoted-CSV parsing to reject malformed expense input.
- Organized attendance cleaning into reusable functions with constants and a direct-execution guard.
- Added attendance read/decoding/save error handling and temporary-file replacement.
- Preserved attendance's original current-working-directory behavior and name-cleaning semantics.
- Captured two expense sessions and two attendance executions; README transcripts use those exact captures.
- Kept generated CSVs, previews, verification materials, and PNG review renders out of the repository archive.

## 3. Validation Evidence

| Check | Result |
| --- | --- |
| Runtime | Python 3.12.14 |
| Expense scenarios | 41/41 passed |
| Attendance scenarios | 17/17 passed |
| Combined | 58/58 passed |
| Python syntax compilation | Both files passed |
| SVG XML parsing | All five passed |
| SVG raster rendering | Five PNGs generated and visually inspected |
| Diagram review | Text, canvas edges, connectors, and arrowheads checked; overlap fixed |
| README image and source links | All relative targets exist |
| Preview packaging | All five SVGs embedded; no external assets needed |
| HTML structural verification | Tables, headings, embedded images, and default themes checked |
| Browser visual inspection of HTML | Unavailable: browser policy rejected local-file navigation; no browser-rendered HTML result is claimed |

To reproduce the program checks, unpack the repository ZIP and verification support ZIP into the same parent folder:

```text
parent/
├── python-files-errors-assessment/
└── review/
    └── verify_submission.py
```

Then run:

```bash
python review/verify_submission.py
```

This test runner uses the standard library and isolated temporary folders. It never uses personal expense data. Raw results are in `review/evidence/test_results.json`; terminal captures and generated sample CSVs are beside it.

## 4. Assumptions and Departures

1. **Missing official brief:** Scope, file names, and repository name were taken from the attached README. Exact official compliance and grading weights remain unconfirmed.
2. **Author identity:** `YOUR NAME` and `YOUR_USERNAME` remain explicit placeholders. Replace them in the README and clone URL before uploading.
3. **Language:** Python was retained from the existing assessment and recovered source programs; application dependencies remain standard-library only.
4. **Extra folder:** `assets/` is the only added repository folder, as requested for SVGs.
5. **Extra support:** HTML previews and verification materials are outside the repository. They are optional review material, not required source submission files.
6. **No live GitHub publication:** This delivery prepares upload-ready repository files. No GitHub repository has been created or published.
7. **Existing implementation:** The matching source programs were recovered and improved. They are the user's existing assessment work; this delivery does not claim they were newly written from scratch.
8. **No brief-driven exceptions:** No supplied official brief required a departure; it was absent. The missing author/username and unavailable browser preview inspection are disclosed above.
9. **Visual background interpretation:** Every SVG has a solid white canvas; the banner places its requested gradient inside that white canvas.
10. **No grade guarantee:** Documentation quality and verified behavior do not establish a grade without the actual marking rubric.

## 5. Upload Checklist

- [ ] Replace `YOUR NAME` and every `YOUR_USERNAME`; compare this package with the original assessment brief if available.
- [ ] Create a GitHub repository named **python-files-errors-assessment**.
- [ ] Upload the contents of the matching folder: the four root files and the entire `assets/` folder.
- [ ] Commit with a message such as `Complete file handling assessment and verified documentation`.
- [ ] Make the repository public and confirm that its README images render.
- [ ] Copy the public repository URL and submit it on the LMS.
