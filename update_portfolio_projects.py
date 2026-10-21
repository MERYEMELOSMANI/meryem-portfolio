"""
Update portfolio projects to match the user's CV screenshot:
1. ResearchOS (RAG, FastAPI, Next.js, pgvector)
2. Analyste IA multi-agents (6 agents, LangGraph, DuckDB, Polars, Gemini)
3. V2C-Sentinel (CAN intrusion detection, 5G constraints, logistic regression, random forest)
"""
from pathlib import Path

file_path = Path("generate_unified_site.py")
content = file_path.read_text(encoding="utf-8")

new_case_studies = '''# Detailed case studies data matching structure 11 (CV featured projects)
case_studies = {
    'researchos': {
        'id': 'researchos',
        'title': 'ResearchOS',
        'tag': 'RAG · RECHERCHE DOCUMENTAIRE · PGVECTOR',
        'repo': None,
        'fr': {
            'subtitle': 'Recherche documentaire avec RAG et réponses sourcées · Comparaison de modèles',
            'overview': 'Recherche documentaire avec génération augmentée par recherche (RAG) et réponses sourcées ; comparaison de modèles prédictifs. FastAPI, Next.js, pgvector.',
            'contribution': 'Architecture logicielle et développement complet : pipeline d’ingestion et de vectorisation des documents avec pgvector, API asynchrone FastAPI, interface utilisateur Next.js et banc d’évaluation comparatif des modèles de prédiction et de réponse.',
            'how_it_works': 'Les documents sont découpés en fragments sémantiques et transformés en embeddings vectoriels indexés dans PostgreSQL avec pgvector. Lors d’une requête, une recherche de similarité cosinus extrait les passages les plus pertinents et les fournit au modèle génératif pour synthétiser des réponses étayées par des citations de sources vérifiables.',
            'decisions': 'Choix de PostgreSQL + pgvector pour regrouper les métadonnées relationnelles et les vecteurs au sein d’une même infrastructure transactionnelle sans complexité opérationnelle superflue, couplé à FastAPI pour le streaming temps réel.',
            'evaluation': 'Évaluation de la pertinence des extraits récupérés (Recall@k, MRR) et élimination des hallucinations factuelles grâce à une consigne stricte de sourçage obligatoire.',
            'limitations': 'La précision dépend de la stratégie de segmentation des documents (chunking) et du comportement des embeddings face aux termes scientifiques hautement spécialisés.',
            'lessons': 'L’ingénierie de la récupération (retrieval) et la qualité du nettoyage amont des données priment toujours sur la taille brute du modèle pour garantir des réponses exactes et fiables.'
        },
        'en': {
            'subtitle': 'Document retrieval with RAG and sourced answers · Model benchmarking',
            'overview': 'Document retrieval with Retrieval-Augmented Generation (RAG) and sourced answers; predictive model benchmarking. FastAPI, Next.js, pgvector.',
            'contribution': 'Full-stack architecture and engineering: document chunking and vector indexing pipeline using pgvector, asynchronous FastAPI backend, Next.js interface, and comparative model benchmarking.',
            'how_it_works': 'Technical documents are chunked and converted into high-dimensional embeddings stored in PostgreSQL with pgvector. A natural language query triggers cosine similarity search to retrieve grounded snippets, allowing the generative model to synthesize verified, source-cited responses.',
            'decisions': 'Selected PostgreSQL + pgvector to consolidate relational metadata and dense vectors in a unified database, combined with FastAPI for asynchronous streaming.',
            'evaluation': 'Benchmarked retrieval fidelity (Recall@k, MRR) and verified source grounding to eliminate unverified hallucinations.',
            'limitations': 'Performance is sensitive to document chunking granularity and domain vocabulary coverage in the embedding space.',
            'lessons': 'Rigorous retrieval curation and clean document chunking contribute far more to reliability than raw LLM scale.'
        }
    },
    'analyste-ia': {
        'id': 'analyste-ia',
        'title': 'Analyste IA multi-agents',
        'tag': 'SYSTÈMES MULTI-AGENTS · LANGGRAPH & DUCKDB',
        'repo': None,
        'fr': {
            'subtitle': 'Système collaboratif de 6 agents pour l’analyse de données et le reporting automatisé',
            'overview': 'Conception d’un système de 6 agents pour analyser les données, vérifier les résultats et produire des graphiques et des rapports. LangGraph, DuckDB, Polars, Gemini.',
            'contribution': 'Conception intégrale de l’architecture multi-agents sous LangGraph, formulation des rôles spécialisés, orchestration de l’état partagé et optimisation des calculs analytiques in-memory avec DuckDB et Polars.',
            'how_it_works': 'Six agents spécialisés collaborent selon un graphe d’états LangGraph : (1) Superviseur & Planificateur, (2) Ingestion & Profilage DuckDB, (3) Transformation Polars, (4) Validation Statistique, (5) Visualisation graphique, et (6) Rédacteur de Synthèse. Un sous-graphe de vérification audite les calculs avant toute génération de rapport.',
            'decisions': 'Choix d’un graphe d’états déterministe avec points de contrôle sous LangGraph plutôt qu’une chaîne linéaire opaque, et association DuckDB + Polars pour exécuter des requêtes analytiques massives avec une empreinte mémoire minimale.',
            'evaluation': 'Tests sur des séries de données réelles complexes avec anomalies injectées : la boucle d’auto-critique entre agents a permis de réduire drastiquement les erreurs de calcul par rapport aux agents solitaires.',
            'limitations': 'Exige un bac à sable (sandboxing) strict pour l’exécution de scripts Python générés et un monitoring précis des quotas d’appels à l’API Gemini.',
            'lessons': 'La décomposition en rôles étroits et mutuellement vérifiables surpasse largement les approches à invite unique pour les tâches analytiques critiques.'
        },
        'en': {
            'subtitle': 'Collaborative 6-agent system for data analysis, verification and reporting',
            'overview': 'Design of a 6-agent system to analyze data, verify results, and generate charts and reports. LangGraph, DuckDB, Polars, Gemini.',
            'contribution': 'Designed and implemented the complete LangGraph multi-agent architecture, authored discrete agent prompt contracts, managed execution state persistence, and accelerated in-memory data operations with DuckDB and Polars.',
            'how_it_works': 'Six specialized agents collaborate across a stateful LangGraph workflow: (1) Supervisor/Planner, (2) DuckDB Ingestion & Profiler, (3) Polars Transformer, (4) Statistical Verification, (5) Chart Generator, and (6) Report Synthesizer. An auditing cycle verifies computations before delivering final documents.',
            'decisions': 'Selected LangGraph for cycle-aware state transitions and safety checkpoints, paired with DuckDB and Polars for columnar speed without database overhead.',
            'evaluation': 'Evaluated against multi-table datasets with messy formats; the multi-agent critique loop eliminated mathematical hallucinations common in single-agent architectures.',
            'limitations': 'Requires secure sandboxed runtime environments for dynamic Python code execution and careful rate limiting for Gemini API tokens.',
            'lessons': 'Specialized modular agents with explicit validation loops provide significantly greater analytical reliability than monolithic prompts.'
        }
    },
    'v2c-sentinel': {
        'id': 'v2c-sentinel',
        'title': 'V2C-Sentinel',
        'tag': 'MACHINE LEARNING · CYBERSECURITY · SIMULATION',
        'repo': 'V2C-Sentinel',
        'fr': {
            'subtitle': 'Prototype de recherche · Détection d’intrusions CAN & contraintes 5G',
            'overview': 'Détection d’intrusions CAN (Controller Area Network) en simulation locale : requêtes de confirmation limitées et délais 5G rejoués. Python, régression logistique, forêt aléatoire.',
            'contribution': 'Recherche et développement logiciel : conception de l’architecture à deux niveaux, extraction des caractéristiques temporelles des trames CAN, entraînement des modèles locaux et simulation des distributions de latence 5G.',
            'how_it_works': 'Un premier modèle local léger (régression logistique) surveille les flux CAN en temps réel avec une latence quasi nulle. En cas d’anomalie suspectée et si le budget de requêtes le permet, une trame est transmise à un modèle de confirmation plus lourd (Random Forest) via une simulation de latence 5G rejouée.',
            'decisions': 'Adopter une approche hiérarchique pour concilier rapidité de réaction locale et économie de bande passante, plutôt que d’envoyer chaque trame dans le cloud ou de surcharger le microcontrôleur embarqué.',
            'evaluation': 'Simulation logicielle sur des enregistrements réels de trames CAN normales et injectées d’attaques. Mesure de la réduction des fausses alertes et du respect du quota de communication selon différents budgets imposés.',
            'limitations': 'Étude de cas réalisée par simulation logicielle locale. Aucun véhicule physique ni antenne 5G réelle n’a été utilisé ; les délais sont issus de distributions statistiques mesurées.',
            'lessons': 'La sécurité automobile exige d’évaluer conjointement les métriques de machine learning (F1-score) et les contraintes cyber-physiques (délai de réaction, bande passante disponible).'
        },
        'en': {
            'subtitle': 'Research prototype · CAN intrusion detection under 5G constraints',
            'overview': 'CAN (Controller Area Network) intrusion detection under local simulation: constrained confirmation requests and replayed 5G delays. Python, logistic regression, random forest.',
            'contribution': 'Research and software development: dual-tier architecture design, CAN frame feature extraction, training detection classifiers, and simulating 5G delay distributions.',
            'how_it_works': 'A lightweight local warning model (logistic regression) inspects CAN frames in real time with near-zero latency. If an anomaly is flagged and the request budget allows, the sequence is forwarded to a deeper confirmation model (random forest) through replayed 5G latency distributions.',
            'decisions': 'Adopted a hierarchical tier to balance immediate on-vehicle reaction with constrained cloud bandwidth, rather than saturating the network or vehicle ECU.',
            'evaluation': 'Simulated across CAN logs containing normal traffic and injected attack patterns, quantifying false-alarm mitigation under varying query quotas.',
            'limitations': 'Simulation-based study using recorded data and replayed network latency. Does not reflect hardware-in-the-loop vehicle deployment.',
            'lessons': 'Automotive cybersecurity requires balancing classical ML metrics (accuracy, F1-score) with cyber-physical constraints such as ECU compute budgets and transmission latency.'
        }
    }
}

# Modals for all projects (including Tadbir AI & Churn)
all_case_studies = {
    **case_studies,
    'tadbir-ai': {
        'id': 'tadbir-ai',
        'title': 'Tadbir AI',
        'tag': 'AI-assisted business software · Internship project',
        'repo': None,
        'fr': {
            'subtitle': 'Logiciel de gestion métier assisté par l’IA · Projet de stage',
            'overview': 'Tadbir AI est une plateforme web intégrée conçue pour centraliser et automatiser les processus administratifs essentiels d’une entreprise : facturation, suivi client, gestion des stocks et reporting analytique. Le système vise à réduire la saisie manuelle et les erreurs humaines en intégrant l’intelligence artificielle dans les flux documentaires quotidiens.',
            'contribution': 'Stagiaire en ingénierie IA / logicielle et team leader au sein de l’équipe de développement. J’ai coordonné les points techniques de l’équipe, participé à la structuration du backend Django REST, et pris en charge l’intégration de l’extraction automatique de champs par l’API Gemini ainsi que la logique de validation des données importées depuis des feuilles de calcul.',
            'how_it_works': 'Le flux combine un frontend Next.js/TypeScript et une API Django REST. Lorsqu’un document (facture, reçu) est importé, un appel structuré extrait les champs clés (montants, dates, identifiants). Ces données passent par un module de vérification de cohérence métier avant d’être soumises à une interface de revue humaine (human-in-the-loop) qui valide l’enregistrement dans la base de données.',
            'decisions': 'Choix d’une approche hybride "IA + validation humaine" plutôt qu’une automatisation opaque à 100%, garantissant la conformité comptable. Utilisation de Django REST pour la robustesse du modèle relationnel et d’un typage strict en TypeScript sur le frontend.',
            'evaluation': 'Tests fonctionnels menés sur des jeux de factures et tableaux types. L’extraction a permis de pré-remplir les formulaires en réduisant significativement le temps de saisie, tandis que la validation humaine a systématiquement intercepté les ambiguïtés de mise en page.',
            'limitations': 'La précision dépend fortement de la qualité de numérisation des documents d’entrée. Les documents manuscrits ou très dégradés nécessitent une correction manuelle complète.',
            'lessons': 'L’importance de concevoir des interfaces d’édition simples pour les corrections humaines : un modèle d’IA n’a de valeur pratique en entreprise que si ses incertitudes sont faciles à inspecter et corriger par les utilisateurs.'
        },
        'en': {
            'subtitle': 'AI-assisted business software · Internship project',
            'overview': 'Tadbir AI is an integrated business management platform developed to centralize and automate core administrative operations: invoicing, customer tracking, inventory and reporting. The goal was to reduce manual entry bottlenecks by embedding AI into everyday document workflows.',
            'contribution': 'Team Leader and AI / Software Engineering Intern within the development team. I coordinated technical tasks, contributed to the Django REST backend, and spearheaded document-field extraction using Gemini alongside spreadsheet validation workflows.',
            'how_it_works': 'The architecture pairs a Next.js/TypeScript client with a Django REST API. When an invoice or spreadsheet is uploaded, structured extraction parses key attributes (totals, line items, dates). Data passes through schema validation rules before surfacing in a human-in-the-loop review UI for final confirmation.',
            'decisions': 'Selected a human-in-the-loop paradigm over fully autonomous processing to maintain accounting precision. Chose Django REST for relational integrity and TypeScript for interface reliability.',
            'evaluation': 'Functional testing across standardized invoice layouts demonstrated substantial time savings in form completion, with human review catching irregular formatting edge cases.',
            'limitations': 'Extraction fidelity varies on low-resolution scans. Handwritten or highly unstructured documents require full manual entry.',
            'lessons': 'Designing frictionless fallback interfaces is just as vital as model accuracy: AI delivers business value only when review workflows are intuitive.'
        }
    },
    'churn-mlops': {
        'id': 'churn-mlops',
        'title': 'Customer Churn · MLOps',
        'tag': 'Machine learning · APIs · Experiment tracking',
        'repo': 'churn-prediction-mlops',
        'fr': {
            'subtitle': 'Pipeline de machine learning · APIs · Suivi d’expériences',
            'overview': 'Ce projet dépasse le cadre du notebook isolé pour construire un pipeline complet d’ingénierie machine learning autour du jeu de données IBM Telco Customer Churn, visant à identifier les clients à risque d’attrition.',
            'contribution': 'Projet individuel mené de bout en bout : exploration des données, ingénierie des variables, entraînement et comparaison de modèles, suivi avec MLflow, conteneurisation Docker et mise en place de tests statistiques de dérive.',
            'how_it_works': 'Le pipeline s’appuie sur DVC pour versionner les données et les étapes. MLflow enregistre les hyperparamètres, métriques et artefacts de modèle. Le meilleur modèle est packagé dans une image Docker servant une API REST FastAPI (/predict). Un script de monitoring calcule les tests Kolmogorov-Smirnov (KS) et le Population Stability Index (PSI) sur les données entrantes.',
            'decisions': 'Choix de Scikit-learn pour la transparence des métriques et la rapidité d’inférence. Priorisation du rappel (recall) sur la précision pour maximiser la détection des départs clients, tout en contrôlant le coût des faux positifs.',
            'evaluation': 'Évaluation sur jeu de test indépendant avec courbes ROC-AUC et matrices de confusion. Les tests KS et PSI simulent des dérives artificielles pour vérifier le déclenchement des alertes de réentraînement.',
            'limitations': 'Exécution et tests réalisés en environnement local conteneurisé. Le déploiement cloud (AWS/GCP) est documenté dans le dépôt mais non maintenu en continu pour des raisons de coût.',
            'lessons': 'Le code de modélisation ne représente qu’une petite fraction du travail en MLOps : la reproductibilité des environnements et la surveillance continue des données sont les véritables garants de la pérennité d’un modèle.'
        },
        'en': {
            'subtitle': 'Machine learning · APIs · Experiment tracking',
            'overview': 'This project moves beyond an isolated notebook to construct an end-to-end MLOps pipeline on the IBM Telco Customer Churn dataset, predicting subscriber attrition risks.',
            'contribution': 'Sole developer: data preparation, feature engineering, model benchmarking, MLflow tracking, Docker containerization, FastAPI endpoint development, and drift monitoring.',
            'how_it_works': 'DVC versions datasets and pipeline stages. MLflow tracks hyperparameters, metrics and the model registry. The selected model is packaged into a Docker container serving FastAPI endpoints. Continuous monitoring scripts compute Kolmogorov-Smirnov (KS) tests and Population Stability Index (PSI) scores to detect distribution drift.',
            'decisions': 'Prioritized recall over precision to catch high-churn risks while managing false-positive intervention costs. Selected FastAPI for lightweight asynchronous inference.',
            'evaluation': 'Benchmarked on a holdout split using ROC-AUC and confusion matrices. Simulated synthetic distribution shifts to confirm drift detection thresholds.',
            'limitations': 'Validated in local Docker execution. Cloud deployment pipelines are documented but not maintained live to avoid idle hosting costs.',
            'lessons': 'Model training code is only a fraction of the real-world challenge; reproducible environments, clean pipelines, and drift detection ensure true operational reliability.'
        }
    }
}

# The 7 additional projects in section 4 (including Tadbir AI and Customer Churn)
more_projects = [
    dict(
        name='Tadbir AI',
        cat='software',
        tag='AI & BUSINESS SOFTWARE · INTERNSHIP',
        repo=None,
        stack=['Python', 'Django REST', 'Next.js', 'TypeScript', 'Gemini'],
        fr=(
            'Logiciel de gestion métier assisté par l’IA',
            'Automatisation des flux administratifs et facturation.',
            'Une plateforme collaborative développée chez Arimas Holdings réunissant facturation, suivi client, gestion des stocks et reporting, avec extraction documentaire assistée par IA et import de tableurs.',
            'Rôle de Team Leader et ingénieure stagiaire : API Django REST, validation de schémas et intégration Gemini.',
            'Projet d’équipe réalisé en stage chez Arimas Holdings (juillet–septembre 2026).'
        ),
        en=(
            'AI-assisted business software',
            'Streamlining administrative workflows and invoicing.',
            'A collaborative business-management platform developed during my internship at Arimas Holdings bringing together invoicing, customer management, inventory and reporting, with AI document extraction and spreadsheet imports.',
            'Team Leader & Engineering Intern: Django REST APIs, schema validation and Gemini orchestration.',
            'Team project delivered during internship at Arimas Holdings (July–September 2026).'
        )
    ),
    dict(
        name='Customer Churn · MLOps',
        cat='ml',
        tag='MACHINE LEARNING · APIS · EXPERIMENT TRACKING',
        repo='churn-prediction-mlops',
        stack=['Python', 'Scikit-learn', 'DVC', 'MLflow', 'FastAPI', 'Docker'],
        fr=(
            'Pipeline machine learning & MLOps',
            'De la préparation de données à la détection de dérive.',
            'Un pipeline complet autour du jeu Telco Churn : versioning DVC, suivi des expérimentations MLflow, API d’inférence FastAPI sous Docker et monitoring de distribution avec tests KS et PSI.',
            'Reproductibilité complète, conteneurisation Docker et tests statistiques de dérive.',
            'Projet individuel avec exécution locale documentée et pipeline de réentraînement.'
        ),
        en=(
            'Machine learning & MLOps pipeline',
            'From data preparation to drift monitoring.',
            'An end-to-end churn prediction pipeline using the Telco dataset: DVC versioning, MLflow tracking, Dockerized FastAPI inference endpoint, and KS/PSI distribution monitoring.',
            'Full pipeline reproducibility, Docker containerization and statistical drift detection.',
            'Personal project with documented local execution and automated retraining criteria.'
        )
    ),
    dict(
        name='Pricing Analytics Engine',
        cat='data',
        tag='SQL · ANALYTICS · FORECASTING',
        repo='pricing-analytics-engine',
        stack=['Python', 'DuckDB', 'SQL', 'FastAPI', 'Prophet', 'Chart.js'],
        fr=(
            'Analytics e-commerce',
            'De 1M+ transactions à des analyses décisionnelles.',
            'Une application analytique construite autour du jeu public Online Retail II (>1 million de transactions). Elle explore la segmentation RFM, la classification ABC-XYZ, les prévisions de revenus avec Prophet et les corrélations prix-demande dans un tableau de bord web interactif.',
            'Segmentation vectorisée avec DuckDB, API FastAPI et visualisation Chart.js.',
            'Projet analytique d’exploration. La corrélation prix-demande est observationnelle et ne démontre pas une élasticité causale ni un gain commercial réel.'
        ),
        en=(
            'E-commerce analytics',
            'From 1M+ transactions to business intelligence.',
            'An e-commerce analytics application built using the public Online Retail II dataset (>1 million transactions). It explores customer RFM segmentation, product classification, revenue forecasting with Prophet, and price-demand relationships in an interactive dashboard.',
            'Vectorized segmentation with DuckDB, FastAPI backend and Chart.js visualization.',
            'Exploratory analytics project. Price-demand correlation is observational and does not claim causal elasticity or commercial gains.'
        )
    ),
    dict(
        name='Supply Chain Optimisation',
        cat='data',
        tag='OPERATIONS RESEARCH · SIMULATION',
        repo='supply-chain-optimization-dashboard',
        stack=['Python', 'PuLP', 'Streamlit', 'Plotly'],
        fr=(
            'Recherche opérationnelle',
            'Aide à la décision logistique sous contraintes.',
            'Un tableau de bord interactif pour explorer des scénarios d’approvisionnement et d’allocation de ressources. Formulation en programmation linéaire, optimisation multi-objectifs, modélisation de l’incertitude, simulation de Monte-Carlo et analyses de sensibilité.',
            'Programmation mathématique PuLP et visualisations interactives Plotly/Streamlit.',
            'Étude de cas par simulation : les scénarios modélisent des compromis mathématiques et ne représentent pas des économies mesurées chez un client.'
        ),
        en=(
            'Operations research',
            'Decision-support dashboard under operational constraints.',
            'An interactive dashboard for exploring procurement and resource allocation decisions under constraints, using linear programming, multi-objective trade-offs, Monte Carlo simulation, and sensitivity analysis.',
            'Mathematical optimization using PuLP with Plotly and Streamlit interactive interfaces.',
            'Simulation-based study: scenarios explore constraint boundaries rather than verified commercial savings.'
        )
    ),
    dict(
        name='Traffic Flow Prediction',
        cat='ml',
        tag='PREDICTIVE MODELLING · VISUALISATION',
        repo='Mini_project-TrafficFlowPrediction-',
        stack=['Python', 'Scikit-learn', 'SVR', 'KNN', 'JavaScript'],
        fr=(
            'Modélisation prédictive',
            'Anticiper les flux de circulation urbains.',
            'Un projet associant préparation de séries temporelles, ingénierie de variables temporelles, comparaison méthodique de modèles (SVR, KNN, arbres de décision, régression multiple) et tableau de bord de visualisation web.',
            'Nettoyage de données, métriques d’erreur (MAE, RMSE, R²) et graphiques web.',
            'Projet académique documenté dans le dépôt GitHub ; évalué sur données historiques sans déploiement urbain réel.'
        ),
        en=(
            'Predictive modelling',
            'Forecasting urban traffic congestion patterns.',
            'A traffic-prediction project combining time-series preparation, feature engineering, and systematic benchmarking of SVR, KNN, decision trees, and multiple regression with interactive web charts.',
            'Data cleaning, metric evaluation (MAE, RMSE, R²) and web visualization.',
            'Documented academic project evaluated against historical benchmark data; no live municipal deployment is claimed.'
        )
    ),
    dict(
        name='Computer Vision Gesture Suite',
        cat='ml',
        tag='COMPUTER VISION · INTERACTION',
        repo='hand-detection-program',
        stack=['OpenCV', 'MediaPipe', 'Python', 'NumPy'],
        fr=(
            'Vision par ordinateur',
            'Transformer le mouvement des mains en interactions naturelles.',
            'Une suite de démonstrations utilisant un flux webcam standard et le suivi des points de repère anatomiques de la main (MediaPipe) : dessin gestuel dans l’espace (air-writing), manipulation d’éléments et redimensionnement par pincement.',
            'Traitement temps réel OpenCV, détection 21 points de repère MediaPipe.',
            'Démonstrations locales temps réel ; la réactivité dépend des conditions d’éclairage et de la résolution caméra.'
        ),
        en=(
            'Computer vision',
            'Turning hand movements into touchless interactions.',
            'Webcam-based demonstrations that turn hand movements into natural user interactions using MediaPipe landmark tracking: air writing, gesture-controlled drawing, and pinch-based resizing.',
            'Real-time OpenCV processing with 21-point MediaPipe hand tracking.',
            'Local interactive demonstrations; performance depends on camera resolution and lighting conditions.'
        )
    ),
    dict(
        name='Contact Manager',
        cat='software',
        tag='FULL-STACK · AI INTEGRATION',
        repo='Gestion-des-contacts',
        stack=['Flask', 'SQLite', 'Jinja2', 'Gemini'],
        fr=(
            'Développement full-stack',
            'Gestion d’annuaire complet avec assistant IA.',
            'Une application web complète comprenant authentification utilisateur, recherche avancée, gestion de catégories, favoris, agenda, assistant conversationnel Gemini, notifications par e-mail et export CSV.',
            'Architecture Flask MVC, base relationnelle SQLite, intégration API Gemini.',
            'Application de démonstration illustrant la maîtrise d’une architecture web complète de bout en bout.'
        ),
        en=(
            'Full-stack development',
            'Contact management system with integrated AI assistant.',
            'A complete web platform featuring user authentication, advanced search, categories, favorites, agenda, an integrated Gemini AI assistant, email alerts, and CSV export.',
            'Flask MVC architecture, SQLite relational schema, Gemini API integration.',
            'Demonstration application showcasing full-cycle web engineering and third-party API orchestration.'
        )
    ),
]

# Section 7: Project Journal Notes matching the featured projects
journal_notes = [
    {
        'id': 'researchos-rag',
        'fr_title': 'RAG & pgvector : sourçage strict et réduction des hallucinations',
        'en_title': 'RAG with pgvector: strict sourcing and hallucination mitigation',
        'tag': 'RAG & VECTOR SEARCH',
        'date': '2026',
        'fr_desc': 'Comment structurer l’indexation vectorielle dans PostgreSQL avec pgvector et contraindre les réponses du modèle génératif à des citations documentaires vérifiables.',
        'en_desc': 'Structuring vector indexing in PostgreSQL with pgvector and strictly grounding generative model responses in verifiable document citations.',
        'link': '#project-case-researchos'
    },
    {
        'id': 'multi-agent-langgraph',
        'fr_title': 'Orchestrer 6 agents autonomes avec LangGraph, DuckDB et Polars',
        'en_title': 'Orchestrating 6 autonomous agents with LangGraph, DuckDB and Polars',
        'tag': 'MULTI-AGENTS & ANALYTICS',
        'date': '2026',
        'fr_desc': 'Architecture d’un graphe d’états à 6 agents pour l’analyse de données : division des responsabilités, boucle d’audit croisée et exécution analytique en mémoire.',
        'en_desc': 'Designing a 6-agent state graph for automated analytics: role decomposition, mutual critique loops, and fast in-memory execution with DuckDB and Polars.',
        'link': '#project-case-analyste-ia'
    },
    {
        'id': 'v2c-tradeoffs',
        'fr_title': 'Compromis entre détection et communication dans V2C-Sentinel',
        'en_title': 'Detection and communication trade-offs in V2C-Sentinel',
        'tag': 'CYBERSECURITY & SIMULATION',
        'date': '2026',
        'fr_desc': 'Quand la bande passante 5G est comptée : arbitrer mathématiquement entre le risque de faux négatifs locaux et l’épuisement du quota de requêtes vers le cloud.',
        'en_desc': 'When 5G bandwidth is constrained: balancing local false-negative risks against cloud request quotas under variable latency distributions.',
        'link': '#project-case-v2c-sentinel'
    },
    {
        'id': 'tadbir-collaboration',
        'fr_title': 'Retours d’expérience et collaboration sur Tadbir AI',
        'en_title': 'Lessons from collaborating on Tadbir AI',
        'tag': 'LEADERSHIP & ENGINEERING',
        'date': '2026',
        'fr_desc': 'Coordonner une équipe de stagiaires autour d’un produit SaaS : standardisation des interfaces TypeScript/Django et conception de revues humaines pour l’IA.',
        'en_desc': 'Leading an intern development team on business SaaS: standardizing TypeScript/Django API contracts and designing human-in-the-loop review interfaces.',
        'link': '#project-1'
    },
    {
        'id': 'churn-to-api',
        'fr_title': 'Du modèle de churn à l’API de prédiction et surveillance de dérive',
        'en_title': 'From a churn model to a prediction API and drift monitoring',
        'tag': 'MLOPS & DEPLOYMENT',
        'date': '2026',
        'fr_desc': 'Pourquoi un notebook ne suffit pas : structurer l’inférence avec FastAPI, gérer la sérialisation des pipelines et surveiller la dérive avec KS et PSI.',
        'en_desc': 'Why a notebook is only the first step: packaging inference endpoints with FastAPI, managing pipeline artifacts, and tracking drift with KS and PSI.',
        'link': '#project-2'
    }
]'''

