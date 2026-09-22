# Beyond Sedona
An evidence-led screening tool for seasonal side trips from Sedona. MIT 1.125, PS01.

## Run
`python3 -m http.server 4173 --directory dist`
Open http://localhost:4173. No website build dependencies are required.

## Website and separate submission
`dist` contains only the story, source notes, styles, scripts, photograph and chart runtime JSON. The website header links to the Google Drive submission folder. The collected CSV dataset and the three PDFs are outside the published directory.

Upload these four files to Drive:
- output/beyond-sedona-dataset-and-sources.zip
- output/pdf/data-and-methodology.pdf
- output/pdf/five-minute-demonstration-plan.pdf
- output/pdf/short-reflection.pdf

The final presentation format (deck or recording) is pending instructor guidance. The demonstration PDF is a timed plan.

## Reproduce
Run `python3 scripts/prepare_data.py`, then `python3 scripts/build_documents.py`, then `python3 scripts/finish_deliverables.py`. The last script requires ReportLab. Processed CSVs are under research/processed; raw downloaded PDFs and extracted text are under research/raw. Several other sources were accessible through indexed text despite direct download failures. The source ZIP documents those limits. No missing source PDF is represented as a downloaded original.

## Interpretation
Park visits are not unique people or total town visitors. Relative quiet is not spare capacity. Spending areas overlap; do not add them into regional impacts. Receiving-community support and operating capacity require further research. No personal data or analytics are collected. NPS regional photograph: public domain; source on website.
