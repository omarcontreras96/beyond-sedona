"""Create the four submission files outside the public site directory."""
from pathlib import Path
import csv,json,zipfile,hashlib
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
R=Path(__file__).resolve().parents[1];O=R/'output';PDF=O/'pdf';PDF.mkdir(parents=True,exist_ok=True)
SITE='https://beyond-sedona-verde-valley.omarcc96.chatgpt.site'
INK=HexColor('#183129');MUTED=HexColor('#536258');RUST=HexColor('#a34629')
styles={k:ParagraphStyle(k,fontName=f,fontSize=s,leading=l,textColor=INK,spaceAfter=a) for k,f,s,l,a in [('title','Helvetica-Bold',24,28,8),('sub','Helvetica',9,12,12),('h','Helvetica-Bold',10.5,14,5),('p','Helvetica',10,14,10),('compact','Helvetica',9,12,8),('ref','Helvetica',8,10,3),('note','Helvetica-Oblique',9,12,10)]}
def clean(t):return t.replace('–','-').replace('—','-').replace('\u2011','-')
def p(t,style='p'):return Paragraph(escape(clean(t)),styles[style])
def link(url,text,style='ref'):return Paragraph(f'<link href="{escape(url)}" color="#a34629">{escape(text)}</link>',styles[style])
def footer(c,doc):
 c.setStrokeColor(HexColor('#d7ddd5'));c.line(42,38,570,38);c.setFillColor(MUTED);c.setFont('Helvetica',8);c.drawString(42,25,'BEYOND SEDONA | MIT 1.125 | 22 September 2026');c.drawRightString(570,25,str(doc.page))
def build(name,title,story):
 SimpleDocTemplate(str(PDF/name),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=36,bottomMargin=52,title=title,author='Beyond Sedona research project').build(story,onFirstPage=footer,onLaterPages=footer)
m=json.loads((R/'research/methodology-content.json').read_text())
s=[p('Beyond Sedona','title'),p('DATA AND METHODOLOGY | One-page note','sub')]
for title,text in m['sections']:s.extend([p(title,'h'),p(text,'compact')])
s.append(p('Primary source links','h'))
for n,title,url in m['refs']:s.append(link(url,n+'. '+title))
build('data-and-methodology.pdf','Beyond Sedona: data and methodology',s)
# A rehearsal script, deliberately not a claimed final deck or recording.
s=[p('Five minutes, one decision','title'),p('SITE DEMONSTRATION PLAN | Final deck or recording format: pending instructor guidance','sub'),p('Purpose','h'),p('Demonstrate how an Arizona tourism planner can use the site to screen seasonal side-trip pilots from Sedona. The objective is to connect evidence to choices while making the limits visible. This PDF is a rehearsal plan, not the final presentation format.'),link(SITE,'Open Beyond Sedona','p'),p('Before starting','h'),p('Open the site on a laptop, close unrelated tabs, and confirm the charts load. Begin with the heatmap set to 2025, All experiences, and % of each park’s peak month. Keep the destination comparison at Cottonwood / September and the spending filter at All spending. Rehearse once with a five-minute timer.','compact')]
segments=[
('0:00-0:45 | Frame the question','Homepage introduction','Say: “Which nearby destinations should Arizona consider for seasonal side-trip promotion from Sedona? This tool is for tourism planners choosing small, testable pilots in Cottonwood, Jerome and Camp Verde.” Explain that six state parks provide comparable attraction-level evidence; they do not measure all visitors to these towns.',''),
('0:45-1:45 | Show the seasonal evidence','Heatmap and annual-change chart','Click Explore the evidence. Switch the heatmap Display to Reported park visits, then back to % of each park’s peak month. Briefly select 2024 and return to 2025. Explain that the colors compare a park with its own peak, not its carrying capacity. Scroll to the annual-change chart: visits across the five comparable full-year parks fell 7.6%. The original “sudden surge” premise is not established by these data.','#explore'),
('1:45-2:45 | Test a place and a month','Destination comparison','Select Cottonwood / Dead Horse Ranch and Sep. Point to 11,705 visits, about 51% of that park’s own 2025 peak. Change Destination to Jerome and Month to Jul. Describe the contrast: Jerome received 16.5% of annual visits in June-August, versus 34.9% at Slide Rock. Different timing supports a test, but museum demand and local capacity still need verification.','#destinations'),
('2:45-3:45 | Add spending and resident context','Economic and resident sections','Change Category from All spending to Lodging and back. Dead Horse Ranch is associated with $18.444 million of direct non-local visitor spending within 50 miles in 2025. Explain that this is not Cottonwood-only revenue or a campaign forecast; park spending areas overlap. Show Sedona’s resident responses: 49% favor a smaller tourism role, 45% the same, and 6% more. These responses do not establish support in receiving towns.','#economy'),
('3:45-4:35 | Make a conditional recommendation','The shortlist','Propose a September Cottonwood nature-and-town pilot, a modest summer museum test in Jerome, and a smaller Fort Verde history itinerary outside its October peak. Keep Rockin’ River Ranch conditional because opening history and restricted operating days complicate the comparison. Before promotion, verify access, staffing, environmental conditions and receiving-community support.','#recommendations'),
('4:35-5:00 | Close with the next evidence','Sources and Google Drive link','Conclude: “The site can help choose what to test. It cannot prove spare capacity, additional spending, or less congestion in Sedona.” Open Sources & methodology to show provenance, then point to Google Drive files for the separate submission materials. A pilot must measure whether a side trip replaces time in Sedona or simply extends the trip.','/methods')]
for i,(timing,screen,words,anchor) in enumerate(segments):
 if i==3:s.append(PageBreak());s.extend([p('From evidence to a pilot','title'),p('DEMONSTRATION PLAN | Second half','sub')])
 block=[p(timing,'h'),p('On screen: '+screen,'note'),p(words,'p')]
 if anchor:block.append(link(SITE+anchor,'Open this part of the site'))
 s.append(KeepTogether(block));s.append(Spacer(1,5))
