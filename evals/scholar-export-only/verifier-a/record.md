# Verifier A — Random Forests

One reference checked on 2026-11-05, 19:19–19:20 CST (2026-11-06, 01:19–01:20 UTC). The input identifies Leo Breiman's 2001 journal article in *Machine Learning*.

| Evidence | Independently inspected result |
| --- | --- |
| Scholar search | Query `"Random Forests" "Breiman" 2001`. The web reader could not open the search URL. Normal Chrome opened the [same query](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Breiman%22+2001) and displayed the journal result, `Random forests`, L Breiman, *Machine learning*, 2001, linked to Springer. |
| Export route | Clicked **Cite** on that result. The dialog identified Leo Breiman and offered **BibTeX**. Clicked the offered link, which opened `scholar.googleusercontent.com/scholar.bib` for result `eCpzaUc5Hg0J`. The rendered response body provided the entry in [export.bib](export.bib), including its indentation and terminal LF. Exported key `breiman2001random`, 195 bytes, SHA-256 `fd274f1b0c5702ad441dd136a83e82cbc68c964b453007acfa8e130197841cd3`. |
| Primary record | Opened the [Springer journal article](https://link.springer.com/article/10.1023/a:1010933404324) identified on Scholar. The page heading gives “Random Forests,” its sole author is Leo Breiman, and the journal is *Machine Learning*. The issue date is October 2001, volume 45, pages 5–32, DOI `10.1023/A:1010933404324`. |

The full title, sole author, year, venue and intended journal version agree across the records, allowing for Scholar's capitalization of “forests” and “learning.” The actual export was retained. No pre-existing working BibTeX entry was supplied for an equality check.
