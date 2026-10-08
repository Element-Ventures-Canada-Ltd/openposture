Handling: Unclassified — public

# Export-control screen and purge procedure (v0.1)

This repository holds supply-chain mapping only. This screen keeps controlled technical data out, and sets out what maintainers do if something gets in. It is a screen, not legal advice; when in doubt, leave it out and ask a maintainer privately.

## 1. Screen (contributor and reviewer)

Answer each question before opening, and again before merging, a pull request. Any "yes" or "unsure" stops the contribution until a maintainer clears it.

| # | Question |
|---|---|
| 1 | Does it describe how a component is designed, made, processed, tested or how it performs (drawings, dimensions, tolerances, materials specifications, process parameters, test data, performance figures)? |
| 2 | Does it concern an item on Canada's Export Control List, the Controlled Goods List, the US ITAR / EAR, or a comparable allied list, beyond naming the item category? |
| 3 | Did the material come from anywhere other than a public, citable release (internal, contract, NDA, classified, Protected or "shared in confidence")? |
| 4 | Does it carry, or derive from material that carried, a security or proprietary marking? |
| 5 | Is the contributor, or the source, subject to an employer, institution or funder restriction on publication? |
| 6 | Does it name a person below officer or spokesperson level, or include personal contact details? |

Public availability elsewhere does not settle question 1 or 2.

## 2. Reviewer duties

- Run the screen on every pull request that adds or changes records, text describing components, or files under `data/`.
- Check each real record's citation opens and supports the record.
- Reject rather than edit when question 1 or 2 is "yes"; do not quote the material in the review.

## 3. Purge procedure (wrongly published material)

1. **Contain (same day).** A maintainer closes or locks the pull request or issue, hides affected comments, and reverts the change on `main` through a pull request. Do not discuss the content publicly.
2. **Report privately.** The reporter or maintainer notifies the lead maintainer through [SECURITY.md](SECURITY.md). Record date, files, commits and who had access.
3. **Assess (within 2 business days).** The lead maintainer, with counsel where needed, decides whether history must be rewritten and whether any authority or source owner must be notified.
4. **Rewrite history if required.** Remove the material from all branches and tags. The `cla-signatures` branch is excluded and preserved. Force-push is done only by the lead maintainer, outside the normal ruleset, and recorded.
5. **Remove cached copies.** Request GitHub Support to purge cached views and pull-request references; ask forks to delete affected commits.
6. **Record and close.** Log the incident privately: what, when, how found, actions, notifications. Update this screen if it missed something.
