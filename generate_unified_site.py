"""
Complete Portfolio Generator for Meryem El Osmani
Featuring ONLY her latest, genuine production and research GitHub projects:
1. BidPilot AI (bidpilot-ai)
2. ResearchOS (research-os)
3. Analyste IA multi-agents (autonomous-ai-data-analyst)
4. V2C-Sentinel (V2C-Sentinel)
5. FlowDesk AI (flowdesk-ai)
6. Tadbir AI (FAWATIR-ROOT)
7. Customer Churn · MLOps (churn-prediction-mlops)
8. Pricing Analytics Engine (pricing-analytics-engine)
9. Supply Chain Optimisation (supply-chain-optimization-dashboard)

Aesthetic: Dark & precise AI research & software engineering (graphite, off-white, restrained electric-blue).
Bilingual: Instant FR / EN switching via header button.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
GH = 'https://github.com/MERYEMELOSMANI/'

# 4 Featured In-Depth Spotlight Case Studies
case_studies = {
    'bidpilot-ai': {
        'id': 'bidpilot-ai',
        'title': 'BidPilot AI',
        'tag': 'AIDE À LA DÉCISION · NLP & GOOGLE OR-TOOLS CP-SAT',
        'repo': 'bidpilot-ai',
        'fr': {
            'subtitle': 'Système d’aide à la décision pour les achats · Optimisation CP-SAT & Matching NLP',
            'overview': 'Application d’aide à la décision pour les appels d’offres (RFQ) combinant le matching sémantique par embeddings NLP (Sentence-Transformers) et l’optimisation mathématique discrète exacte avec Google OR-Tools CP-SAT pour minimiser le coût d’achat total sous contraintes de délais, capacités fournisseurs et quantités minimales (MOQ).',
            'contribution': 'Architecture logicielle et modélisation mathématique complète : pipeline de vectorisation et réconciliation sémantique des devis fournisseurs non standardisés, formulation du programme d’optimisation discrète avec Google OR-Tools CP-SAT et détection d’infaisabilité, API asynchrone FastAPI et tableau de bord Next.js / TypeScript.',
            'how_it_works': 'Les lignes de devis fournisseurs bruts sont transformées en embeddings vectoriels et associées aux lignes de la demande d’achat par similarité cosinus avec seuil de confiance et arbitrage humain. Le solveur CP-SAT prend les correspondances validées et résout un programme d’optimisation discrète pour déterminer les volumes exacts alloués à chaque fournisseur tout en respectant les MOQ, capacités maximales et fenêtres de livraison.',
            'decisions': 'Sélection du solveur Google OR-Tools CP-SAT (Constraint Programming over Finite Domains) plutôt qu’un solveur MIP linéaire classique afin de modéliser nativement les contraintes logiques disjonctives (coûts fixes d’activation de fournisseur, MOQ discontinues). Utilisation d’embeddings locaux pour une latence d’inférence maîtrisée.',
            'evaluation': 'Benchmark sur des scénarios de simulation d’achats industriels : comparaison des coûts optimisés par rapport à une allocation gloutonne baseline, validation de la détection d’infaisabilité budgétaire et tests de sensibilité aux variations de prix fournisseurs.',
            'limitations': 'Prototype de recherche et d’ingénierie évalué sur des données synthétiques contrôlées. Ne comprend pas de connecteur direct vers un progiciel ERP en production (SAP/Oracle).',
            'lessons': 'Dans les systèmes d’aide à la décision critique, la transparence algorithmique et l’explication des causes d’infaisabilité sont tout aussi essentielles aux décideurs que la valeur de la fonction objectif.'
        },
        'en': {
            'subtitle': 'Enterprise Procurement Decision Support · CP-SAT Optimization & NLP Matching',
            'overview': 'Enterprise decision-support application for industrial RFQ quotations coupling NLP semantic embeddings with exact discrete mathematical optimization (Google OR-Tools CP-SAT) to minimize procurement spend under delivery deadlines, supplier capacities, and minimum order quantities (MOQs).',
            'contribution': 'Full-stack software architecture and mathematical modeling: NLP semantic matching pipeline reconciling non-standard supplier quotations, discrete CP-SAT formulation with infeasibility diagnostics in Google OR-Tools, asynchronous FastAPI backend, and Next.js / TypeScript dashboard.',
            'how_it_works': 'Unstructured supplier quotation lines are embedded and matched against RFQ specifications using cosine similarity with confidence thresholds and manual override capability. The CP-SAT solver ingests verified pairings and solves a discrete constraint programming model to allocate quantities across suppliers, strictly respecting MOQs, volume caps, and delivery schedules.',
            'decisions': 'Selected Google OR-Tools CP-SAT solver over standard linear MIP solvers to natively model disjunctive logic constraints (supplier activation fixed costs, discontinuous minimum order quantities) without heuristic relaxation.',
            'evaluation': 'Benchmarked across industrial procurement simulation scenarios: quantified cost reductions against greedy baseline allocations, rigorously verified infeasibility detection under tight budget caps, and performed parameter sensitivity tests.',
            'limitations': 'Local portfolio prototype operating on synthetic RFQ data. Multi-user authentication and hardened cloud deployment are outside the demonstration scope.',
            'lessons': 'In mission-critical decision support, algorithmic interpretability and actionable infeasibility diagnostics matter just as much to stakeholders as raw cost minimization.'
        }
    },
    'researchos': {
        'id': 'researchos',
        'title': 'ResearchOS',
        'tag': 'RAG · RECHERCHE DOCUMENTAIRE · PGVECTOR',
        'repo': 'research-os',
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
        'repo': 'autonomous-ai-data-analyst',
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

# Modals for all 9 genuine GitHub projects
all_case_studies = {
    **case_studies,
    'flowdesk-ai': {
        'id': 'flowdesk-ai',
        'title': 'FlowDesk AI',
        'tag': 'SERVICE MANAGEMENT · ML & GOOGLE OR-TOOLS CP-SAT',
        'repo': 'flowdesk-ai',
        'fr': {
            'subtitle': 'Plateforme de gestion de services & Planification · Classification ML & Optimisation CP-SAT',
            'overview': 'Plateforme intelligente de gestion de services d’entreprise (ITSM) associant la classification automatique de tickets par machine learning (TF-IDF + Régression Logistique avec Scikit-learn) et la planification mathématique optimale des équipes avec Google OR-Tools CP-SAT selon les compétences, disponibilités et délais SLA.',
            'contribution': 'Conception et développement complet : entraînement et validation du modèle de classification NLP de tickets, formulation mathématique du problème d’affectation sous Google OR-Tools CP-SAT avec équilibrage de charge, API FastAPI asynchrone et interface moderne Next.js / TypeScript.',
            'how_it_works': 'Chaque ticket entrant est analysé par un pipeline TF-IDF + Régression Logistique qui prédit sa catégorie et son niveau d’urgence avec un score de confiance étalonné. Le moteur d’optimisation OR-Tools CP-SAT affecte les tickets du backlog aux intervenants qualifiés et disponibles, en maximisant le respect des délais SLA et en équilibrant la charge hebdomadaire.',
            'decisions': 'Choix d’un modèle ML transparent et ultra-rapide (<10 ms) avec Scikit-learn pour la catégorisation sans dépendance cloud coûteuse, couplé à un solveur de satisfaction de contraintes CP-SAT pour garantir formellement l’adéquation compétences-tâches et l’équité de charge.',
            'evaluation': 'Évaluation des métriques de classification (Accuracy, F1-score macro) sur jeux de test et tests de robustesse du solveur CP-SAT face à des pics d’arrivée de tickets sous contraintes d’indisponibilité d’agents.',
            'limitations': 'Évalué sur des jeux de données d’incidents synthétiques réalistes pour la démonstration. L’intégration avec des annuaires d’entreprise LDAP/Okta n’est pas implémentée dans ce prototype.',
            'lessons': 'La synergie entre modélisation statistique (machine learning probabiliste) et recherche opérationnelle (optimisation exacte déterministe) permet d’automatiser des flux opérationnels complexes tout en conservant une garantie formelle de faisabilité.'
        },
        'en': {
            'subtitle': 'Enterprise Service Management & Scheduling · ML Classification & CP-SAT Optimization',
            'overview': 'Intelligent enterprise service-management (ITSM) platform coupling machine learning text classification (Scikit-learn TF-IDF + Logistic Regression) with exact discrete optimization (Google OR-Tools CP-SAT) to categorize support tickets and solve technician shift assignment under skills, availability, and SLA deadlines.',
            'contribution': 'End-to-end design and software development: training and evaluating the ticket classification NLP model, mathematical formulation of technician assignment under Google OR-Tools CP-SAT with workload balancing, asynchronous FastAPI backend, and Next.js / TypeScript interface.',
            'how_it_works': 'Incoming service requests are processed by a TF-IDF + Logistic Regression pipeline that infers category and urgency with calibrated confidence scores. The OR-Tools CP-SAT engine then assigns backlog tickets to qualified, available agents, optimizing SLA compliance and balancing weekly workload distributions.',
            'decisions': 'Chose a lightweight, interpretable Scikit-learn ML pipeline for ultra-fast (<10ms) local inference, coupled with CP-SAT constraint programming to formally guarantee skill alignment and strict workload limits.',
            'evaluation': 'Evaluated text categorization metrics (Accuracy, macro F1-score) across test splits and benchmarked CP-SAT solver responsiveness during ticket surges and sudden technician unavailability.',
            'limitations': 'Evaluated on synthetic ITSM incident logs for demonstration. Enterprise identity integration (LDAP/Okta SSO) is outside the prototype scope.',
            'lessons': 'Combining probabilistic machine learning with deterministic operations research provides reliable automation with formal feasibility guarantees.'
        }
    },
    'tadbir-ai': {
        'id': 'tadbir-ai',
        'title': 'Tadbir AI',
        'tag': 'AI & BUSINESS SOFTWARE · INTERNSHIP',
        'repo': 'FAWATIR-ROOT',
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
        'tag': 'MACHINE LEARNING · MLOPS · DRIFT MONITORING',
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
    },
    'pricing-engine': {
        'id': 'pricing-engine',
        'title': 'Pricing Analytics Engine',
        'tag': 'SQL · ANALYTICS · FORECASTING',
        'repo': 'pricing-analytics-engine',
        'fr': {
            'subtitle': 'Intelligence de tarification e-commerce sur 1M+ transactions · DuckDB & Prophet',
            'overview': 'Application analytique construite autour du jeu public Online Retail II (>1 million de transactions). Elle explore la segmentation RFM, la classification ABC-XYZ, les prévisions de revenus avec Prophet et les corrélations prix-demande dans un tableau de bord web interactif.',
            'contribution': 'Conception et développement complet : requêtes analytiques vectorisées sous DuckDB pour le calcul de métriques sur 1M+ lignes en millisecondes, API FastAPI et visualisations dynamiques Chart.js.',
            'how_it_works': 'DuckDB exécute les calculs de cohortes, de valeur client (CLV) et de segmentation RFM directement en mémoire. Les séries temporelles de ventes sont agrégées pour alimenter un modèle de prévision Prophet, tandis que l’élasticité prix-demande est explorée par modélisation statistique.',
            'decisions': 'Utilisation de DuckDB comme moteur analytique in-process pour éliminer la latence d’une base de données externe tout en offrant des performances SQL analytiques de pointe sur des millions d’enregistrements.',
            'evaluation': 'Validation de la vitesse d’exécution SQL (requêtes sous les 80ms sur 1M+ transactions) et contrôle de la cohérence statistique des clusters clients.',
            'limitations': 'Les corrélations observées entre prix et demande sont empiriques et ne constituent pas une démonstration de causalité commerciale.',
            'lessons': 'L’optimisation des calculs au niveau du moteur analytique (colonnes vectorisées) est indispensable pour garantir une fluidité parfaite sur des volumes de transactions importants.'
        },
        'en': {
            'subtitle': 'E-Commerce Pricing Intelligence on 1M+ Transactions · DuckDB & Prophet',
            'overview': 'Analytical application built on the Online Retail II dataset (>1 million transactions). It integrates RFM customer segmentation, ABC-XYZ inventory classification, Prophet revenue forecasting, and price-demand correlation analysis in an interactive dashboard.',
            'contribution': 'Full-stack development: authored vectorized analytical queries in DuckDB processing 1M+ records in milliseconds, FastAPI backend, and Chart.js dynamic visualizations.',
            'how_it_works': 'DuckDB executes cohort analysis, customer lifetime value (CLV), and RFM segmentation directly in memory. Aggregated transaction time series feed into Prophet forecasting models while price-demand relationships are modeled statistically.',
            'decisions': 'Selected DuckDB as an embedded analytical engine to avoid database overhead while delivering sub-80ms analytical query speeds on over a million records.',
            'evaluation': 'Benchmarked query performance (<80ms response time on 1M+ rows) and verified statistical consistency across customer segmentation clusters.',
            'limitations': 'Price-demand correlations are observational and do not demonstrate causal commercial elasticity.',
            'lessons': 'Vectorized columnar query design is the single most effective lever for delivering real-time analytical exploration over high-volume transactional data.'
        }
    },
    'supply-chain': {
        'id': 'supply-chain',
        'title': 'Supply Chain Optimisation',
        'tag': 'OPERATIONS RESEARCH · SIMULATION',
        'repo': 'supply-chain-optimization-dashboard',
        'fr': {
            'subtitle': 'Aide à la décision logistique sous contraintes · Programmation linéaire PuLP & Monte-Carlo',
            'overview': 'Tableau de bord interactif pour explorer des scénarios d’approvisionnement et d’allocation de ressources. Formulation en programmation linéaire, optimisation multi-objectifs, modélisation de l’incertitude par simulation de Monte-Carlo et analyses de sensibilité.',
            'contribution': 'Formulation mathématique complète du problème d’allocation sous contraintes de capacités d’entrepôts et de coûts de transport avec PuLP, génération de distributions stochastiques et interface interactive Streamlit / Plotly.',
            'how_it_works': 'L’utilisateur configure les capacités logistiques, demandes clients et coûts unitaires. Le solveur de programmation linéaire résout le problème de transport optimal. Un module de simulation de Monte-Carlo évalue la robustesse de la chaîne logistique face aux aléas de demande.',
            'decisions': 'Utilisation de PuLP pour une formulation mathématique claire et portable, associée à des graphiques interactifs Plotly pour rendre les surfaces de compromis immédiatement compréhensibles.',
            'evaluation': 'Simulation de scénarios de rupture de stock et analyse de sensibilité sur les capacités d’approvisionnement.',
            'limitations': 'Modèle de simulation à vocation méthodologique et pédagogique, fondé sur des paramètres synthétiques.',
            'lessons': 'La programmation linéaire doit toujours être complétée par des analyses de robustesse face à l’incertitude pour être exploitable en environnement réel.'
        },
        'en': {
            'subtitle': 'Logistics Decision Support under Constraints · PuLP Linear Programming & Monte Carlo',
            'overview': 'Interactive decision-support dashboard for exploring procurement and resource allocation scenarios under operational constraints, using linear programming, multi-objective trade-offs, Monte Carlo simulation, and sensitivity analysis.',
            'contribution': 'Complete mathematical formulation of warehouse allocation and transportation cost minimization using PuLP, stochastic simulation distributions, and interactive Streamlit / Plotly UI.',
            'how_it_works': 'Users define supplier capacities, regional demands, and transport costs. The linear solver identifies optimal routing. A Monte Carlo module samples demand fluctuations to quantify supply chain resilience under stochastic shocks.',
            'decisions': 'Selected PuLP for explicit, readable mathematical constraints and Plotly for intuitive visualization of multi-variable trade-off surfaces.',
            'evaluation': 'Tested stockout scenarios and sensitivity curves across constrained warehouse capacities.',
            'limitations': 'Simulation-based study using synthetic operational parameters rather than live commercial fleet telemetry.',
            'lessons': 'Deterministic linear programming must be paired with stochastic sensitivity testing to deliver reliable operational decision guidance.'
        }
    }
}

# The 5 additional projects in section 4 (Genuine GitHub repositories only)
more_projects = [
    dict(
        name='FlowDesk AI',
        cat='software',
        modal_id='flowdesk-ai',
        tag='SERVICE MANAGEMENT · ML & OR-TOOLS CP-SAT',
        repo='flowdesk-ai',
        stack=['Python', 'FastAPI', 'Scikit-learn', 'Google OR-Tools', 'Next.js', 'TypeScript'],
        fr=(
            'Gestion des services & Planification',
            'Classification automatique et affectation optimale des effectifs.',
            'Une plateforme ITSM intelligente qui allie classification de tickets par machine learning (TF-IDF + Régression Logistique) et programmation mathématique par contraintes (Google OR-Tools CP-SAT) pour l’affectation d’agents sous contraintes de compétences, disponibilités et SLA.',
            'Classifieur NLP rapide (<10ms), solveur CP-SAT avec équilibrage de charge et API FastAPI.',
            'Prototype d’ingénierie évalué sur données d’incidents synthétiques réalistes avec métriques de classification documentées.'
        ),
        en=(
            'Service management & Workforce scheduling',
            'Automated ticket categorization and optimal staff assignment.',
            'An intelligent ITSM platform coupling machine learning ticket categorization (TF-IDF + Logistic Regression) with exact constraint programming (Google OR-Tools CP-SAT) for staff scheduling under skills, availability, and SLA targets.',
            'Sub-10ms NLP classifier, CP-SAT solver with workload balancing, and asynchronous FastAPI backend.',
            'Engineering prototype evaluated on synthetic incident backlogs with documented classification metrics.'
        )
    ),
    dict(
        name='Tadbir AI',
        cat='software',
        modal_id='tadbir-ai',
        tag='AI & BUSINESS SOFTWARE · INTERNSHIP',
        repo='FAWATIR-ROOT',
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
        modal_id='churn-mlops',
        tag='MACHINE LEARNING · MLOPS · DRIFT MONITORING',
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
        modal_id='pricing-engine',
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
        modal_id='supply-chain',
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
    )
]

# Section 7: Project Journal Notes matching the featured projects
journal_notes = [
    {
        'id': 'bidpilot-opt',
        'fr_title': 'Optimisation discrète avec Google OR-Tools CP-SAT et matching NLP',
        'en_title': 'Discrete optimization with Google OR-Tools CP-SAT and NLP matching',
        'tag': 'OR-TOOLS CP-SAT & NLP',
        'date': '2026',
        'fr_desc': 'Comment modéliser les coûts fixes et seuils MOQ en programmation par contraintes disjonctives tout en réconciliant les devis par similarité vectorielle.',
        'en_desc': 'Modeling fixed supplier costs and MOQ thresholds in disjunctive constraint programming while reconciling RFQ lines with semantic embeddings.',
        'link': '#project-case-bidpilot-ai'
    },
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
        'id': 'flowdesk-scheduling',
        'fr_title': 'FlowDesk AI : Coupler classification Scikit-learn et affectation CP-SAT',
        'en_title': 'FlowDesk AI: Coupling Scikit-learn ML routing with CP-SAT team assignment',
        'tag': 'ML & CONSTRAINT PROGRAMMING',
        'date': '2026',
        'fr_desc': 'Associer la prédiction statistique des catégories de tickets aux contraintes dures de compétences et d’équité de charge hebdomadaire.',
        'en_desc': 'Bridging statistical ticket categorization with hard operational constraints on technician certifications and weekly workload fairness.',
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
        'link': '#project-3'
    }
]

def bi(fr_val, en_val):
    return f'<span class="i18n-fr">{fr_val}</span><span class="i18n-en">{en_val}</span>'

def build_full_html():
    # 1. Navigation items: About · Projects · Experience · Journal · CV · Contact
    nav_links = [
        ('about', 'À propos', 'About'),
        ('selected', 'Sélection', 'Spotlight'),
        ('projects', 'Projets', 'Projects'),
        ('experience', 'Parcours', 'Experience'),
        ('journal', 'Journal', 'Journal'),
        ('cv', 'CV', 'CV'),
        ('contact', 'Contact', 'Contact'),
    ]
    nav_html = ''.join(f'<a href="#{nid}">{bi(fr, en)}</a>' for nid, fr, en in nav_links)

    # 3. Selected Spotlight Case Studies (BidPilot AI, ResearchOS, Analyste IA, V2C-Sentinel)
    selected_html = ''
    for key, p in case_studies.items():
        repo_btn = ''
        if p['repo']:
            repo_btn = f'''
            <a class="source-btn" href="{GH+p['repo']}" target="_blank" rel="noopener noreferrer">
              <svg width="15" height="15" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
              {bi("Voir le code source", "View source code")}
              <span>↗</span>
            </a>
            '''
        
        selected_html += f'''
        <article class="spotlight-card" id="project-case-{p['id']}">
          <div class="spotlight-copy">
            <span class="micro">{p['tag']}</span>
            <h3>{p['title']}</h3>
            <p class="spotlight-sub">{bi(p['fr']['subtitle'], p['en']['subtitle'])}</p>
            <p>{bi(p['fr']['overview'], p['en']['overview'])}</p>
            <div class="spotlight-actions">
              <button type="button" class="project-jump-btn open-case-study" data-case="{p['id']}">
                {bi("Lire l’étude de cas", "Read the case study")}
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
              {repo_btn}
            </div>
          </div>
          <div class="workflow-pipeline">
            <div class="pipeline-header">
              <span class="diagram-label">{bi("CADRE D’INGÉNIERIE", "ENGINEERING SCOPE")}</span>
              <span class="live-badge">{bi("CONTRÔLE & RIGUEUR", "VERIFIED SCOPE")}</span>
            </div>
            <div class="case-brief-box">
              <strong>{bi("Contribution personnelle :", "Individual contribution:")}</strong>
              <p>{bi(p['fr']['contribution'], p['en']['contribution'])}</p>
              <div class="brief-divider"></div>
              <strong>{bi("Choix techniques & compromis :", "Technical decisions & trade-offs:")}</strong>
              <p>{bi(p['fr']['decisions'], p['en']['decisions'])}</p>
            </div>
          </div>
        </article>
        '''

    # 4. More Projects Grid (5 projects)
    more_cards = []
    for i, p in enumerate(more_projects):
        sub_fr, tit_fr, d_fr, app_fr, sc_fr = p['fr']
        sub_en, tit_en, d_en, app_en, sc_en = p['en']
        
        link = ''
        if p['repo']:
            link = f'''
            <a class="source-btn" href="{GH+p['repo']}" target="_blank" rel="noopener noreferrer">
              <svg width="14" height="14" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
              {bi("Voir le dépôt GitHub", "View GitHub repository")}
              <span>↗</span>
            </a>
            '''

        modal_btn = ''
        if p.get('modal_id'):
            modal_btn = f'''
            <button type="button" class="project-jump-btn open-case-study" data-case="{p['modal_id']}">
              {bi("Étude de cas", "Case study")}
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
            '''

        stack_spans = ''.join(f'<span>{t}</span>' for t in p['stack'])

        more_cards.append(f'''
        <article id="project-{i+1}" class="project" data-category="{p['cat']}">
          <div class="project-header">
            <span class="index">{i+1:02}</span>
            <span class="cat-tag">{p['tag']}</span>
          </div>
          <p class="project-context">{bi(sub_fr, sub_en)}</p>
          <h3>{p['name']}</h3>
          <h4>{bi(tit_fr, tit_en)}</h4>
          <p class="project-desc">{bi(d_fr, d_en)}</p>
          <div class="tags">{stack_spans}</div>
          <details>
            <summary>
              <span>{bi("Méthodologie & Périmètre", "Approach & Scope")}</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="detail">
              <div class="detail-box">
                <strong>{bi("Approche technique", "Technical approach")}</strong>
                <p>{bi(app_fr, app_en)}</p>
              </div>
              <div class="detail-box">
                <strong>{bi("Cadre & validation", "Project scope & validation")}</strong>
                <p>{bi(sc_fr, sc_en)}</p>
              </div>
            </div>
          </details>
          <div class="project-actions-row">
            {modal_btn}
            {link}
          </div>
        </article>
        ''')

    # 7. Project Journal Cards
    journal_html = ''
    for note in journal_notes:
        journal_html += f'''
        <article class="journal-card">
          <div class="journal-meta">
            <span class="journal-tag">{note['tag']}</span>
            <time>{note['date']}</time>
          </div>
          <h3>{bi(note['fr_title'], note['en_title'])}</h3>
          <p>{bi(note['fr_desc'], note['en_desc'])}</p>
          <a class="journal-link project-jump" href="{note['link']}">
            {bi("Explorer le projet associé", "Explore associated project")}
            <span aria-hidden="true">→</span>
          </a>
        </article>
        '''

    # Modals for Deep-Dive Structure (All 9 projects)
    modals_html = ''
    for key, p in all_case_studies.items():
        modals_html += f'''
        <div class="case-study-modal" id="modal-{p['id']}" role="dialog" aria-modal="true" aria-labelledby="modal-title-{p['id']}">
          <div class="modal-backdrop close-case-study"></div>
          <div class="modal-dialog">
            <button type="button" class="modal-close-btn close-case-study" aria-label="Fermer / Close">✕</button>
            <div class="modal-content">
              <span class="micro">{p['tag']}</span>
              <h2 id="modal-title-{p['id']}">{p['title']}</h2>
              <p class="modal-sub">{bi(p['fr']['subtitle'], p['en']['subtitle'])}</p>
              
              <div class="deep-dive-grid">
                <div class="deep-dive-section">
                  <h4>1. {bi("Vue d’ensemble (Overview)", "Overview")}</h4>
                  <p>{bi(p['fr']['overview'], p['en']['overview'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>2. {bi("Contribution personnelle (My Contribution)", "My Contribution")}</h4>
                  <p>{bi(p['fr']['contribution'], p['en']['contribution'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>3. {bi("Fonctionnement & Architecture (How It Works)", "How It Works")}</h4>
                  <p>{bi(p['fr']['how_it_works'], p['en']['how_it_works'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>4. {bi("Décisions techniques & Compromis (Technical Decisions)", "Technical Decisions")}</h4>
                  <p>{bi(p['fr']['decisions'], p['en']['decisions'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>5. {bi("Évaluation & Mesures (Evaluation)", "Evaluation")}</h4>
                  <p>{bi(p['fr']['evaluation'], p['en']['evaluation'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>6. {bi("Limites identifiées (Limitations)", "Limitations")}</h4>
                  <p>{bi(p['fr']['limitations'], p['en']['limitations'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>7. {bi("Enseignements tirés (Lessons Learned)", "Lessons Learned")}</h4>
                  <p>{bi(p['fr']['lessons'], p['en']['lessons'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>8. {bi("Explorer le projet & Code source (Explore Further)", "Explore Further")}</h4>
                  <p style="margin-bottom: 12px;">{bi("Accédez au dépôt officiel sur GitHub pour examiner le code source, l’architecture et les instructions d’exécution :", "Explore the official GitHub repository for source code, architecture specifications, and local execution guides:")}</p>
                  <a class="source-btn" href="{GH+p['repo']}" target="_blank" rel="noopener noreferrer" style="display:inline-flex;">
                    <svg width="15" height="15" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    {bi("Ouvrir le dépôt GitHub", "View GitHub repository")}
                    <span>↗</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        '''

    html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Meryem El Osmani — Applied AI · Data · Software | meryemelosmani.site</title>
  <meta name="description" content="Meryem El Osmani. Applied AI, Data and Software engineering portfolio. Seeking a PFE graduation internship in Morocco (Feb/Mar - Jul 2027).">
  <meta name="theme-color" content="#090d14">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='8' fill='%23090d14'/%3E%3Ctext x='7' y='29' font-family='Arial' font-size='27' fill='%2360a5fa'%3EM%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="style.css?v=9">
  <script src="site.js?v=9" defer></script>
</head>
<body>
  <div class="ambient-glow"></div>
  <div class="ambient-glow glow-2"></div>
  
  <a class="skip" href="#projects">{bi("Accéder aux projets", "Skip to projects")}</a>

  <!-- Header Navigation -->
  <header>
    <a class="brand" href="#top">M<span>EO</span><b>.</b><small class="brand-domain">meryemelosmani.site</small></a>
    <nav aria-label="{bi('Navigation principale', 'Main navigation')}">
      {nav_html}
    </nav>
    <div class="header-actions">
      <!-- One Interactive Language Toggle Pill -->
      <div class="lang-switcher" id="langSwitcher" role="group" aria-label="Langue / Language">
        <button type="button" class="lang-btn active" data-lang="fr" id="btn-fr" aria-pressed="true" title="Passer en français">FR</button>
        <button type="button" class="lang-btn" data-lang="en" id="btn-en" aria-pressed="false" title="Switch to English">EN</button>
      </div>
      <a class="mini-button" id="headerCvBtn" href="Meryem_El_Osmani_CV_FR.pdf" download>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        CV
      </a>
    </div>
  </header>

  <main id="top">
    <!-- 1. Homepage Introduction (Hero) -->
    <section class="hero">
      <div class="status-pill">
        <span class="pulse-beacon"></span>
        <span class="status-text">{bi("RECHERCHE STAGE PFE · FÉVRIER / MARS — JUILLET 2027 · MAROC", "SEEKING A PFE INTERNSHIP IN MOROCCO — FEBRUARY / MARCH TO JULY 2027")}</span>
      </div>

      <div class="hero-grid">
        <div>
          <div class="hero-meta">
            <p>{bi("IA APPLIQUÉE · RECHERCHE OPÉRATIONNELLE · SOFTWARE", "APPLIED AI. OPERATIONS RESEARCH. SOFTWARE.")}</p>
            <p>MEKNÈS · MOROCCO</p>
          </div>
          <h1>Meryem El Osmani</h1>
          <p class="hero-tagline">{bi("Ingénieure en Intelligence Artificielle & Développement Logiciel", "Artificial Intelligence & Software Engineer")}</p>
          
          <p class="intro">
            {bi(
              "Étudiante en Master Intelligence Artificielle et Systèmes de Décision Optimale à Meknès. Je conçois des systèmes d'IA appliqués, des architectures logicielles robustes et des modèles d'optimisation mathématique de bout en bout. Spécialisée en recherche opérationnelle (Google OR-Tools CP-SAT), modélisation prédictive, RAG vectoriel et ingénierie logicielle full-stack.",
              "Master's student in Artificial Intelligence and Optimal Decision Systems in Meknès, Morocco. I design applied AI systems, robust software architectures, and end-to-end mathematical optimization models. Specialized in operations research (Google OR-Tools CP-SAT), predictive modeling, vector RAG, and full-stack software engineering."
            )}
          </p>
          
          <div class="hero-contact-strip">
            <a href="mailto:maryamelosmani@gmail.com" class="strip-item">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <span>maryamelosmani@gmail.com</span>
            </a>
            <a href="tel:+212684836656" class="strip-item">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              <span>+212 684 836 656</span>
            </a>
          </div>

          <div class="actions">
            <a class="button primary" href="#selected">
              {bi("Explorer mes projets", "Explore my projects")}
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
            <a class="button outline" id="heroCvBtn" href="Meryem_El_Osmani_CV_FR.pdf" download>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              {bi("Télécharger mon CV", "Download my CV")}
            </a>
            <a class="button outline" href="#contact">
              {bi("Me contacter", "Get in touch")}
            </a>
          </div>
        </div>

        <!-- Hero Executive Portrait Showcase (Only 1 prominent photo) -->
        <div class="hero-portrait-wrap">
          <div class="hero-portrait-card">
            <div class="hero-portrait-image-box">
              <img src="meryem-portrait.jpg" alt="Meryem El Osmani — Ingénieure IA & Logiciel" class="hero-portrait-img">
              <div class="hero-portrait-overlay"></div>
              
              <div class="hero-portrait-top-badge">
                <span class="status-pulse-dot"></span>
                <span>{bi("Stage PFE 2027 · Disponible", "PFE Internship 2027 · Available")}</span>
              </div>

              <div class="hero-portrait-master-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                <span>{bi("Master IA & Décision", "Master's in AI & Decision")}</span>
              </div>

              <div class="hero-portrait-glass-bar">
                <div class="glass-bar-headline">
                  <div class="glass-title-badge">
                    <span class="glass-check">✓</span>
                    <span class="glass-title">{bi("INGÉNIEURE IA & LOGICIEL", "AI & SOFTWARE ENGINEER")}</span>
                  </div>
                  <span class="glass-loc">📍 Meknès</span>
                </div>
                <p class="glass-sub">{bi("OR-Tools CP-SAT · MLOps & RAG · Architecture Logicielle", "OR-Tools CP-SAT · MLOps & RAG · Full-Stack Systems")}</p>
                <div class="glass-stats-strip">
                  <div class="glass-stat">
                    <strong>9</strong>
                    <span>{bi("Projets GitHub", "GitHub Projects")}</span>
                  </div>
                  <div class="glass-stat-divider"></div>
                  <div class="glass-stat">
                    <strong>PFE 2027</strong>
                    <span>{bi("Disponibilité", "Availability")}</span>
                  </div>
                  <div class="glass-stat-divider"></div>
                  <div class="glass-stat">
                    <strong>C1 / B2</strong>
                    <span>{bi("Bilingue", "Bilingual")}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. About Me Section -->
    <section class="section about-section" id="about">
      <div class="heading">
        <div>
          <p class="micro">01 / {bi("À PROPOS", "ABOUT ME")}</p>
          <h2>{bi("Relier l’analyse à la réalisation.", "Connecting analysis with implementation.")}</h2>
        </div>
        <p>{bi("Comprendre la donnée, choisir l'approche technique, construire le logiciel et évaluer ses limites.", "Understanding the data, choosing an approach, building the application and evaluating its limitations.")}</p>
      </div>

      <div class="about-grid">
          <div class="about-card">
            <span class="about-icon">🔬</span>
            <h3>{bi("Parcours académique & curiosité", "Academic foundation")}</h3>
            <p>
              {bi(
                "Ma formation associe génie informatique, systèmes intelligents et recherche opérationnelle. Je m’intéresse à la trajectoire complète qui mène d’un problème à une solution concrète : comprendre la donnée, modéliser les contraintes mathématiques, développer l’application et mesurer honnêtement ses limites.",
                "My background spans computer engineering, intelligent systems and operations research. I’m interested in the complete path from a problem to a working solution: understanding data, formulating mathematical constraints, building software and evaluating limitations."
              )}
            </p>
          </div>
          <div class="about-card">
            <span class="about-icon">⚡</span>
            <h3>{bi("Expérience pratique & équipe", "Practical impact")}</h3>
            <p>
              {bi(
                "Lors de mon stage chez Arimas Holdings, j’ai exercé comme team leader et ingénieure IA/logiciel sur Tadbir AI. Mon activité freelance m’a également appris à nettoyer, structurer et automatiser des flux de données répondant à de réels besoins métier.",
                "During my internship at Arimas Holdings, I worked as a team leader and AI/software engineering intern on Tadbir AI. My freelance work has also given me experience preparing and structuring data for practical business needs."
              )}
            </p>
          </div>
          <div class="about-card">
            <span class="about-icon">💡</span>
            <h3>{bi("Philosophie & transparence", "Engineering philosophy")}</h3>
            <p>
              {bi(
                "Mes projets explorent l'optimisation combinatoire (OR-Tools CP-SAT), le machine learning, le RAG vectoriel et la cybersécurité. À travers ce portfolio, je partage ce que je construis, les décisions qui sous-tendent chaque choix et les enseignements tirés en chemin.",
                "My projects explore combinatorial optimization (OR-Tools CP-SAT), machine learning, vector RAG and cybersecurity. Through this portfolio, I share what I build, the decisions behind it and what I learn along the way."
              )}
            </p>
          </div>
      </div>
    </section>

    <!-- 3. Selected Projects (Spotlight / Case Studies) -->
    <section class="section selected" id="selected">
      <div class="heading">
        <div>
          <p class="micro">02 / {bi("PROJETS SÉLECTIONNÉS", "SELECTED PROJECTS")}</p>
          <h2>{bi("Quatre études de cas approfondies.", "Four in-depth case studies.")}</h2>
        </div>
        <p>{bi("BidPilot AI, ResearchOS, Analyste IA multi-agents et V2C-Sentinel : explorez les décisions d'architecture et les détails d'implémentation.", "BidPilot AI, ResearchOS, Multi-Agent AI Analyst and V2C-Sentinel: explore the architectural choices and technical implementations.")}</p>
      </div>
      {selected_html}
    </section>

    <!-- 4. More Projects Section -->
    <section class="section work" id="projects">
      <div class="heading">
        <div>
          <p class="micro">03 / {bi("AUTRES PROJETS GITHUB", "MORE GITHUB PROJECTS")}</p>
          <h2>{bi("Cinq projets d'ingénierie & d'optimisation.", "Five engineering & optimization projects.")}</h2>
        </div>
        <p>{bi("FlowDesk AI, Tadbir AI, pipeline MLOps de bout en bout, intelligence de tarification e-commerce et optimisation logistique.", "FlowDesk AI, Tadbir AI, end-to-end MLOps pipeline, e-commerce pricing intelligence and logistics optimization.")}</p>
      </div>

      <div class="filters-bar">
        <span class="filter-label">{bi("Filtrer :", "Filter:")}</span>
        <div class="filters-wrapper">
          <button type="button" class="filter-btn active" data-filter="all" aria-pressed="true">{bi("Tous les projets (5)", "All projects (5)")}</button>
          <button type="button" class="filter-btn" data-filter="software" aria-pressed="false">{bi("IA & Systèmes", "AI & Systems")}</button>
          <button type="button" class="filter-btn" data-filter="ml" aria-pressed="false">{bi("ML & MLOps", "ML & MLOps")}</button>
          <button type="button" class="filter-btn" data-filter="data" aria-pressed="false">{bi("Data & Optimisation", "Data & Optimization")}</button>
        </div>
      </div>

      <div class="projects">
        {''.join(more_cards)}
      </div>
    </section>

    <!-- 5. Professional Experience -->
    <section class="section" id="experience">
      <div class="heading">
        <div>
          <p class="micro">04 / {bi("EXPÉRIENCE PROFESSIONNELLE", "PROFESSIONAL EXPERIENCE")}</p>
          <h2>{bi("Stages & Activité freelance.", "Experience in teams & consulting.")}</h2>
        </div>
        <p>{bi("Une pratique alliant conduite de projet, intégration logicielle et traitement rigoureux des données.", "Combining team coordination, software development and rigorous data processing.")}</p>
      </div>

      <div class="background-grid">
        <div class="timeline">
          <article class="timeline-item">
            <time>JUILLET—SEPTEMBRE 2026</time>
            <h4>Arimas Holdings</h4>
            <h3>{bi("Team Leader · Ingénieure IA / Logiciel stagiaire", "Team Leader · AI / Software Engineering Intern")}</h3>
            <p>
              {bi(
                "Travail avec une équipe de développement sur Tadbir AI, une plateforme de gestion d’entreprise intégrant des capacités d’IA. Coordination d’équipe combinée à des contributions concrètes au développement logiciel et à l’extraction de documents.",
                "Worked with a development team on Tadbir AI, a business-management platform incorporating AI capabilities. Combined team coordination with contributions to AI and software development."
              )}
            </p>
          </article>

          <article class="timeline-item">
            <time>OCTOBRE 2025—JANVIER 2026</time>
            <h4>EUMATRIX.eu · Upwork</h4>
            <h3>{bi("Data Analyst freelance", "Freelance Data Analyst")}</h3>
            <p>
              {bi(
                "Collecte de jeux de données ciblés pour le marché danois ; nettoyage, transformation et structuration des données avec Python et SQL. Contribution à la validation des données et à l’automatisation des workflows, avec une mission renouvelée par le client.",
                "Collected targeted datasets for the Danish market and cleaned, transformed and structured data using Python and SQL. Contributed to data validation and workflow automation, including a follow-up engagement with the same client."
              )}
            </p>
          </article>

          <article class="timeline-item">
            <time>AVRIL—JUIN 2024</time>
            <h4>EST Meknès</h4>
            <h3>{bi("Stagiaire en développement logiciel", "Software Development Intern")}</h3>
            <p>
              {bi(
                "Développement d’une application PHP/MySQL de génération automatique d’emplois du temps, déployée et utilisée au sein de trois départements académiques. Rédaction de la documentation d’utilisation et de maintenance.",
                "Developed a PHP/MySQL timetable-generation application used across three departments. Produced user and maintenance documentation."
              )}
            </p>
          </article>

          <article class="timeline-item">
            <time>JUILLET—AOÛT 2023</time>
            <h4>AREP · Meknès</h4>
            <h3>{bi("Stagiaire technicienne informatique", "IT Technician Intern")}</h3>
            <p>
              {bi(
                "Support des outils informatiques internes, assistance à la résolution d’incidents techniques et préparation de guides documentaires pour les utilisateurs.",
                "Supported internal tools, helped resolve technical incidents and prepared documentation for users."
              )}
            </p>
          </article>
        </div>

        <!-- 8. Education & 9. Certificates -->
        <aside>
          <h3 class="column-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            {bi("Formation académique", "Education")}
          </h3>
          <article class="education-item">
            <time>2025—2027 · {bi("En cours", "In progress")}</time>
            <h4>{bi("Master Intelligence Artificielle & Systèmes de Décision Optimale", "Master’s in Artificial Intelligence & Optimal Decision Systems")}</h4>
            <p>Faculté des Sciences, Meknès</p>
          </article>
          <article class="education-item">
            <time>2024—2025</time>
            <h4>{bi("Licence Systèmes Intelligents & Recherche Opérationnelle", "Licence in Intelligent Systems & Operations Research")}</h4>
            <p>Faculté des Sciences, Meknès</p>
          </article>
          <article class="education-item">
            <time>2022—2024</time>
            <h4>{bi("DUT Génie Informatique", "DUT in Computer Engineering")}</h4>
            <p>École Supérieure de Technologie, Meknès</p>
          </article>

          <!-- 9. Certificates and Training -->
          <div class="certificates-box">
            <h3>{bi("Certifications & Formations", "Certificates and training")}</h3>
            <div class="cert-entry">
              <span class="cert-featured-badge">{bi("CERTIFICAT CLÉ", "FEATURED CREDENTIAL")}</span>
              <strong>Google Cloud Cybersecurity Certificate</strong>
              <p>Google Cloud</p>
            </div>
            <div class="cert-entry">
              <strong>IBM / Coursera</strong>
              <p>Python for Data Science & AI · Generative AI for Data Analytics · Prompt Engineering Foundations</p>
            </div>
            <div class="cert-entry">
              <strong>Formations complémentaires</strong>
              <p>AWS Technical Essentials · Tableau (Salesforce) · Operations Research: Optimization Algorithms (NTU)</p>
            </div>
          </div>

          <div class="spoken-box">
            <span>🌐</span>
            <p>{bi("Arabe : Langue maternelle · Français : B2 · Anglais : C1 (EF SET 74/100)", "Arabic: Native · French: B2 · English: C1 (EF SET 74/100)")}</p>
          </div>
        </aside>
      </div>
    </section>

    <!-- 6. Areas of Practice (Skills) -->
    <section class="section expertise" id="expertise">
      <div class="heading">
        <div>
          <p class="micro">05 / {bi("DOMAINES DE COMPÉTENCES", "AREAS OF PRACTICE")}</p>
          <h2>{bi("Expertise & Méthodes de travail.", "Core competencies & toolsets.")}</h2>
        </div>
        <p>{bi("Quatre piliers techniques reliant analyse, modélisation, mise en production et optimisation mathématique.", "Four technical pillars connecting analysis, modeling, software deployment and mathematical optimization.")}</p>
      </div>

      <div class="expertise-grid">
        <article class="expertise-card">
          <span class="micro">01 / DATA</span>
          <h3>{bi("Analyse de données", "Data analysis")}</h3>
          <p>{bi("Préparer, explorer et structurer des volumes de données pour appuyer des analyses décisionnelles utiles.", "Preparing, exploring and structuring data to support useful analysis.")}</p>
          <div class="tech-capsule">Python · SQL · Pandas · NumPy · DuckDB · Polars · Tableau · Plotly</div>
        </article>

        <article class="expertise-card">
          <span class="micro">02 / AI & ML</span>
          <h3>{bi("IA & Machine learning", "AI and machine learning")}</h3>
          <p>{bi("Comparer méthodiquement les modèles prédictifs, concevoir des architectures RAG et orchestrer des agents autonomes.", "Systematically benchmarking predictive models, engineering vector RAG systems and orchestrating autonomous agents.")}</p>
          <div class="tech-capsule">Scikit-learn · LangGraph · pgvector · Sentence-Transformers · Gemini API</div>
        </article>

        <article class="expertise-card">
          <span class="micro">03 / SOFTWARE & MLOPS</span>
          <h3>{bi("Logiciel & MLOps", "Software and MLOps")}</h3>
          <p>{bi("Relier modèles et données aux applications réelles, avec des APIs rapides, du suivi d'expériences et du code reproductible.", "Connecting models and data to applications, with APIs, experiment tracking and reproducible environments.")}</p>
          <div class="tech-capsule">FastAPI · Django REST · Next.js · TypeScript · Docker · DVC · MLflow · Git</div>
        </article>

        <article class="expertise-card">
          <span class="micro">04 / OPTIMIZATION</span>
          <h3>{bi("Recherche opérationnelle", "Operations research")}</h3>
          <p>{bi("Formuler des contraintes mathématiques discrètes et linéaires, modéliser l’incertitude et optimiser les décisions opérationnelles.", "Formulating discrete and linear constraints, modeling uncertainty and optimizing operational decisions.")}</p>
          <div class="tech-capsule">Google OR-Tools CP-SAT · PuLP · Programmation discrète & linéaire · Monte-Carlo</div>
        </article>
      </div>
    </section>

    <!-- 7. Project Journal -->
    <section class="section journal-section" id="journal">
      <div class="heading">
        <div>
          <p class="micro">06 / {bi("JOURNAL DE PROJETS", "PROJECT JOURNAL")}</p>
          <h2>{bi("Les coulisses des projets.", "Behind the projects.")}</h2>
        </div>
        <p>{bi("Notes sur les expérimentations, les choix d’implémentation et les enseignements tirés sur le terrain.", "Notes on experiments, implementation choices and lessons from working with data, AI and software.")}</p>
      </div>

      <div class="journal-format-box">
        <strong>{bi("Format d’analyse rigoureux :", "Analytical article structure:")}</strong>
        <p>{bi("Le problème formulé → L’approche testée → L’expérimentation → Ce que les données ont montré → Limites & suites.", "The problem formulation → Approach tested → Implementation/experiment → Empirical findings → Limitations & next steps.")}</p>
      </div>

      <div class="journal-grid">
        {journal_html}
      </div>
    </section>

    <!-- 8. Dedicated CV & Resume Section -->
    <section class="section cv-showcase-section" id="cv">
      <div class="heading">
        <div>
          <p class="micro">07 / {bi("CURRICULUM VITAE", "CURRICULUM VITAE")}</p>
          <h2>{bi("Curriculum Vitae — Synthèse 1 Page A4", "Curriculum Vitae — 1-Page Focused Resume")}</h2>
        </div>
        <p>{bi("Conçu pour les recruteurs techniques et responsables d'équipe : une synthèse dense et lisible reliant modélisation IA, ingénierie logicielle et expérience concrète.", "Crafted for technical recruiters and engineering managers: a concise 1-page synthesis connecting AI modeling, software engineering and real-world execution.")}</p>
      </div>

      <div class="cv-showcase-grid">
        <!-- Interactive Visual Preview -->
        <div class="cv-preview-container">
          <div class="cv-preview-frame">
            <img src="output/cv-fr-1.png" alt="CV Meryem El Osmani (Français)" class="cv-preview-img i18n-fr" id="cvPreviewFr">
            <img src="output/cv-en-1.png" alt="Meryem El Osmani Resume (English)" class="cv-preview-img i18n-en" id="cvPreviewEn">
            <div class="cv-preview-overlay">
              <a href="Meryem_El_Osmani_CV_FR.pdf" target="_blank" rel="noopener noreferrer" class="button primary cv-open-btn" id="cvOpenTabBtn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                {bi("Ouvrir le PDF", "Open PDF")}
              </a>
            </div>
          </div>
          <p class="cv-caption"><span class="pulse-beacon"></span> {bi("Aperçu fidèle du document généré · Conforme 1 page A4", "Exact rendering of compiled document · Strict 1-page A4 format")}</p>
        </div>

        <!-- Details & Download Actions -->
        <div class="cv-details-panel">
          <div class="cv-badges-row">
            <span class="badge-chip">✓ {bi("1 Page A4 Stricte", "Strict 1-Page A4")}</span>
            <span class="badge-chip">✓ {bi("Optimisé ATS & Recruteurs", "ATS & Recruiter Optimized")}</span>
            <span class="badge-chip">✓ {bi("Liens GitHub & LinkedIn cliquables", "Clickable GitHub & LinkedIn links")}</span>
          </div>

          <div class="cv-highlights-box">
            <h4>{bi("Contenu clé du CV :", "Key resume contents:")}</h4>
            <ul class="cv-points-list">
              <li><strong>{bi("Formation d'élite :", "Education:")}</strong> {bi("Master IA & Systèmes de Décision Optimale (FSM Meknès) + Licence Systèmes Intelligents + DUT Génie Informatique.", "Master's in AI & Optimal Decision Systems (FSM Meknès) + BSc Intelligent Systems + DUT Computer Engineering.")}</li>
              <li><strong>{bi("Expérience professionnelle :", "Professional experience:")}</strong> {bi("Team Leader & Ingénieure IA/Logiciel stagiaire chez Arimas Holdings (Tadbir AI) + Data Analyst freelance (EUMATRIX.eu / Upwork) + Stagiaire EST.", "Team Leader & AI/Software intern at Arimas Holdings (Tadbir AI) + Freelance Data Analyst (EUMATRIX.eu / Upwork) + EST intern.")}</li>
              <li><strong>{bi("Projets phares sélectionnés :", "Featured projects:")}</strong> BidPilot AI (OR-Tools CP-SAT), ResearchOS (RAG / pgvector), Analyste IA multi-agents (LangGraph), V2C-Sentinel (Cyber-sécurité CAN), FlowDesk AI.</li>
              <li><strong>{bi("Compétences & Certifications :", "Skills & Certifications:")}</strong> Google Cloud Cybersecurity Certificate, Google OR-Tools CP-SAT, Python, Scikit-learn, LangGraph, Django REST, Next.js, Docker, PuLP.</li>
            </ul>
          </div>

          <div class="cv-downloads-action-block">
            <p class="cv-download-heading">{bi("Télécharger le document officiel (PDF) :", "Download official resume (PDF):")}</p>
            <div class="cv-buttons-duo">
              <a href="Meryem_El_Osmani_CV_FR.pdf" download class="cv-action-card active-card" id="cvCardFr">
                <div class="cv-card-icon">FR</div>
                <div class="cv-card-info">
                  <strong>{bi("Version Française", "French Version")}</strong>
                  <span>Format PDF · 78 Ko · Calendrier 2027</span>
                </div>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>

              <a href="Meryem_El_Osmani_CV_EN.pdf" download class="cv-action-card" id="cvCardEn">
                <div class="cv-card-icon">EN</div>
                <div class="cv-card-info">
                  <strong>{bi("Version Anglaise", "English Version")}</strong>
                  <span>PDF Format · 78 KB · 2027 Timeline</span>
                </div>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

            <div class="cv-meta-links">
              <span class="muted-label">{bi("Formats sources disponibles dans le dossier output/ :", "Source formats available in output/ folder:")}</span>
              <a href="output/CV_FR_editable.txt" target="_blank" class="meta-link">CV_FR_editable.txt</a>
              <span class="sep">·</span>
              <a href="output/CV_EN_editable.txt" target="_blank" class="meta-link">CV_EN_editable.txt</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. Contact Section -->
    <section class="section contact" id="contact">
      <p class="micro">08 / {bi("CONTACT & RECHERCHE PFE", "CONTACT")}</p>
      <h2>{bi("Échangeons sur ce que nous pourrions construire.", "Let’s discuss what we could build.")}</h2>
      
      <div class="contact-row">
        <p>
          {bi(
            "Je recherche un stage de fin d’études (PFE) au Maroc de février / mars à juillet 2027 en IA appliquée, recherche opérationnelle ou ingénierie logicielle. Si votre équipe recherche quelqu’un qui aime relier l’analyse à la réalisation, je serais ravie d’échanger sur vos projets et sur ma contribution.",
            "I’m seeking a final-year internship in Morocco in applied AI, operations research or software engineering. If your team is looking for someone who enjoys connecting analysis with implementation, I’d be happy to discuss your work and how I could contribute."
          )}
        </p>

        <div class="contact-meta-table">
          <div><span>{bi("Disponibilité :", "Availability:")}</span> <strong>{bi("Février / Mars à Juillet 2027", "February / March to July 2027")}</strong></div>
          <div><span>{bi("Localisation :", "Location:")}</span> <strong>Meknès, Morocco</strong></div>
          <div><span>Email :</span> <a href="mailto:maryamelosmani@gmail.com">maryamelosmani@gmail.com</a></div>
          <div><span>{bi("Téléphone :", "Phone:")}</span> <a href="tel:+212684836656">+212 684 836 656</a></div>
        </div>

        <div class="email-actions">
          <a class="button primary" href="mailto:maryamelosmani@gmail.com">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            {bi("Envoyer un e-mail", "Send an email")}
          </a>
          <button type="button" class="copy-email-btn" id="copyEmailBtn">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>maryamelosmani@gmail.com</span>
          </button>
        </div>
      </div>
    </section>
  </main>

  <!-- 11. Modals for Deep-Dive Case Studies -->
  {modals_html}

  <!-- Footer -->
  <footer>
    <div>
      <p>Meryem El Osmani<br><span>{bi("Meknès, Maroc · Portfolio professionnel & académique", "Meknès, Morocco · Professional & academic portfolio")}</span></p>
    </div>
    <div class="footer-links">
      <a href="https://github.com/MERYEMELOSMANI" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
      <a href="https://www.linkedin.com/in/meryem-el-osmani-754a56271" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
      <a href="mailto:maryamelosmani@gmail.com">Email ↗</a>
      <a href="tel:+212684836656">+212 684 836 656</a>
    </div>
  </footer>
</body>
</html>'''
    return html

if __name__ == '__main__':
    html_content = build_full_html()
    (DIST / 'index.html').write_text(html_content, encoding='utf-8')
    (ROOT / 'index.html').write_text(html_content, encoding='utf-8')
    
    redirect_html = '''<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;url=index.html?lang=en"><script>window.location.href="index.html?lang=en";</script></head><body>Redirecting...</body></html>'''
    (DIST / 'en.html').write_text(redirect_html, encoding='utf-8')
    (ROOT / 'en.html').write_text(redirect_html, encoding='utf-8')
    
    print('Generated complete bilingual portfolio featuring ONLY latest GitHub projects!')
