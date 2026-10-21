from pathlib import Path
import ast
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import pdfplumber

ROOT=Path(__file__).parent
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
def literal(path, name):
    tree=ast.parse(path.read_text(encoding='utf-8'))
    for n in tree.body:
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets):
            return eval(compile(ast.Expression(n.value),str(path),'eval'),{'dict':dict})
content=literal(ROOT/'build_cvs.py','content')
web=literal(ROOT/'build_portfolio.py','copy')
pdfmetrics.registerFont(TTFont('Body','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Bold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
ink=HexColor('#19232d'); blue=HexColor('#2454a5')
body=ParagraphStyle('body',fontName='Body',fontSize=9,leading=11.9,textColor=ink,spaceAfter=3)
small=ParagraphStyle('small',parent=body,fontSize=8.4,leading=10.8)
heading=ParagraphStyle('head',parent=body,fontName='Bold',fontSize=10.2,leading=13,spaceBefore=8,spaceAfter=3,textColor=blue)
name=ParagraphStyle('name',parent=body,fontName='Bold',fontSize=25,leading=29,alignment=1,spaceAfter=5)
center=ParagraphStyle('center',parent=small,alignment=1)
for lang in ('fr','en'):
    c=content[lang]; w=web[lang]; fr=lang=='fr'; story=[]; plain=[]
    def p(t,s=body): story.append(Paragraph(t,s)); plain.append(t)
    def sec(t): p(t,heading); story.append(HRFlowable(width='100%',thickness=.5,color=HexColor('#c4cbd3'),spaceAfter=4))
    p('Meryem El Osmani',name)
    p('IA & SOFTWARE | STAGE PFE 2027' if fr else 'AI & SOFTWARE | GRADUATION INTERNSHIP 2027',center)
    p(('Meknès, Maroc' if fr else 'Meknès, Morocco')+' | +212 684 836 656 | <link href="mailto:maryamelosmani@gmail.com">maryamelosmani@gmail.com</link>',center)
    p('<link href="https://github.com/MERYEMELOSMANI" color="#2454a5">GitHub: MERYEMELOSMANI</link> | <link href="https://www.linkedin.com/in/meryem-el-osmani-754a56271" color="#2454a5">LinkedIn: Meryem El Osmani</link>',center)
    sec('PROFIL' if fr else 'PROFESSIONAL SUMMARY')
    p('Étudiante en master IA et systèmes de décision optimale, avec une expérience de team leader et d’ingénieure IA / logiciel stagiaire chez Arimas Holdings, ainsi qu’en analyse freelance Python/SQL. Je relie modélisation, API et applications. Recherche de stage PFE au Maroc, de février / mars à juillet 2027.' if fr else 'Master’s student in AI and Optimal Decision Systems, with team leadership and AI/software internship experience at Arimas Holdings and freelance Python/SQL data analysis. I connect modelling, APIs and applications. Seeking a graduation internship in Morocco, February / March to July 2027.')
    sec(c['expTitle'])
    for i in range(3):
        date,company,role,_=w['exp'][i]
        p(f'<b>{company}</b> | {date.replace("—","-")}',body)
        p(role,small)
        bullets=c['bullets'][i][:1]
        if i==0: bullets+=['Contribution au développement IA / logiciel d’une plateforme collective de facturation, clients, stocks et reporting. Environnement : Django REST, Next.js, TypeScript, Gemini.' if fr else 'Contributed to AI/software development of a team-built platform for invoicing, customers, inventory and reporting. Environment: Django REST, Next.js, TypeScript, Gemini.']
        for b in bullets:p('- '+b,small)
    p('<b>AREP, Meknès</b> | '+('Stagiaire IT, juillet-août 2023 : support, incidents et guides utilisateurs.' if fr else 'IT intern, July-August 2023: support, incident resolution and user guides.'),small)
    sec('PROJETS SÉLECTIONNÉS' if fr else 'SELECTED PROJECTS')
    projects=[
      ('ResearchOS','research-os','FastAPI, Next.js, pgvector','Recherche documentaire avec génération augmentée par recherche (RAG) et réponses sourcées ; comparaison de modèles prédictifs.' if fr else 'Document retrieval with Retrieval-Augmented Generation (RAG) and sourced answers; predictive model benchmarking.'),
      ('Analyste IA multi-agents','autonomous-ai-data-analyst','LangGraph, DuckDB, Polars, Gemini','Conception d’un système de 6 agents pour analyser les données, vérifier les résultats et produire des graphiques et des rapports.' if fr else 'Design of a 6-agent system to analyze data, verify results, and generate charts and reports.'),
      ('V2C-Sentinel','V2C-Sentinel','Python, Logistic Regression, Random Forest','Détection d’intrusions CAN (Controller Area Network) en simulation locale : requêtes de confirmation limitées et délais 5G rejoués.' if fr else 'CAN (Controller Area Network) intrusion detection under local simulation: constrained confirmation requests and replayed 5G delays.')]
    for title,repo,stack,desc in projects:
        p(f'<b>{title}</b> | <link href="https://github.com/MERYEMELOSMANI/{repo}" color="#2454a5">GitHub</link>',body)
        p('• '+desc+' '+stack,small)
    sec(c['eduTitle'])
    for date,title,school in w['edu']:
        p(f'<b>{date.replace("—","-")} | {title}</b><br/>{school}',small)
    sec('COMPÉTENCES TECHNIQUES' if fr else 'TECHNICAL SKILLS')
    p('<b>Data & ML:</b> Python, SQL, Pandas, NumPy, Scikit-learn, OpenCV, MediaPipe.<br/><b>Software & MLOps:</b> Django REST, FastAPI, Flask, Next.js, TypeScript, Git, Docker, DVC, MLflow.<br/><b>'+('Optimisation & visualisation' if fr else 'Optimisation & visualization')+':</b> PuLP, '+('programmation linéaire' if fr else 'linear programming')+', Streamlit, Plotly, Tableau.',small)
    sec('CERTIFICATS & LANGUES' if fr else 'CERTIFICATES & LANGUAGES')
    p('<b>Google Cloud Cybersecurity Certificate</b> | '+('Formation : Python for Data Science & AI - IBM/Coursera.' if fr else 'Training: Python for Data Science & AI - IBM/Coursera.'),small)
    p(c['languages'],small)
    path=OUT/f'Meryem_El_Osmani_CV_{lang.upper()}_Focused.pdf'
    SimpleDocTemplate(str(path),pagesize=A4,leftMargin=39,rightMargin=39,topMargin=30,bottomMargin=28,title='Meryem El Osmani | AI & Software',author='Meryem El Osmani').build(story)
    (OUT/f'CV_{lang.upper()}_editable.txt').write_text('\n\n'.join(plain),encoding='utf-8')
    with pdfplumber.open(path) as pdf:
        print(lang,'pages:',len(pdf.pages))
        for i,page in enumerate(pdf.pages):page.to_image(resolution=120).save(OUT/f'cv-{lang}-{i+1}.png')

