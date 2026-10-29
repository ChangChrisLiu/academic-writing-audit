# Contributing

Propose improvements around an observed editorial failure, not a preference for longer instructions.

1. Supply a short fictional or openly shareable passage and its relevant evidence.
2. Describe the user's requested scope and the agent's actual response.
3. Explain the scientific or reader-facing consequence of the behavior.
4. Propose the smallest change to the skill that addresses it.
5. Re-run the relevant fixture and inspect the full response for regressions.

Keep the core skill portable. Avoid mandatory model brands, provider-specific tools, universal section orders, fixed word quotas, and unnecessary mandatory multi-agent workflows. The reference-authenticity workflow requires two independent agents and Google Scholar-first checks. Idea-led research preparation also requires independent overlapping investigation followed by reciprocal review, within the permitted sources. Preserve these scoped contracts and report capability limits honestly; ordinary local edits do not trigger either workflow. Put conditional depth in the relevant reference and keep its link discoverable from `SKILL.md`.

For behavior changes, include a no-guidance control when practical. Distinguish observed results from an expected outcome. A small number of synthetic trials is useful regression evidence, not proof of general effectiveness. A no-change decision can be a passing result.

Role guidance must name the decision and evidence appropriate to the study design, not merely announce an expert persona. Revision tests should include both harmful losses and changes that ought to be accepted, such as concise equivalent wording or a correction to an unsupported old claim. Freeze inputs before execution, retain full outputs and disagreements, and pin historical skill versions before changing previously tested files.

Distinguish behavioral report assessments from operational tests. Reference-workflow operation claims need reviewable source captures, export files, source diffs, build artifacts, or observed native citation-field refreshes as appropriate. Static reports, cached field text, and package inspection do not alone establish those operations succeeded. Preserve failures and partial coverage.

Keep descriptions and installation guidance consistent with the current format. Check frontmatter, relative links, and standalone packaging. Do not copy proprietary prompts, manuscripts, correspondence, logs, credentials, or personal filesystem paths into an issue or pull request. Use authorized, minimal source excerpts or fictional examples.

## Keep responsibilities and shared guidance clear

Place a rule with the skill that owns the decision. The full audit routes consequential findings; drafting develops the manuscript; prose editing repairs expression; revision integrity compares versions; response writing addresses reviewers. Keep these responsibilities distinct rather than giving every skill the complete workflow. Use the [documentation index](docs/README.md) for user-facing task guidance.

Repeated prose conventions and the reference ledger have canonical sources under [shared/](shared/manifest.json). Their declared copies remain inside each skill so a selected skill can be installed independently. Edit the canonical source, then run:

```sh
python3 scripts/sync_shared.py
python3 scripts/sync_shared.py --check
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Do not hand-edit declared copies or make a skill depend on a sibling skill or the repository-level shared directory. A shared-source change affects every declared consumer, so review its fit for each responsibility. Keep skill-specific exceptions in the relevant entrypoint or reference.

The validator uses Python 3.9+ and the standard library. It checks the repository's simple scalar frontmatter and UI metadata, license copies, local file links, common Markdown heading anchors in active documentation, standalone dependencies, shared-copy equality, historical manifest hashes and Git whitespace checks. It is not a general YAML or Markdown parser. Use a full Git clone containing the recorded historical commits; an exported source ZIP cannot complete the Git checks. An optional `--installed-dir /path/to/skills` compares complete installed folders without writing them. These structural checks do not establish behavioral effectiveness.

After validation and committing the intended files, build a release from the clean Git tree with `python3 scripts/package_release.py --tag v0.9.0 --output-dir ../releases/v0.9.0`, substituting the intended version and a new destination. The command validates again, packages the committed repository and complete standalone skills, verifies archive bytes and modes, and writes media assets and checksums. It refuses an existing destination and does not push, tag or publish. Review the resulting files before the separately authorized publication step.

## Preserve historical evidence

Treat existing trial requests, rubrics, freezes, outputs, assessments, artifact files and record READMEs as historical evidence. Do not shorten, reformat or overwrite them during documentation maintenance, including whitespace that is protected by `.gitattributes`. Add new trials or explanatory records separately and link them through the [evaluation index](evals/index.md).

Before editing a skill referenced by a live historical manifest, pin the existing tested bytes to their already-recorded Git revision and document that resolution change. Preserve the expected hashes. Do not recalculate historical hashes to make revised instructions appear previously tested. A commit-resolved hash check verifies that historical version; it does not detect every change to the current copy, so compare the existing evidence files before and after a maintenance change as well.

Contributions are distributed under this repository's MIT license.
