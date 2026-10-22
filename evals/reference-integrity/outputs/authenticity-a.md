# Independent reference-authenticity audit — verifier A

Three original references were checked using live public-source retrievals on **2026-10-22, 16:49:07–16:50:27 UTC**. This is one independently assigned leaf record. I did not delegate, inspect the other verifier's findings, inspect evaluation rubrics or prior outputs, or alter the supplied references. I read only the assigned skill, its field-decisions reference, and the supplied request before searching.

**Result:** R1's supplied fields match the identified journal article. R2 resolves to the same identified work, with a year mismatch against its journal publication record; it is not supported as a second publication. R3's supplied fields match the intended 2016 conference publication. **None is fully verified under the prescribed dual Scholar-first workflow:** all three initial Google Scholar accesses failed, and this report establishes only this verifier's findings. No claim-support audit was performed.

## Preserved inputs and outcomes

| ID | Original reference, unchanged | Existence | Citation fields | Version / identity |
|---|---|---|---|---|
| R1 | Leo Breiman. Random Forests. Machine Learning. 2001. | Supported by publisher and DOI registry | All four required fields match | Identified journal article, DOI 10.1023/A:1010933404324 |
| R2 | Leo Breiman. Random Forests. Machine Learning. 2002. | The identified work exists | Title, complete authors, and venue match; **2002 conflicts with the journal publication year 2001** | Same identified journal article as R1; no separate 2002 publication established |
| R3 | Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. Deep Residual Learning for Image Recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2016. | Supported by institutional publication record, conference-indexed record, and DOI registry | All four required fields match | Intended conference version identified, DOI 10.1109/CVPR.2016.90 |

## Scholar-first record

Each reference began with its own Google Scholar URL. The three requests were submitted together, before any fallback bibliographic searches. At 16:49:07 UTC the browsing tool reported each URL “not accessible via this tool.” It supplied no search-result records. This is a tool-access failure, not proof of a Scholar CAPTCHA, an empty result set, or absence from Scholar. No Scholar record, author expansion, citation export, or version list was inspected.

| ID | Exact query | Attempted URL |
|---|---|---|
| R1 | `"Random Forests" "Leo Breiman" 2001` | https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22+2001 |
| R2 | `"Random Forests" "Leo Breiman" 2002` | https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22+2002 |
| R3 | `"Deep Residual Learning for Image Recognition"` | https://scholar.google.com/scholar?q=%22Deep+Residual+Learning+for+Image+Recognition%22 |

## R1 and R2: observed fields and date resolution

