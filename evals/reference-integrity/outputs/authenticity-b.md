# Independent reference-authenticity audit — verifier B

Three supplied entries were independently checked in this live public-source audit. They identify two supported works. R1 matches the publisher's 2001 journal record; R2 is best resolved as a duplicate of that work with an incorrect year; R3 matches the 2016 conference bibliographic record. **None receives the workflow's “fully verified” status here:** all three Google Scholar retrieval attempts were inaccessible through the web tool, and this is one leaf verifier's record, not a reconciled two-agent result.

Audit retrieval window: **2026-10-22, 16:49:09–16:50:33 UTC**, using clock-tool readings around the recorded retrieval batches. These are actual observation windows, not claimed source publication or crawl times. Only the assigned skill, its field-decision reference, and the supplied request were read locally. No other evaluation files, rubric, other verifier's output, or memory were consulted. No delegation occurred. The original entries and all inputs remain unchanged.

| ID | Existence | Citation fields | Intended version | Process / disposition |
| --- | --- | --- | --- | --- |
| R1 | Supported by an opened publisher record | All four supplied fields match | *Machine Learning* journal article, 2001, identified | Scholar unavailable; retain entry provisionally pending workflow completion |
| R2 | The matching work is supported; a separate 2002 publication was not established | Title, sole author, and journal match R1's identified work; **2002 conflicts with publisher's 2001** | The identified journal article is dated 2001; a distinct intended 2002 version remains unsupported | Scholar unavailable; flag the year and duplicate identity for correction/reconciliation |
| R3 | Supported by an opened institutional publication record and its retrieved BibTeX | Complete title, ordered authors, year, and conference identity match; exact expanded venue wording additionally appears in the search-indexed official CVF record | 2016 conference bibliographic identity matched; final IEEE proceedings PDF not inspected | Scholar unavailable; direct CVF access blocked and IEEE challenged access; retain entry with these process limits |

## Original entries preserved

- **R1.** Leo Breiman. Random Forests. Machine Learning. 2001.
- **R2.** Leo Breiman. Random Forests. Machine Learning. 2002.
- **R3.** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. Deep Residual Learning for Image Recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2016.

R1 and R2 were assessed separately before identity reconciliation within this verifier's record. Their supplied venue indicates a journal article. R3 explicitly intends the conference version.

## Scholar-first retrievals

Each reference's first lookup was its own Google Scholar URL. These three independent requests were submitted in one retrieval batch starting after the 16:49:09 UTC clock reading. No Scholar result page, record, author list, citation export, or version cluster was returned. The tool reported “not accessible via this tool” for each URL. This does **not** establish a CAPTCHA, an absent index record, or a fabricated work; the precise reason for the tool's inability to access Scholar is unknown.

