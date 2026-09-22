# Beyond Sedona
An evidence-led screening tool for seasonal side trips from Sedona. MIT 1.125, PS01.

## Run
`python3 -m http.server 4173 --directory dist`
Open http://localhost:4173. No build step or dependencies are needed for the website.

## Evidence and deliverables
The `dist` directory is the complete publishable site. Its `data` directory includes six CSV files, a dictionary, a ZIP dataset, methodology PDF, reflection draft and presentation notes. `methods.html` documents original sources, dates, units and caveats. `submission.html` maps assignment requirements to artifacts.

## Reproduce
Run `python3 scripts/prepare_data.py`, then `python3 scripts/build_documents.py`, then `python3 scripts/finish_deliverables.py`. The last script requires ReportLab. The raw 2024 attendance and 2025 economics PDFs and extracted text are retained under research/raw. The 2025 attendance source returned 404 on direct retrieval; the script preserves the indexed-text transcription and validates annual totals. See methodology for limits.

## Interpretation
Park visits are not unique people or total town visitors. Relative quiet is not spare capacity. Spending areas overlap; do not sum them into regional impacts. Receiving-community consent and operational capacity require further research. No personal data or analytics are collected. The NPS regional photograph is public domain; credit and source are linked on the website.
