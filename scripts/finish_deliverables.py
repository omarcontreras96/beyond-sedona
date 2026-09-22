from pathlib import Path
import json, zipfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape
R=Path(__file__).resolve().parents[1]; D=R/'dist'
m=json.loads((R/'research/methodology-content.json').read_text())
styles={k:ParagraphStyle(k,fontName=f,fontSize=s,leading=l,textColor=HexColor('#183129'),spaceAfter=a) for k,f,s,l,a in [('title','Helvetica-Bold',24,28,8),('sub','Helvetica',9,12,12),('h','Helvetica-Bold',10,13,4),('p','Helvetica',9,12,8),('ref','Helvetica',8,10,2)]}
story=[Paragraph('Beyond Sedona',styles['title']),Paragraph('ONE-PAGE METHODOLOGY · MIT 1.125 · Research checked 22 September 2026 UTC',styles['sub'])]
for title,body in m['sections']:story.extend([Paragraph(escape(title),styles['h']),Paragraph(escape(body),styles['p'])])
story.append(Paragraph('Source links',styles['h']))
for n,title,url in m['refs']:story.append(Paragraph(f'{n}. <link href="{escape(url)}" color="#a7472e">{escape(title)}</link>',styles['ref']))
SimpleDocTemplate(str(D/'data/methodology.pdf'),pagesize=(612,792),rightMargin=42,leftMargin=42,topMargin=34,bottomMargin=30,title='Beyond Sedona: methodology',author='Beyond Sedona research project').build(story)
base=(D/'methodology.html').read_text();head=base.split('<main')[0];foot=base.split('</main>')[1]
def page(name,title,body): (D/name).write_text(head.replace('One-page methodology — Beyond Sedona',title+' — Beyond Sedona')+'<main id="main" class="document">'+body+'</main>'+foot)
steps=[('00:00–01:00','The planning question','Which nearby destinations should Arizona consider for seasonal side-trip promotion from Sedona? The intended user is an Arizona tourism planner choosing a small pilot. Start by explaining that selected parks are evidence about attractions, not complete town visitor counts.','index.html','Open the story'),('01:00–02:00','Let the evidence revise the premise','Show the year-over-year chart: the selected parks declined in 2025. Then use the heatmap year and experience filters. Slide Rock receives 34.9% of annual visits in June–August, compared with 16.5% at Jerome. Different seasonal patterns are a reason to investigate, not proof of spare capacity.','index.html#explore','Demonstrate the heatmap'),('02:00–03:00','Compare a destination and a month','Select Dead Horse Ranch and September in the comparison. Its 11,705 visits are about 51% of its own 2025 peak. Change to Jerome and a summer month. Explain why relative annual shares compare timing more fairly than raw counts, but do not measure visitor willingness to take a side trip.','index.html#destinations','Demonstrate the comparison'),('03:00–04:00','Economic value needs local context','Show the spending category filter. Dead Horse Ranch is associated with $18.444 million of direct non-local visitor spending within 50 miles; that is not Cottonwood-only revenue or a campaign forecast. Show the resident feedback: 49% prefer a smaller tourism role, 45% the same, 6% more. This is Sedona’s survey, not consent from receiving towns.','index.html#economy','Show spending and resident context'),('04:00–05:00','Make a conditional recommendation','Propose Cottonwood in September, a small Jerome summer museum test, and Fort Verde outside its October peak. Keep Rockin’ River Ranch conditional because operating days and opening history complicate comparison. Before promotion: confirm staffing, conditions and community support. Measure itinerary substitution, local spending and resident effects. Close by opening the downloadable data and methodology.','index.html#recommendations','Show the shortlist')]
body='<p class="eyebrow">CLASS PRESENTATION / FIVE MINUTES</p><h1>A guided tour of the evidence.</h1><p class="lede">Five one-minute segments, with speaking notes and links for a live demonstration. Open each demo in a second tab and return here between segments.</p><div class="download-grid"><a href="data/presentation-notes.md" download>Download speaking notes ↓</a><a href="submission.html">Class deliverables ↗</a></div>'
for time,title,notes,url,label in steps: body+=f'<article class="source-card"><p class="eyebrow">{time}</p><h2>{title}</h2><p>{notes}</p><p><a class="button" href="{url}" target="_blank" rel="noopener">{label} ↗</a></p></article>'
page('presentation.html','Five-minute presentation',body)
(D/'data/presentation-notes.md').write_text('# Beyond Sedona — five-minute live demonstration\n\n'+'\n\n'.join(f'## {t}: {title}\n{notes}\nDemo: {url}' for t,title,notes,url,_ in steps))
page('submission.html','Class deliverables','''<p class="eyebrow">MIT 1.125 / PS01</p><h1>The submission package.</h1><p class="lede">The research story, the evidence behind it, and the materials for presenting it.</p><div class="download-grid"><a href="index.html">Interactive website ↗</a><a href="data/research-dataset.zip" download>Dataset: CSVs and dictionary ↓</a><a href="data/methodology.pdf" download>One-page methodology PDF ↓</a><a href="presentation.html">Five-minute live-demo guide ↗</a><a href="reflection.html">Short reflection draft ↗</a><a href="https://github.com/omarcontreras96/beyond-sedona" target="_blank" rel="noopener">GitHub source repository ↗</a></div><h2>Site requirements</h2><ul><li><strong>User and problem:</strong> Arizona tourism planners screening seasonal side-trip pilots.</li><li><strong>Collection:</strong> public aggregate tables, extraction and manual transcription with annual-total checks; documented on the sources page.</li><li><strong>Visual evidence:</strong> monthly heatmap, annual change bars, seasonal comparison, spending bars, hotel table and resident-response chart.</li><li><strong>Controls:</strong> year, experience, heatmap units, destination, month and spending category.</li><li><strong>Findings and action:</strong> three conditional recommendations linked to observations and missing evidence.</li><li><strong>Transparency:</strong> dates, units, definitions, original links, downloadable data and explicit limits.</li><li><strong>Access:</strong> responsive layouts, labeled controls, keyboard focus, accessible chart summaries and public aggregate data.</li></ul><h2>Before handing in</h2><p>Personalize the reflection with your own experience. The GitHub copy is private; give the instructor access if required. Rehearse the five-minute live demonstration. Add the published website URL to your PS1 cell in the class submission sheet. The sheet has not been edited by this project.</p><p><a href="https://docs.google.com/spreadsheets/d/1ZewIG5udWWpk3Kdrab5yDbsWDV4gnH3liKobIAp7HG4/edit?usp=sharing" target="_blank" rel="noopener">Open the class submission sheet ↗</a></p>''')
with zipfile.ZipFile(D/'data/research-dataset.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted((D/'data').glob('*.csv')):z.write(f,f.name)
 z.write(D/'data/data-dictionary.md','data-dictionary.md')
(R/'README.md').write_text('''# Beyond Sedona
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
''')
(R/'.gitignore').write_text('.DS_Store\n__pycache__/\n*.pyc\nqa/\n')
print('Created remaining deliverables and PDF')