| ID | Exact decoded Scholar query | Requested URL | Observed result |
| --- | --- | --- | --- |
| R1 | `"Random Forests" "Leo Breiman" 2001` | [Scholar R1 query](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22+2001) | Inaccessible via tool; no record inspected |
| R2 | `"Random Forests" "Leo Breiman" 2002` | [Scholar R2 query](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22+2002) | Inaccessible via tool; no record inspected |
| R3 | `"Deep Residual Learning for Image Recognition" 2016` | [Scholar R3 query](https://scholar.google.com/scholar?q=%22Deep+Residual+Learning+for+Image+Recognition%22+2016) | Inaccessible via tool; no record inspected |

The first subsequent general-web search batch completed by **16:49:18 UTC**. General-web results supplement these failed attempts; they are not represented as Google Scholar verification. No access control or robot challenge was bypassed.

## R1 and R2 — journal identity and year

### Actually inspected primary evidence

The [Springer article landing page](https://link.springer.com/article/10.1023/A:1010933404324) was successfully opened during **16:49:29–16:49:42 UTC**. Its complete bibliographic header, author information, and citation/issue-date sections were inspected, not merely a truncated search snippet. The following values were displayed:

| Field | Observed publisher value | R1 comparison | R2 comparison |
| --- | --- | --- | --- |
| Complete title | Random Forests | Exact match | Exact match |
| Complete ordered author list | Leo Breiman — one author; also confirmed in the page's author-information section | Exact match | Exact match |
| Publication year | 2001; both publication and issue information specify October 2001 | Match | **Mismatch: supplied 2002** |
| Venue | Machine Learning | Exact match | Exact match |
| Additional identity fields | Volume 45, pages 5–32; DOI `10.1023/A:1010933404324` | Disambiguating evidence; not originally supplied | Same identified work as R1 |

The publisher date evidence contains no observed online-first/issue-year split that would justify replacing 2001 with 2002. The article's existence and complete supplied fields can be checked from this public landing page even though its full text is subscription content. I did not purchase, log in to obtain, or inspect the publisher PDF.

### Identity decision and proposed correction

R1 should be retained as the supplied journal citation. R2 should be treated as a **duplicate candidate for the same identified journal work with a wrong year**, not as evidence of a second publication. The field combination resolves to the same publisher record and DOI. No separate 2002 *Machine Learning* article with these supplied fields was established in the searches performed. This is a bounded identification judgment, not an exhaustive claim that no similarly named work or version exists anywhere.

Proposed correction for R2: change the year to **2001**, then reconcile/deduplicate it against R1 while preserving any citation-key relationships. The audit did not change or delete either entry. If the draft author intended a distinct 2002 item, they need to provide its DOI or primary record; changing the date alone cannot establish that different intention. A corrected database entry has not been created or checked in this audit.

### R1/R2 search and access record

After the Scholar attempts, these exact general-web searches were issued in the batch completed by **16:49:18 UTC**:

- `"Random Forests" "Leo Breiman" "2001" Machine Learning`
- `"Random Forests" "Leo Breiman" "2002" Machine Learning`

The search output exposed a Springer result carrying the 2001 article metadata. It also exposed a Berkeley random-forests page mentioning July 2002 lecture materials, among other results. Such mentions were not assumed to be the journal article's publication year.

| Requested or returned URL | Actual access outcome / use |
| --- | --- |
| [DOI route](https://doi.org/10.1023/A:1010933404324) | During 16:49:18–16:49:29 UTC, retrieval failed with a 500/tool error after redirecting to `https://link.springer.com/10.1023/A:1010933404324`. No page contents obtained through this route. |
| [Lowercase DOI search-result URL](https://doi.org/10.1023/a%3A1010933404324) | Followed during 16:49:29–16:49:42 UTC; the same failed redirect was reported. This was not counted as a successful publisher visit. |
| [Canonical Springer article route](https://link.springer.com/article/10.1023/A:1010933404324) | Successfully returned the full public metadata page during 16:49:29–16:49:42 UTC; decisive evidence above. |
| [Berkeley random-forests papers page](https://statgrades.berkeley.edu/~breiman/RandomForests/reg_papers.htm) | Search-indexed text was returned, but direct opening during 16:49:18–16:49:29 UTC timed out. Its linked reports/lectures were not opened and do not verify any 2002 journal version. |

Other search hits, including secondary indexes and mirrored PDFs, were not opened or relied on as complete-field evidence. Search result dates such as “published ... years ago” were not used as bibliographic publication dates.

## R3 — conference record and preprint distinction

### Actually inspected primary evidence

The [Microsoft Research publication record](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/) was successfully opened during **16:50:07–16:50:14 UTC**. It displayed the complete title, all four authors in order, June 2016, a conference name, and IEEE as publisher. The linked [institutional BibTeX export](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/bibtex/) could not be parsed by the web tool because its content type was `application/x-bibtex`; an ordinary public `curl --fail --location --max-time 20 --silent --show-error` request then successfully retrieved that same export during **16:50:20–16:50:33 UTC**. This fallback addressed the parser's unsupported file type; it did not bypass authentication or a robot challenge.

| Field | Observed source value | Decision |
| --- | --- | --- |
| Complete title | Deep Residual Learning for Image Recognition | Exact match in opened institutional record and retrieved export |
| Complete ordered author list | Kaiming He; Xiangyu Zhang; Shaoqing Ren; Jian Sun | All four names and their order match in record and export |
| Year | 2016; month June | Matches intended conference year |
| Venue | Institutional export: `2016 Computer Vision and Pattern Recognition`; entry type `@inproceedings`; publisher `IEEE` | Matches the identified conference; the expanded proceedings wording supplied in R3 is also present in official CVF search-indexed metadata |
| Additional fields | Institutional export pages `770-778` | Consistent conference record; not required by original entry |

The [official CVF article record as surfaced by web search](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html?_hsmi=2) supplied an untruncated metadata block with the same title and four ordered authors, the supplied expanded venue, 2016, pages 770–778, and its own conference BibTeX. Direct opening failed, so I distinguish that **search-indexed official-source evidence** from the successfully opened Microsoft record. I do not claim a successful direct CVF page inspection.

The [conference DOI](https://doi.org/10.1109/CVPR.2016.90) resolved to [IEEE Xplore document 7780459](https://ieeexplore.ieee.org/document/7780459/). That destination returned a JavaScript/robot-verification page rather than article metadata. The redirect was observed, but the IEEE full record and final published PDF were not inspected.

### Version distinction actually observed

Clicking the PDF link on the Microsoft record successfully opened [its hosted PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/07/Deep-Residual-Learning-for-Image-Recognition.pdf) during **16:50:14–16:50:20 UTC**. The returned PDF text identifies the same complete title and four authors on its first page, but it also explicitly identifies **arXiv:1512.03385v1, 10 Dec 2015**. Thus this hosted PDF is preprint-version evidence; it is not proof that I inspected the 2016 final proceedings PDF. The URL's `2021/07` directory was not interpreted as a publication year.

R3's intended **conference bibliographic identity** is supported by the opened publication record and export, with indexed CVF corroboration. The linked 2015 preprint does not create a year mismatch for this explicitly conference-version citation, and I do not propose changing R3 to 2015. No claim is made that the preprint and conference texts are identical.

### R3 search and access record

Exact general-web queries, after the initial Scholar attempt:

| Observation window, UTC | Exact queries |
| --- | --- |
| By 16:49:18 | `"Deep Residual Learning for Image Recognition" "2016" site:openaccess.thecvf.com` |
| 16:49:42–16:49:50 | `"Deep Residual Learning for Image Recognition" site:ieeexplore.ieee.org/document`; `"Deep Residual Learning for Image Recognition" site:openaccess.thecvf.com/content_cvpr_2016/papers` |
| 16:49:57–16:50:07 | `"Deep Residual Learning for Image Recognition" site:microsoft.com/en-us/research/publication`; `"Deep Residual Learning for Image Recognition" "7780459"`; `"Deep Residual Learning for Image Recognition" "10.1109"` |

The batched search outputs do not expose an exhaustive per-query hit list. Their absence of a usable IEEE result was not treated as absence of a publication. The following actual direct accesses were attempted:

| URL | Observed result and time window, UTC |
| --- | --- |
| [CVF article, clean URL](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) | 403 Forbidden, 16:49:18–16:49:29 |
| [CVF article, returned search-result URL](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html?_hsmi=2) | 403 Forbidden, 16:49:29–16:49:42 |
| [CVF 2016 proceedings index](https://openaccess.thecvf.com/CVPR2016.py) | Direct opening returned 403 Forbidden, 16:49:42–16:49:50. Search-indexed text did expose this paper's complete conference metadata, separately from that failed direct opening. |
| [CVF conference PDF](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) | Search result discovered the PDF; direct opening returned 403 Forbidden, 16:49:50–16:49:57. No successful PDF inspection through this URL. |
| [Microsoft publication page](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/) | Successfully opened, 16:50:07–16:50:14 |
| [IEEE document](https://ieeexplore.ieee.org/document/7780459) | Robot-verification page requiring JavaScript, 16:50:07–16:50:14; no article metadata obtained |
| [Conference DOI](https://doi.org/10.1109/CVPR.2016.90) | Redirected to IEEE document with trailing slash and returned the same challenge, 16:50:07–16:50:14 |
| [Microsoft BibTeX](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/bibtex/) | Web-tool unsupported-content-type error, 16:50:14–16:50:20; ordinary public curl retrieval succeeded, 16:50:20–16:50:33 |
| [Microsoft-hosted PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/07/Deep-Residual-Learning-for-Image-Recognition.pdf) | Successfully opened PDF text, including first-page authors and the 2015 arXiv v1 stamp, 16:50:14–16:50:20 |

Secondary results were discovery aids only. No Wikipedia, citation counts, or third-party citation statements were used to establish the four required fields.

## Remaining checks and audit boundary

1. The coordinator must compare this independent record with the other verifier's completed record. I have not seen or assumed its findings. Agreement cannot by itself cure missing Scholar access.
2. Obtain accessible Scholar results for each entry if the audit must satisfy the skill's full two-independent-Scholar-first workflow. In the present record those checks remain incomplete, despite useful primary-source findings.
3. Resolve R2's erroneous date and duplicate identity in the reference database only under a correction task, then check the corrected entry. Preserve the original IDs and citation-key relationships during that work.
4. If direct inspection of R3's final proceedings artifact is required beyond bibliographic identity, retrieve it legitimately from CVF or IEEE when accessible. The Microsoft-linked preprint must remain labeled as such.

This report verifies bibliographic identity and records limitations. It does not evaluate scientific quality, reproduction of results, or whether either work supports an unspecified manuscript claim. No unsuccessful search is treated as proof of fabrication.