The full [Springer article landing page](https://link.springer.com/article/10.1023/A:1010933404324), opened at 16:49:21 UTC, identifies the complete title as **Random Forests**, its sole author as **Leo Breiman**, and its journal as **Machine Learning**. Its publication and issue dates are October 2001, volume 45, pages 5–32. The page's author-information section independently lists the single author. The public metadata was accessible; the article body was subscription content, and I did not obtain its publisher PDF.

A direct HTTPS request to the [Crossref work record](https://api.crossref.org/works/10.1023%2FA%3A1010933404324) returned HTTP 200 at **16:50:09.785791 UTC**. The browsing tool had previously rejected this API URL as inaccessible; the ordinary public API request succeeded without authentication or bypassing an access control. Selected observed fields:

```json
{
  "DOI": "10.1023/a:1010933404324",
  "title": ["Random Forests"],
  "author": [{"given": "Leo", "family": "Breiman"}],
  "container-title": ["Machine Learning"],
  "type": "journal-article",
  "volume": "45",
  "issue": "1",
  "page": "5-32",
  "published": {"date-parts": [[2001, 10]]},
  "published-print": {"date-parts": [[2001, 10]]},
  "published-online": null,
  "issued": {"date-parts": [[2001, 10]]},
  "created": {"date-time": "2002-12-22T23:10:54Z"}
}
```

The `created` date belongs to the registry record and does not establish a 2002 publication. Crossref supplied no separate online-publication date. I therefore do not infer an online-first date.

The fallback search also returned an indexed [MaRDI record](https://portal.mardi4nfdi.de/wiki/Random_forests) saying “8 January 2002” and giving **the same DOI**. Direct opening timed out at 16:49:54 UTC. This is an observed secondary metadata conflict, not an independently verified 2002 edition. Its January date also differs from Crossref's December creation date, so I cannot explain its provenance by equating those dates. The publisher's explicit journal issue/citation date and the registry publication fields agree on 2001 and resolve the appropriate year for the supplied journal citation.

An [author-hosted Berkeley PDF](https://www.stat.berkeley.edu/users/breiman/randomforests-rev.pdf), opened and parsed at 16:49:54 UTC, displays **RANDOM FORESTS**, **Leo Breiman**, and **September 1999** on its first page. This is an earlier manuscript; its date does not replace the journal publication date. I did not establish its exact revision history or text identity with the final article. Its existence is not evidence for a separate 2002 journal publication.

**Decision:** Keep R1's four supplied fields. Flag R2 for correction to 2001 and duplicate reconciliation with R1. The identity conclusion is an inference from the identical title, sole author, venue, and the identified DOI, reinforced by the secondary 2002 record pointing to that same DOI. The supplied entries themselves contain no DOI, so this report does not prove what an author privately intended by R2. If a distinct 2002 work was intended, its unique identifier or source is still needed. No failure to find a separate work is being treated as proof that such a work cannot exist.

Proposed canonical entry, audit suggestion only: **Leo Breiman. Random Forests. Machine Learning 45(1), 5–32. 2001. DOI: 10.1023/A:1010933404324.** No database entries were changed or deleted.

## R3: conference-version record

The full [Microsoft Research publication page](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/), opened at 16:50:10 UTC, supplies the complete title and ordered author list: **Deep Residual Learning for Image Recognition**; **Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun**. It specifies June 2016, Computer Vision and Pattern Recognition, and IEEE. The separately opened [Microsoft CVPR 2016 accepted-papers page](https://www.microsoft.com/en-us/research/event/cvpr-2016/accepted-papers/) also lists this title and the four authors in that order.

The publication page's DOI link was followed at 16:50:15 UTC: https://dx.doi.org/10.1109/CVPR.2016.90 redirected to https://ieeexplore.ieee.org/document/7780459/. IEEE returned a JavaScript/robot-verification page, so I did not inspect its bibliographic record or PDF and did not try to bypass the check.

A direct request to the [Crossref conference record](https://api.crossref.org/works/10.1109%2FCVPR.2016.90) returned HTTP 200 at **16:50:27.094816 UTC**. It confirms the complete title and all four authors in the supplied order; `type = proceedings-article`; `publisher = IEEE`; `container-title = 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)`; pages 770–778; and publication/print/issued date June 2016. The DOI is `10.1109/cvpr.2016.90`.

The [Microsoft BibTeX export](https://www.microsoft.com/en-us/research/publication/deep-residual-learning-for-image-recognition/bibtex/) was actually retrieved by direct HTTPS, HTTP 200, at **16:50:27.480203 UTC**, after the browsing tool reported unsupported `application/x-bibtex` content. Its entry type is `@inproceedings`, with the same ordered author list, complete title, 2016 year, June month, IEEE publisher, and pages 770–778.

The search tool returned an indexed [CVF conference record](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html?_hsmi=2) containing the complete four-author list and BibTeX, with the exact venue wording supplied in R3. Direct retrieval of the [canonical CVF page](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html), [CVF PDF](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf), and [2016 index](https://openaccess.thecvf.com/CVPR2016.py) returned HTTP 403 at 16:49:21–16:49:34 UTC. I inspected the search service's indexed content, not a successfully fetched live CVF page or PDF. The differing full venue form in Crossref and the supplied “Proceedings of …” form identify the same conference, supported by CVF's indexed official citation and the directly retrieved institutional/registry records.

A Microsoft-hosted PDF search result displayed an arXiv v1 date of 10 December 2015: https://www.microsoft.com/en-us/research/wp-content/uploads/2021/07/Deep-Residual-Learning-for-Image-Recognition.pdf. I did not directly open that PDF and did not use its preprint date to replace the conference year. The identified 2016 proceedings metadata establishes the intended version; the inaccessible conference PDF's contents were not checked.

**Decision:** Keep R3 as supplied. Optional enrichment is pages 770–778 and DOI 10.1109/CVPR.2016.90. Required-field and conference-version findings are supported; Scholar verification remains incomplete.

## Fallback search log

These were web search-engine requests, **not Google Scholar results**. Times are UTC clock readings immediately following each returned batch. Domain filters are recorded separately from the literal query text. Unrelated results and secondary citations were not treated as authority for the bibliographic decisions.

| Time | Exact query | Domain filter |
|---|---|---|
| 16:49:14 | `"Random Forests" "Leo Breiman" "2001" Machine Learning` | link.springer.com |
| 16:49:14 | `"Random Forests" "Leo Breiman" "2002" Machine Learning` | link.springer.com |
| 16:49:14 | `"Deep Residual Learning for Image Recognition" CVPR 2016` | openaccess.thecvf.com |
| 16:49:34 | `"Deep Residual Learning for Image Recognition" "2016" "Kaiming He"` | ieeexplore.ieee.org; computer.org |
| 16:49:34 | `"Random Forests" "Breiman" "2002" "Machine Learning"` | none |
| 16:49:34 | `"Random Forests" "Leo Breiman"` | stat.berkeley.edu |
| 16:49:54 | `"Deep Residual Learning for Image Recognition"` | microsoft.com |
| 16:49:54 | `"10.1023/A:1010933404324" "2002"` | none |

## Remaining checks and limits

- The coordinator must compare this record against the independently obtained second record. I make no assertion about whether the second verifier succeeded or agreed.
- Successful Google Scholar record inspection remains outstanding for all three entries. Primary-source supplementation does not complete that requirement.
- R2's correction and any duplicate merge remain proposed actions. No corrected database entry was supplied for a subsequent check.
- No exhaustive search, full-text comparison, claim-support assessment, or retraction-status audit was performed. Absence of a retraction notice in the inspected metadata is not a verified publication-status assessment.
- This report contains actual live retrieval observations and clearly identified search-index evidence; it is not a replay or synthetic fixture. No Scholar visit, source success, or second-agent verification is invented.
