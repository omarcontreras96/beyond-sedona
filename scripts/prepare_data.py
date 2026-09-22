from pathlib import Path
import csv,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'research/processed'; OUT.mkdir(parents=True,exist_ok=True)
WEB=ROOT/'dist/data'; WEB.mkdir(parents=True,exist_ok=True)
DATE='2026-09-22'
urls={'vis2024':'https://in.nau.edu/wp-content/uploads/sites/212/State-Parks-2024-1.pdf','vis2025':'https://in.nau.edu/wp-content/uploads/sites/212/State-Parks-2025-2.pdf','economics':'https://extension.arizona.edu/sites/default/files/2026-06/ASP-2025-Economic-Impact-Report_05152026.pdf','residents':'https://www.sedonaaz.gov/home/showpublisheddocument/53237/638718401613770000','lodging':'https://www.sedonaaz.gov/home/showpublisheddocument/55452/639015695406600000'}
# 2025 rows transcribed from the public research PDF's indexed text; annual totals independently cross-checked against the economic report, Table 2.
y2025={
'Slide Rock':[16165,24182,37981,51275,43048,54512,53162,44339,35158,39104,21827,14333,435086],
'Red Rock':[5211,6761,10884,10332,6974,3789,3347,3057,4690,7983,7115,6074,76217],
'Dead Horse Ranch':[17694,20666,23131,21417,19598,11012,9394,6914,11705,17358,18626,12147,189662],
'Jerome':[3446,4398,6033,4667,3510,2617,2256,2053,2571,4398,3289,2676,41914],
'Fort Verde':[516,904,1117,956,619,649,418,342,524,1461,674,589,8769],
"Rockin' River Ranch":[786,813,761,516,486,331,214,234,340,472,418,301,5672]}
parks=[
{'id':'slide','name':'Slide Rock','fullName':'Slide Rock State Park','community':'Sedona area','role':'Reference','type':'Water & outdoors','url':'https://azstateparks.com/slide-rock','color':'#aa482b'},
{'id':'red','name':'Red Rock','fullName':'Red Rock State Park','community':'Sedona area','role':'Reference','type':'Nature & trails','url':'https://azstateparks.com/red-rock','color':'#c98234'},
{'id':'dead','name':'Dead Horse Ranch','fullName':'Dead Horse Ranch State Park','community':'Cottonwood','role':'Candidate','type':'Nature & trails','url':'https://azstateparks.com/dead-horse','color':'#24594b'},
{'id':'jerome','name':'Jerome','fullName':'Jerome State Historic Park','community':'Jerome','role':'Candidate','type':'History & culture','url':'https://azstateparks.com/jerome','color':'#674b8a'},
{'id':'fort','name':'Fort Verde','fullName':'Fort Verde State Historic Park','community':'Camp Verde','role':'Candidate','type':'History & culture','url':'https://azstateparks.com/fort-verde','color':'#30677d'},
{'id':'rockin','name':"Rockin' River Ranch",'fullName':"Rockin' River Ranch State Park",'community':'Camp Verde','role':'Candidate','type':'Nature & trails','url':'https://azstateparks.com/rockin-river/','color':'#826b2f'}]
text=(ROOT/'research/raw/visitation-2024.txt').read_text()
rows=[]
for p in parks:
 line=next(l for l in text.splitlines() if l.startswith(p['name']+' '))
 v24=[int(n.replace(',','')) for n in re.findall(r'\d[\d,]*',line[len(p['name']):])]
 assert len(v24)==13,(p['name'],v24)
 p['visits']={2024:v24[:12],2025:y2025[p['name']][:12]}
 for year,vals in [(2024,v24),(2025,y2025[p['name']])]:
  assert sum(vals[:12])==vals[12],(p['name'],year,sum(vals[:12]),vals[12])
  for m,v in enumerate(vals[:12],1):
   rows.append({'park_id':p['id'],'park':p['fullName'],'community':p['community'],'year':year,'month':m,'visits':v,'unit':'park visits','status':'not yet open' if p['id']=='rockin' and year==2024 and m==1 else 'reported','source_url':urls['vis'+str(year)],'retrieved_utc':DATE})
# Non-local visitor spending within 50 miles of park; nominal 2025 USD; Tables 35 and 44.
categories=['Admission/recreation','Camping','Lodging','Groceries','Food and beverage','Retail','Auto','Other']
spend={
'slide':[4686000,797000,18963000,5763000,10019000,5406000,4787000,1045000],
'red':[1009000,571000,7448000,2044000,3881000,1255000,1508000,496000],
'dead':[1469000,4421000,1966000,2840000,3228000,1170000,2806000,543000],
'jerome':[662000,187000,2819000,680000,1803000,863000,582000,121000],
'fort':[128000,76000,596000,111000,281000,87000,147000,23000],
'rockin':[26000,45000,77000,34000,52000,26000,38000,2000]}
direct={'slide':51467000,'red':18213000,'dead':18444000,'jerome':7718000,'fort':1448000,'rockin':300000}
spendrows=[]
for p in parks:
 p['spending']=dict(zip(categories,spend[p['id']]))
 p['directSpending']=direct[p['id']]
 for c,v in p['spending'].items(): spendrows.append({'park_id':p['id'],'park':p['fullName'],'year':2025,'category':c,'value_usd':v,'unit':'nominal USD','geography':'within 50 miles of park','population':'non-local visitors (over 50 miles away)','source_table':35 if p['id']=='slide' else 44,'source_url':urls['economics'],'retrieved_utc':DATE})
 spendrows.append({'park_id':p['id'],'park':p['fullName'],'year':2025,'category':'Published direct total','value_usd':p['directSpending'],'unit':'nominal USD','geography':'within 50 miles of park','population':'non-local visitors (over 50 miles away)','source_table':35 if p['id']=='slide' else 44,'source_url':urls['economics'],'retrieved_utc':DATE})
residents=[{'year':2024,'response':r,'percent':v,'geography':'City of Sedona','overall_sample_n':551,'item_sample_n':'not reported','overall_response_rate_pct':20,'overall_margin_error_pp':4,'source_url':urls['residents'],'retrieved_utc':DATE} for r,v in [('Less of a role',49),('About the same',45),('More of a role',6)]]
lodging=[]
for geo,occ,adr in [('Sedona+',[59.6,64.2,74.8],[256,354,446]),('Village of Oak Creek+',[60.1,65.9,71.9],[165,214,251])]:
 for m,o,a in zip([8,9,10],occ,adr): lodging.append({'study_area':geo,'year':2025,'month':m,'occupancy_pct':o,'adr_usd':a,'source_url':urls['lodging'],'source_page':4,'retrieved_utc':DATE})
# All lodging transcriptions must be visually checked against page 4 before delivery.
def csvwrite(name,records):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
csvwrite('park-visitation.csv',rows);csvwrite('visitor-spending.csv',spendrows);csvwrite('resident-feedback.csv',residents);csvwrite('hotel-context.csv',lodging)
(WEB/'site-data.json').write_text(json.dumps({'retrieved':DATE,'parks':parks,'residents':residents,'lodging':lodging,'sources':urls},indent=2))
print('Validated',len(rows),'monthly observations,',len(spendrows),'spending observations')
for p in parks:
 a=p['visits'][2025];b=p['visits'][2024]
 print(p['name'],sum(a),'change',round((sum(a)/sum(b)-1)*100,1),'summer share',round(sum(a[5:8])/sum(a)*100,1),'peak',a.index(max(a))+1,'sep',round(a[8]/max(a)*100,1),'winter share',round((a[0]+a[1]+a[11])/sum(a)*100,1))