s.extend([Spacer(1,8),p('If the live site is unavailable','h'),p('Use the dataset and methodology PDFs to explain the same sequence. Do not claim to have demonstrated working controls. After class, adapt this plan to the confirmed deck or recording requirement.','compact')])
build('five-minute-demonstration-plan.pdf','Beyond Sedona: five-minute demonstration plan',s)
reflection=[
('The evidence revised the premise','The project began with the idea that a sudden visitor influx in one city could benefit nearby communities. The selected Arizona park records did not establish such a surge: all six parks recorded fewer visits in 2025 than in 2024. This is not proof that Sedona tourism as a whole declined, because the sample covers specific attractions. It did justify reframing the study around seasonal side-trip promotion rather than treating an unverified surge as fact.'),
('What the data supports','The strongest evidence concerns seasonal timing. Slide Rock received 34.9% of annual visits in June-August 2025, while Jerome State Historic Park received 16.5%. Dead Horse Ranch’s September count was about 51% of its own peak month. These differences support screening a September Cottonwood itinerary, a modest summer history option in Jerome, and an off-peak Fort Verde test. They identify hypotheses worth investigating; they do not establish an optimal destination ranking.'),
('What the data cannot prove','Lower attendance is not evidence of spare capacity. Heat, opening days, staffing, parking, events and ecological limits can all affect counts. Two years cannot establish a long-term trend or explain the causes of change. Park visits also include repeat visits and local users; they are not a census of unique tourists or total town visitation.'),
('Why spending and resident views need boundaries','The spending estimates concern non-local visitor activity within 50 miles of each park. These areas overlap and may include Sedona itself, so the estimates cannot be added into a regional windfall or used to predict new campaign revenue. Sedona’s weighted resident survey provides a reason to take local impacts seriously, but it does not speak for Cottonwood, Jerome or Camp Verde. Survey nonresponse and missing receiving-community feedback remain limitations.'),
('The practical conclusion','The website is useful as a transparent screening tool for small pilots. The next step is to ask local partners about capacity and priorities, confirm access and conditions, and test visitor interest. Evaluation should track local business participation, resident feedback and crowding, while asking whether side trips replace time in Sedona or extend a trip. The central lesson is that a credible recommendation makes its assumptions visible and states what evidence would be needed before expanding it.')]
s=[p('What the evidence can carry','title'),p('SHORT REFLECTION | Beyond Sedona','sub')]
for title,text in reflection:s.extend([p(title,'h'),p(text,'compact')])
s.extend([Spacer(1,6),link(SITE+'/methods','Sources and definitions supporting this reflection')])
build('short-reflection.pdf','Beyond Sedona: short reflection',s)
# Bundle actual source files separately from links to sources that could not be downloaded.
readme='''# Beyond Sedona - collected dataset and source evidence
Research checked: 2026-09-22 UTC. Website: https://beyond-sedona-verde-valley.omarcc96.chatgpt.site

## Contents
- data/: six CSV files (five datasets plus source register) and data dictionary.
- sources/: the TWO original PDFs successfully downloaded, plus extracted text:
  * visitation-2024.pdf: NAU / Arizona State Parks 2024 monthly attendance.
  * park-economics-2025.pdf: University of Arizona 2025 park economics report, published 2026.
- scripts/prepare_data.py: quantitative transformation and 2025 transcription fixture.
- source-notes.txt: provenance and retrieval limitations.
- SHA256SUMS.txt: checksums for files in this archive.

## What to use
park-visitation.csv: 144 park-month observations, six parks, 2024-2025.
visitor-spending.csv: 54 category/total entries, 2025 nominal USD.
resident-feedback.csv: three weighted percentages from Sedona's 2024 probability sample.
hotel-context.csv: six market-month observations, August-October 2025.
destinations.csv: six parks, official links, roles and explicit missing evidence.
source-register.csv: links and research date for the five primary statistical sources.
The dictionary gives definitions, formulas and caveats. Do not count published spending totals again alongside their categories.

## Reproduction
The included script expects to run in the source project: raw files in research/raw,
processed tables in research/processed, and runtime JSON in dist/data. For a standalone
reproduction, put the contents of sources/ into research/raw/ next to the scripts/
directory and run python3 scripts/prepare_data.py. It creates those output directories.
Destination metadata, the source register and dictionary are curated supporting files;
they are included directly rather than regenerated by this one script.

## Boundaries
These are public aggregate data, not personal records. Park visits are not unique people
or total town tourism. Quiet months are not measured capacity. Park spending geographies
overlap; no causal campaign effect, optimal allocation, or receiving-community consent
can be inferred. See source-notes.txt for unavailable original downloads.
'''
notes='''SOURCE RETRIEVAL NOTES

Downloaded originals included:
1. https://in.nau.edu/wp-content/uploads/sites/212/State-Parks-2024-1.pdf
   Extracted with pdftotext. Monthly counts were checked against published annual totals.
2. https://extension.arizona.edu/sites/default/files/2026-06/ASP-2025-Economic-Impact-Report_05152026.pdf
   University of Arizona, 2025 Economic Contributions & Impacts of Arizona State Parks.
   Table 2 cross-checks annual attendance; Tables 35 and 44 provide spending estimates.

Sources read through indexed public text; original PDF files NOT included:
3. https://in.nau.edu/wp-content/uploads/sites/212/State-Parks-2025-2.pdf
   Direct download returned 404 during collection. Monthly values were transcribed from
   indexed source text. Sums match the source annual totals, which also match source 2.
   The transcription fixture is in scripts/prepare_data.py. Annual checks do not rule
   out every possible monthly transcription error; an archived original remains desirable.
4. https://www.sedonaaz.gov/home/showpublisheddocument/53237/638718401613770000
   Sedona National Community Survey 2024. Direct download returned 403. Weighted
   probability sample: 551 overall respondents, 20% response rate, overall margin up
   to +/-4 percentage points at 95% confidence. Tourism-role item denominator not
   separately reported. Open-participation responses excluded. Methods pp.2-6; item p.30.
5. https://www.sedonaaz.gov/home/showpublisheddocument/55452/639015695406600000
   October 2025 lodging report. Direct download returned 403. Current hotel panel,
   PDF p.4, provides August-October data. Older embedded narrative was not used.
   April sample note: 21/44 Sedona+ hotels and 6/14 Village of Oak Creek+ hotels;
   a June renovation closure reduced Sedona+ supply. No candidate-town capacity data.

Operational context (links, not archived originals):
https://azstateparks.com/dead-horse
https://azstateparks.com/jerome
https://azstateparks.com/fort-verde
https://azstateparks.com/rockin-river/
https://arizona-content.usedirect.com/storage/Annual_Report_FY24_FINAL_4.pdf
https://verdeshuttle.com/routes/verde-shuttle/
https://azstateparks.com/arizona-summer-vacations
Hours checked in September 2026 are current offers, not historical operating-day data.
Rockin' River Ranch opened February 2024; January zero is flagged not yet open.
No missing source PDF has been recreated or represented as a downloaded original.
'''
files={'README.md':readme.encode(),'source-notes.txt':notes.encode()}
for f in sorted((R/'research/processed').iterdir()):
 if f.suffix in ['.csv','.md']:files['data/'+f.name]=f.read_bytes()
for f in sorted((R/'research/raw').iterdir()):
 if f.suffix in ['.pdf','.txt']:files['sources/'+f.name]=f.read_bytes()
files['scripts/prepare_data.py']=(R/'scripts/prepare_data.py').read_bytes()
files['SHA256SUMS.txt']=''.join(hashlib.sha256(v).hexdigest()+'  '+k+'\n' for k,v in files.items()).encode()
with zipfile.ZipFile(O/'beyond-sedona-dataset-and-sources.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name,content in files.items():z.writestr(name,content)
print('Created dataset/source ZIP and three PDFs in output/')
