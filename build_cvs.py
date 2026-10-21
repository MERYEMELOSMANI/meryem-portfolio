from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import pdfplumber
from build_portfolio import copy, projects, GH

ROOT=Path(__file__).parent
pdfmetrics.registerFont(TTFont('CVArial',r'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('CVArialBold',r'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('CVArial',normal='CVArial',bold='CVArialBold')
ink=HexColor('#172c43'); blue=HexColor('#2454bd')
style=ParagraphStyle('body',fontName='CVArial',fontSize=9.7,leading=13.4,textColor=ink,spaceAfter=5)
small=ParagraphStyle('small',parent=style,fontSize=8.6,leading=11.6,spaceAfter=4)
name=ParagraphStyle('name',parent=style,fontName='CVArialBold',fontSize=25,leading=30,spaceAfter=6)
headline=ParagraphStyle('headline',parent=style,fontName='CVArialBold',fontSize=11.5,leading=16,spaceAfter=6)
section=ParagraphStyle('section',parent=style,fontName='CVArialBold',fontSize=10.7,leading=15,spaceBefore=12,spaceAfter=5,textColor=blue)
entry=ParagraphStyle('entry',parent=style,fontName='CVArialBold',fontSize=10.2,leading=14,spaceBefore=5,spaceAfter=4)
bullet=ParagraphStyle('bullet',parent=style,leftIndent=9,firstLineIndent=-8,spaceAfter=4)
project_style=ParagraphStyle('project',parent=style,fontSize=9.1,leading=12.3,spaceAfter=3)

content={
'fr':dict(title='STAGE PFE - IA, DATA & DÉVELOPPEMENT LOGICIEL',availability='Février / mars à juillet 2027 | Maroc',profile='Étudiante en master Intelligence artificielle et systèmes de décision optimale, avec une expérience de team leader et d’ingénieure IA / logiciel stagiaire chez Arimas Holdings. Mon parcours associe analyse de données, machine learning, applications full-stack et recherche opérationnelle. Je recherche un stage PFE pour contribuer à un projet Data, IA ou logiciel, de l’analyse du besoin à la réalisation technique.',profileTitle='PROFIL',expTitle='EXPÉRIENCE PROFESSIONNELLE',eduTitle='FORMATION',projectTitle='PROJETS TECHNIQUES',skillTitle='COMPÉTENCES MOBILISÉES DANS LES PROJETS',certTitle='CERTIFICATS & FORMATIONS',languages='Arabe : langue maternelle | Français : B2 | Anglais : C1 (EF SET : 74/100)',bullets=[['Team leader au sein de l’équipe de développement de Tadbir AI, une application de gestion d’entreprise intégrant des fonctionnalités d’intelligence artificielle.','Contribution au développement logiciel et IA du projet. Le périmètre collectif couvre la facturation, les clients, les stocks, le reporting, l’extraction documentaire et l’import de données assisté par IA.'],['Collecte de données ciblées pour le marché danois ; nettoyage, transformation et structuration avec Python et SQL.','Validation de l’intégrité des données et automatisation de la collecte ; réalisation d’un nouvel engagement avec le même client.'],['Développement d’une application PHP/MySQL de génération automatique d’emplois du temps, déployée dans trois départements.','Rédaction des guides d’utilisation et de maintenance, validés par les encadrants académiques.'],['Résolution d’incidents et support aux outils internes au sein d’une équipe pluridisciplinaire.','Rédaction de guides pour les utilisateurs non techniques.']],environment='Environnement du projet',page='Page',portfolio='Portfolio',projectdesc=[
('Pricing Analytics Engine','Analyse du jeu public Online Retail II (plus d’un million de transactions) : segmentation RFM, valeur client, classification ABC-XYZ, exploration prix-demande et prévisions.','DuckDB, SQL, FastAPI, Prophet, Chart.js',1),
('Customer Churn - MLOps','Pipeline de prédiction d’attrition : préparation des données, entraînement, suivi d’expériences, API de prédiction et surveillance de dérive.','Scikit-learn, DVC, MLflow, FastAPI, Docker',2),
('Supply Chain Optimization','Tableau de bord de scénarios logistiques : programmation linéaire, optimisation multi-objectifs, simulation Monte-Carlo et analyse de sensibilité.','Python, PuLP, Streamlit, Plotly',3),
('V2C-Sentinel','Prototype de recherche sur la détection d’intrusions CAN : alerte locale et confirmation avec budget de requêtes et délais 5G rejoués. Étude de cas par simulation locale.','Python, régression logistique, forêt aléatoire',4),
('Traffic Flow Prediction','Préparation des données et comparaison de modèles de prédiction de trafic : SVR, KNN, arbres de décision et régression multiple ; visualisation web.','Python, Scikit-learn, JavaScript',5),
('Computer Vision Gesture Suite','Démonstrations webcam de suivi des mains, dessin gestuel, écriture dans l’air et interactions par pincement des doigts.','Python, OpenCV, MediaPipe',6),
('Contact Manager','Application de gestion de contacts : connexion utilisateur, recherche, catégories, agenda, assistant IA, e-mail et export CSV.','Flask, SQLite, Jinja2, Gemini',7)],skills='<b>Data & visualisation :</b> Python, SQL, Pandas, NumPy, Tableau, Excel, Matplotlib, Seaborn.<br/><b>Software & MLOps :</b> Django REST, FastAPI, Flask, Next.js, TypeScript, Git, Docker, DVC, MLflow.<br/><b>IA & optimisation :</b> Scikit-learn, OpenCV, MediaPipe, Gemini, PuLP, programmation linéaire.<br/><b>Collaboration :</b> team leadership en stage, travail en équipe, documentation technique.'),
'en':dict(title='GRADUATION INTERNSHIP - AI, DATA & SOFTWARE',availability='February / March to July 2027 | Morocco',profile='Master’s student in Artificial Intelligence and Optimal Decision Systems, with experience as a team leader and AI / software engineering intern at Arimas Holdings. My work spans data analysis, machine learning, full-stack applications and operations research. Seeking a graduation internship contributing to a data, AI or software project, from understanding requirements to technical implementation.',profileTitle='PROFILE',expTitle='PROFESSIONAL EXPERIENCE',eduTitle='EDUCATION',projectTitle='TECHNICAL PROJECTS',skillTitle='SKILLS USED IN PROJECTS',certTitle='CERTIFICATES & TRAINING',languages='Arabic: Native | French: B2 | English: C1 (EF SET: 74/100)',bullets=[['Team leader within the development team for Tadbir AI, a business management application integrating artificial intelligence capabilities.','Contributed to software and AI development. The team’s application covers invoicing, customers, inventory, reporting, document extraction and AI-assisted data imports.'],['Collected targeted datasets for the Danish market; cleaned, transformed and structured data using Python and SQL.','Validated data integrity and automated collection workflows; completed a follow-up engagement with the same client.'],['Developed a PHP/MySQL application for automatic timetable generation, deployed across three departments.','Produced user and maintenance documentation validated by academic supervisors.'],['Resolved technical incidents and supported internal tools within a multidisciplinary team.','Prepared user guides for non-technical staff.']],environment='Project environment',page='Page',portfolio='Portfolio',projectdesc=[
('Pricing Analytics Engine','Analysis of the public Online Retail II dataset (over one million transactions): RFM segmentation, customer value, ABC-XYZ classification, price-demand exploration and forecasts.','DuckDB, SQL, FastAPI, Prophet, Chart.js',1),
('Customer Churn - MLOps','Churn prediction pipeline covering data preparation, training, experiment tracking, a prediction API and drift monitoring.','Scikit-learn, DVC, MLflow, FastAPI, Docker',2),
('Supply Chain Optimization','Logistics scenario dashboard combining linear programming, multi-objective optimization, Monte Carlo simulation and sensitivity analysis.','Python, PuLP, Streamlit, Plotly',3),
('V2C-Sentinel','CAN intrusion detection research prototype: local warnings and confirmation under a request budget with replayed 5G delays. A locally simulated case study.','Python, logistic regression, random forest',4),
('Traffic Flow Prediction','Data preparation and comparison of traffic prediction models: SVR, KNN, decision trees and multiple regression, with web visualization.','Python, Scikit-learn, JavaScript',5),
('Computer Vision Gesture Suite','Webcam demonstrations for hand tracking, gesture painting, air writing and pinch-based interactions.','Python, OpenCV, MediaPipe',6),
('Contact Manager','Contact management application with user login, search, categories, agenda, an AI assistant, email integration and CSV export.','Flask, SQLite, Jinja2, Gemini',7)],skills='<b>Data & visualization:</b> Python, SQL, Pandas, NumPy, Tableau, Excel, Matplotlib, Seaborn.<br/><b>Software & MLOps:</b> Django REST, FastAPI, Flask, Next.js, TypeScript, Git, Docker, DVC, MLflow.<br/><b>AI & optimization:</b> Scikit-learn, OpenCV, MediaPipe, Gemini, PuLP, linear programming.<br/><b>Collaboration:</b> internship team leadership, teamwork and technical documentation.')}

def build(lang):
 c=content[lang]; web=copy[lang]; story=[]
 def p(text,sty=style): story.append(Paragraph(text,sty))
 def sec(text):
  p(text,section);story.append(HRFlowable(width='100%',thickness=.5,color=HexColor('#c6d3df'),spaceAfter=4))
 p('MERYEM EL OSMANI',name);p(c['title'],headline)
 p(c['availability'],style)
 p('Meknès · +212 684 836 656 · <link href="mailto:maryamelosmani@gmail.com">maryamelosmani@gmail.com</link> · <link href="https://meryemelosmani.site" color="#2454bd">meryemelosmani.site</link>',small)
 p('<link href="https://github.com/MERYEMELOSMANI" color="#2454bd">GitHub: MERYEMELOSMANI</link> · <link href="https://www.linkedin.com/in/meryem-el-osmani-754a56271" color="#2454bd">LinkedIn: Meryem El Osmani</link>',small)
 sec(c['profileTitle']);p(c['profile'])
 sec(c['expTitle'])
 for i,(date,company,role,_) in enumerate(web['exp']):
  p(escape(role)+' | '+escape(company),entry);p(date.replace('—',' - '),small)
  for b in c['bullets'][i]: p('• '+escape(b),bullet)
  if i==0:p(c['environment']+': Python, Django REST Framework, Next.js, TypeScript, Gemini.',small)
 sec(c['eduTitle'])
 for date,title,school in web['edu']:
  p('<b>'+escape(title)+'</b> | '+date.replace('—',' - '),style);p(escape(school),small)
 story.append(PageBreak())
 p('MERYEM EL OSMANI',headline)
 p('AI · DATA · SOFTWARE · MLOPS · OPERATIONS RESEARCH',small)
 sec(c['projectTitle'])
 for title,desc,stack,index in c['projectdesc']:
  p('<link href="'+GH+projects[index]['repo']+'" color="#2454bd"><b>'+escape(title)+'</b></link>',entry)
  p(escape(desc),project_style);p(escape(stack),small)
 sec(c['skillTitle']);p(c['skills'],project_style)
 sec(c['certTitle'])
 p('<b>Google Cloud Cybersecurity Certificate</b> - Google Cloud.<br/><b>IBM / Coursera:</b> Python for Data Science &amp; AI; Generative AI for Data Analytics; Prompt Engineering Foundations.<br/><b>AWS:</b> Technical Essentials. <b>Tableau</b> (Salesforce). <b>NTU:</b> Operations Research: Optimization Algorithms.',small)
 p('<b>'+escape(c['languages'])+'</b>',small)
 path=ROOT/'dist'/f'Meryem_El_Osmani_CV_{lang.upper()}.pdf'
 def footer(canvas,doc):
  canvas.setFont('CVArial',8);canvas.setFillColor(HexColor('#617184'))
  canvas.drawString(36,24,'Meryem El Osmani | '+('Stage PFE 2027' if lang=='fr' else 'Graduation internship 2027'))
  canvas.drawRightString(A4[0]-36,24,c['page']+' '+str(doc.page))
 doc=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=36,rightMargin=36,topMargin=29,bottomMargin=40,title='Meryem El Osmani - '+c['title'],author='Meryem El Osmani')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
 with pdfplumber.open(path) as pdf:
  print(lang,len(pdf.pages),'pages')
  (ROOT/f'CV_{lang.upper()}_editable.txt').write_text('\n\n'.join(page.extract_text() for page in pdf.pages),encoding='utf-8')
  for i,page in enumerate(pdf.pages):page.to_image(resolution=110).save(str(ROOT/f'cv-{lang}-{i+1}.png'))
for lang in ['fr','en']:build(lang)
# Preserve the first version's download URL while replacing its content with the revised French CV.
(ROOT/'dist/Meryem_El_Osmani_CV.pdf').write_bytes((ROOT/'dist/Meryem_El_Osmani_CV_FR.pdf').read_bytes())
