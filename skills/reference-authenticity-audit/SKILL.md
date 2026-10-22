---
name: reference-authenticity-audit
description: Verify whether scholarly references exist and whether their complete titles, authors, publication years, venues, and intended versions match. Use for bibliography authenticity checks, suspected invented references, or citation metadata verification. Requires two independent agents to start with Google Scholar; an unavailable agent or inaccessible source leaves the corresponding verification incomplete.
license: MIT
---

# Reference Authenticity Audit

Establish both whether the work exists and whether the supplied citation identifies it correctly. A real article with a wrong author or year is a metadata mismatch. An unsuccessful search does not prove fabrication. Bibliographic verification does not establish that a paper supports the manuscript's claim.

## Set the scope

Identify the supplied reference list, intended versions, and whether the task is audit or authorized correction. Preserve original entries and stable IDs. Do not rewrite manuscript prose during a reference audit. Search only the bibliographic information needed for the task, not private manuscript passages.

## Require two independent checks

The coordinating agent assigns **the same references to two distinct agents**, each with the original citation and intended version. Neither sees the other's findings or a suggested verdict before completing its own record. Splitting the list between two agents is not cross-verification. A second persona in one conversation is not a second agent. A verifier explicitly assigned a leaf role completes its own check without spawning further verifiers.

Each agent independently begins each reference on **Google Scholar**, preferably with its full title in quotes, then narrows or expands using author and year if necessary. It opens the matching record/version and records its actual search and inspected sources. It must check all four fields, including the complete title and author list, rather than accepting a truncated search snippet. Read [field decisions](references/field-decisions.md) for exact-match and version rules.

Use the article, publisher, official proceedings, or repository record to resolve truncated or conflicting Scholar metadata. This supplements the Scholar-first check; it does not silently replace it. If access is blocked, record the block and any independently supported primary-source findings. Do not bypass access controls, CAPTCHA, or bulk-access limits. If either agent or the required sources are unavailable, provide useful partial findings and explicitly leave dual verification incomplete. Never invent a second review, a search result, a timestamp, or a source visit.

Scholar's [official help](https://scholar.google.com/intl/en/scholar/help.html) explains citation exports, coverage limits, and automated metadata extraction. Index absence and extraction error are possible. Do not turn its search result or citation count into a quality or authenticity guarantee.

## Capture each agent's evidence

For every reference, record the original ID; exact query and observed source URLs; inspection time; intended work/version; observed full title, complete ordered authors, publication year, and venue; field matches or discrepancies; and source/access limitations. Use actually observed values. Mark unknown fields unknown. Preserve export or page evidence when permitted and useful, without bulk scraping.

Treat supplied snapshots as snapshot evidence. Identify who captured them and when if known. A synthetic fixture or replay can test decision rules but cannot be reported as a live Scholar verification. Two independent analyses of one capture are not two independent source retrievals.

## Reconcile without voting

Compare the two completed records field by field. Agreement is necessary for a clean dual-verification verdict but does not override conflicting primary evidence. Investigate differences in edition, version, online-first year, full author list, venue, and DOI. Retain both initial records and the resolution evidence; a third check may help but does not erase disagreement.

Use separate status dimensions rather than a vague pass:

| Dimension | Useful states |
| --- | --- |
| Existence | Supported by identified sources / unresolved |
| Citation fields | All required fields match / specific mismatch / incomplete |
| Version | Intended version matched / different version / unresolved |
| Process | Two independent Scholar-first checks completed / incomplete, with reason |

A reference is **fully verified under this workflow** only when both independent checks are complete and the required fields and intended version match with no unresolved evidence conflict. Correctable mismatches remain findings until the corrected entry has been checked. Do not label a work nonexistent solely because it was not found.

## Deliver a bounded record

Lead with the number and scope actually checked, then a concise table of consequential findings and kept entries. Attach the two source records and any reconciliation when a full audit is requested. Separate confirmed facts, proposed corrections, and unresolved facts. Keep exact title punctuation, spelling, technical terms, and required bibliographic formatting. The library's prose preferences do not authorize rewriting publication titles. Stop when the scoped references have explicit outcomes and actionable remaining checks.