# Replace from `# Detailed case studies data matching structure 11` up to `def bi(fr_val, en_val):`
start_marker = "# Detailed case studies data matching structure 11"
end_marker = "def bi(fr_val, en_val):"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error: markers not found (start: {start_idx}, end: {end_idx})")
    exit(1)

updated_content = content[:start_idx] + new_case_studies + "\n\n" + content[end_idx:]

# Also ensure modals loop over all_case_studies:
updated_content = updated_content.replace(
    "for key, p in case_studies.items():\n        modals_html +=",
    "for key, p in all_case_studies.items():\n        modals_html +="
)

# Also update stat count from 08 to 10
updated_content = updated_content.replace(
    '<span class="stat-num">08</span>',
    '<span class="stat-num">10</span>'
)

# And update Section 2 heading description to mention ResearchOS & multi-agents:
updated_content = updated_content.replace(
    'Tadbir AI, Customer Churn MLOps et V2C-Sentinel : explorez les décisions d\'architecture',
    'ResearchOS, Analyste IA multi-agents et V2C-Sentinel : explorez les décisions d\'architecture'
)
updated_content = updated_content.replace(
    'Tadbir AI, Customer Churn MLOps and V2C-Sentinel: explore the architectural choices',
    'ResearchOS, Multi-Agent AI Analyst and V2C-Sentinel: explore the architectural choices'
)

file_path.write_text(updated_content, encoding="utf-8")
print("generate_unified_site.py updated successfully!")
