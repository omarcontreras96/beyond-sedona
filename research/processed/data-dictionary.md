# Beyond Sedona: dataset dictionary
Collected 2026-09-22 UTC. Public aggregate research only. No personal records.

## park-visitation.csv (144 records)
park_id: stable key; park/community: named park and associated community (not the geography of a total visitor census); year/month: calendar period; visits: reported count of park visits, not unique people; unit: park visits; status: reported or not yet open; source_url: original report; retrieved_utc: research date. January 2024 Rockin River Ranch is zero in the source and flagged not yet open. Heatmap displays a dash. Monthly totals match annual totals. The 2025 source was accessed as indexed text because its direct download returned 404. The 2024 file was downloaded and text-extracted.

## visitor-spending.csv (54 records)
park_id/park: attraction associated with the spending; year: 2025; category: one of eight expenditure categories or Published direct total; value_usd: nominal dollars, rounded by source; geography: within 50 miles of park; population: non-local visitors from over 50 miles away; source_table: Table 35 or 44 of University of Arizona report. These overlapping areas are not town boundaries. Category sums can differ slightly from published totals due to rounding. Do not sum Published direct total alongside its categories. No park totals are added into a regional forecast. The report's multi-park survey includes 10,693 responses, 8,600 with usable expenditure data; park-level uncertainty is not estimated here.

## resident-feedback.csv (3 records)
Weighted 2024 City of Sedona probability sample. response: preferred tourism role in economy; percent: weighted percent; overall_sample_n: 551 respondents to survey overall, NOT the item denominator; item_sample_n: not separately reported; overall_response_rate_pct: 20; overall_margin_error_pp: 4 at 95% confidence. Separate open-participation data excluded. No inference to receiving communities. Nonresponse and coverage bias remain.

## hotel-context.csv (6 records)
study_area: STR's Sedona+ or Village of Oak Creek+ market; year/month: August-October 2025; occupancy_pct: rooms sold / rooms available x 100; adr_usd: average daily room rate in dollars, rounded in source; source_page: PDF page 4. Not destination-town availability. The source's current hotel table is used rather than older narrative text embedded in its PDF. A June renovation closure reduced Sedona+ supply. No short-term rental metrics included. The report's April 2025 sample note lists 21/44 Sedona+ hotels and 6/14 Village of Oak Creek+ hotels reporting.

## destinations.csv (6 records)
Park names, associated communities, reference/candidate role, experience, official links, published current hours where verified, and explicit missingness. Hours were checked in September 2026; these are not 2024/25 operating-day histories. Driving times, capacity and receiving-community attitudes are unverified, never encoded as zero.

## Derived values
Peak-relative index = 100 * monthly visits / maximum monthly visits for that park-year.
Annual share = 100 * monthly visits / sum of 12 monthly visits.
YOY percent = 100 * (2025 total / 2024 total - 1).
Summer = June-August. No statistical significance is claimed for count changes.
Five-park combined change excludes Rockin River Ranch because it opened February 2024.
Recommendations are qualitative screening judgments with explicit prerequisites; not an optimized score.

## Scope and reproducibility
Two years cannot establish long-term trends. Counts are not normalized for opening days, weather or closures. Park visits may include local users and repeated visits. Detailed collection and source notes are on methods.html; the source repository includes scripts/prepare_data.py and the 2024 extracted source. The 2025 transcribed fixture is in that script. Run python3 scripts/prepare_data.py to regenerate quantitative CSVs. scripts/build_documents.py writes destination data and methodology content. No runtime API key or third-party analytics is used.
