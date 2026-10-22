---
name: word-citation-audit
description: Audit Word manuscript citations and the reference list in both directions after identifying the required style. Use for missing or unused references, ambiguous author-year matches, numbering errors, bibliography duplicates, and citation-manager field preservation. Distinguish formatting, mapping, and authenticity verification.
license: MIT
---

# Word Citation Audit

First establish the required citation format. Then check both **citation → reference** and **reference → citation**, preserving the intended work and any live citation fields.

## Identify style and document state

Read supplied author/venue instructions and the selected citation-manager or Word style. Record the exact style and version when available, plus whether references are live fields or plain text. A parenthesized author and year does not uniquely establish APA; superscript numbers do not uniquely establish Vancouver. When evidence conflicts, report the required and currently configured styles separately. If the exact style remains unknown, continue identity and coverage checks that do not depend on it, while leaving style-specific judgments pending.

Establish the intended revision view and scope. Tracked insertions and deletions must not silently become one combined citation inventory. Do not accept changes, refresh fields, or alter the file during an audit-only task. A PDF or text export may support visible checks but cannot establish native field integrity or coverage of omitted document regions.

Use the [reference ledger](references/reference-ledger.md) to reuse identity evidence and connect occurrence locations to original entries. Preserve suspected duplicates as candidates until resolved. Style-only changes do not require repeating unchanged authenticity checks.

## Build two traceable inventories

Read [matching and coverage](references/matching-and-coverage.md). Inventory every citation occurrence with its location and visible form or field identity. Include the relevant body, captions, tables, text boxes, notes, and appendices, according to the manuscript and style. Mark inaccessible regions as unchecked. Do not treat every number, bracket, footnote marker, or cross-reference as a bibliographic citation.

Inventory each reference-list entry with a stable ID, displayed label, full bibliographic identity, and manager ID when available. Distinguish the main cited reference list from explicitly permitted further reading or a broader bibliography. Record duplicate works and ambiguous labels rather than hiding them by normalizing everything to a single title.

## Match in both directions

For each citation, resolve the intended reference or report missing, ambiguous, or wrong-target status. Expand numeric ranges and grouped citations; check narrative and parenthetical author-year citations, corporate authors, initials, `et al.`, and year suffixes using the identified style. A numerical label existing in the list is not sufficient when the field or context identifies another work. Do not infer a source's content solely from its title.

For each listed reference, locate its citation occurrences. Report entries with no observed citation, explicitly qualified by the inspected scope. Check notes, captions, tables, and appendices before calling an entry uncited. A bibliography or further-reading convention can permit uncited entries; identify these separately rather than deleting them. When the whole document is not available, use “not found in inspected portions,” not “unused throughout.”

Separate identity/mapping errors from style errors. For example, a uniquely identifiable author-year work can be mapped even when its required author abbreviation is wrong. Similar names and missing year suffixes can instead leave the target unresolved. Do not invent a match to make the reference counts agree.

## Keep authenticity and claim support separate

A correctly linked and formatted citation can still identify a nonexistent or misdescribed work. If authenticity is in scope, use two distinct agents to check the same references independently, each beginning on Google Scholar and corroborating the complete title, ordered authors, publication year, venue, and intended version against primary publication evidence before seeing the other's verdict. Require that corroboration even when Scholar looks complete; record shared primary-source dependence if both agents use the same record. If a retrieval tool fails, try an already available, authorized ordinary browser route when feasible. Distinguish tool failure, site restriction, and no matching result; do not bypass challenges or retry in loops. Leaf verifiers do not delegate recursively. Reuse a completed source-linked report for unchanged identities/versions; reopen affected checks when metadata, version, or new conflicting evidence changes. Inaccessible sources or unavailable independent agents leave this check incomplete. Do not call missing search results proof of fabrication. Reconcile conflicts with source evidence rather than voting.

For a mapping-only audit, clearly state that live authenticity was not checked. Whether the cited paper supports the sentence is a separate content audit requiring the paper and the specific proposition; neither reference-list matching nor a real DOI proves it.

## Repair without breaking fields

Edit only within the user's authorized scope. For Zotero, EndNote, Mendeley, or native Word fields, repair through the relevant citation source or manager when available, then refresh and inspect the affected citations and bibliography. Do not replace field results with plain text, strip fields, manually renumber generated labels, or silently accept tracked changes. If safe field-aware editing is unavailable, provide the exact proposed corrections without flattening the document.

After edits or field refresh, recheck numbering, ordering, year-letter suffixes, duplicate entries, and both mapping directions. Retain a before/after record of field identities and source relationships, plus observed refresh outcomes. Record native refresh, save, and reopen verification separately. An update command returning success does not establish that the changes were saved. Verify the saved copy's field instructions, source identities, and displayed mappings after reopening when feasible; leave persistence unconfirmed if the saved artifact cannot be inspected. Inspect affected rendered pages if layout is part of the task. Package/XML inspection establishes structure only; cached display text is not a successful citation-manager refresh. Rendering in another office engine is not proof that Word or a particular reference-manager integration refreshed correctly. Keep exact publication titles, names, punctuation, and style conventions even where ordinary prose would be simplified.

## Deliver a bounded audit

State the required/current/unknown style, document view, inspected regions, and field visibility. Summarize counts only when their units and coverage are clear. Report missing targets, ambiguous matches, wrong targets, duplicate records, and uncited-list candidates with locations, evidence, and the smallest justified action. Include sound entries and any legitimate uncited bibliography items. Distinguish proposed corrections from applied changes and visible-text checks from native-field or rendered checks.
