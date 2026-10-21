"""Build the bilingual portfolio and add editorial project walkthroughs."""
from pathlib import Path
import build_portfolio as base

D = Path(__file__).parent / 'dist'
for lang in ('fr', 'en'):
    fr = lang == 'fr'
    path = D / ('index.html' if fr else 'en.html')
    html = path.read_text(encoding='utf-8')
    for i in range(8):
        html = html.replace(f'class="project p{i}"', f'id="project-{i}" class="project p{i}"')
    title = 'De la donnée à une application utile.' if fr else 'From data to useful software.'
    subtitle = 'Trois projets pour explorer ma façon de travailler.' if fr else 'Three projects that show how I work.'
    flows = [
        (0, '01 / SOFTWARE + AI', ['Documents', 'Extraction IA', 'Revue humaine', 'Gestion métier'] if fr else ['Documents', 'AI extraction', 'Human review', 'Business workflows'], 'Une expérience collective chez Arimas Holdings, comme team leader et ingénieure IA / logiciel stagiaire.' if fr else 'A team project at Arimas Holdings, where I worked as a team leader and AI / software engineering intern.'),
        (1, '02 / DATA + DECISIONS', ['Transactions', 'SQL / DuckDB', 'Segmentation', 'Tableau de bord'] if fr else ['Transactions', 'SQL / DuckDB', 'Segmentation', 'Dashboard'], 'Relier l’exploration de données e-commerce à des analyses de clients, produits et revenus.' if fr else 'Connect e-commerce data exploration with customer, product and revenue analysis.'),
        (4, '03 / ML + SECURITY', ['Données CAN', 'Alerte locale', 'Budget de requêtes', 'Confirmation'] if fr else ['CAN recordings', 'Local warning', 'Request budget', 'Confirmation'], 'Explorer par simulation les compromis entre détection, fausses alertes et communication.' if fr else 'Explore detection, false-alert and communication trade-offs through simulation.'),
    ]
    stories = ''
    for i, label, steps, desc in flows:
        diagram = ''.join(f'<li><span>{n+1:02}</span>{step}</li>' for n, step in enumerate(steps))
        stories += f'''<article class="spotlight"><div class="spotlight-copy"><p class="micro">{label}</p><h3>{base.projects[i]['name']}</h3><p>{desc}</p><a class="source project-jump" href="#project-{i}">{'Explorer le projet' if fr else 'Explore the project'}</a></div><div class="workflow"><p class="diagram-label">{'SCHÉMA DU FONCTIONNEMENT' if fr else 'WORKFLOW OVERVIEW'}</p><ol>{diagram}</ol><p class="diagram-caption">{'Schéma explicatif · détails et périmètre dans la fiche projet' if fr else 'Explanatory diagram · details and scope in the project entry'}</p></div></article>'''
    section = f'<section class="section selected" id="selected"><div class="heading"><div><p class="micro">SELECTED WORK / 2026</p><h2>{title}</h2></div><p>{subtitle}</p></div>{stories}</section>'
    html = html.replace('<section class="section work"', section + '<section class="section work"', 1)
    proof = [
        ('IA & software' if fr else 'AI & software', 'Stage · Arimas Holdings' if fr else 'Internship · Arimas Holdings', '#project-0'),
        ('Python & SQL', 'Mission freelance · EUMATRIX.eu' if fr else 'Freelance work · EUMATRIX.eu', '#experience'),
        ('ML & recherche' if fr else 'ML & research', 'Pipelines, vision & cybersécurité' if fr else 'Pipelines, vision & cybersecurity', '#project-4'),
    ]
    summary = '<div class="profile-proof">' + ''.join(f'<a class="project-jump" href="{link}"><strong>{a}</strong><span>{b}</span><b aria-hidden="true">↗</b></a>' for a,b,link in proof) + '</div>'
    html = html.replace('<section class="roles"', summary + '<section class="roles"', 1)
    html = html.replace('<a class="button acid" href="#projects">', '<a class="button acid" href="#selected">', 1)
    html = html.replace('<p class="micro">MERYEM<br>EL OSMANI</p>', '<p class="micro">MERYEM<br>EL OSMANI</p><p class="identity-location">Meknès · Maroc</p>' if fr else '<p class="micro">MERYEM<br>EL OSMANI</p><p class="identity-location">Meknès · Morocco</p>')
    html = html.replace('SELECTED WORK / 2026', 'SÉLECTION / 2026' if fr else 'SELECTED WORK / 2026')
    html = html.replace('</head>', '<meta name="theme-color" content="#0c1014"></head>')
    html = html.replace('<script src="site.js" defer>', '<script src="site.js?v=3" defer>')
    html = html.replace('href="style.css"', 'href="style.css?v=3"')
    path.write_text(html, encoding='utf-8')
print('Enhanced both languages with featured workflows and evidence links.')
