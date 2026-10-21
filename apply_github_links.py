"""
Apply verified GitHub repository links to all 10 projects in generate_unified_site.py:
1. ResearchOS: research-os
2. Analyste IA multi-agents: autonomous-ai-data-analyst
3. V2C-Sentinel: V2C-Sentinel
4. Tadbir AI: FAWATIR-ROOT
5. Customer Churn · MLOps: churn-prediction-mlops
6. Pricing Analytics Engine: pricing-analytics-engine
7. Supply Chain Optimisation: supply-chain-optimization-dashboard
8. Traffic Flow Prediction: Mini_project-TrafficFlowPrediction-
9. Computer Vision Gesture Suite: hand-detection-program
10. Contact Manager: Gestion-des-contacts
"""
from pathlib import Path
import re

file_path = Path("generate_unified_site.py")
content = file_path.read_text(encoding="utf-8")

# 1. Update researchos repo
content = re.sub(
    r"('researchos':\s*\{[^}]*?'repo':\s*)(None|'[^']*?')",
    r"\1'research-os'",
    content
)

# 2. Update analyste-ia repo
content = re.sub(
    r"('analyste-ia':\s*\{[^}]*?'repo':\s*)(None|'[^']*?')",
    r"\1'autonomous-ai-data-analyst'",
    content
)

# 3. Update tadbir-ai repo
content = re.sub(
    r"('tadbir-ai':\s*\{[^}]*?'repo':\s*)(None|'[^']*?')",
    r"\1'FAWATIR-ROOT'",
    content
)

# 4. In more_projects, update Tadbir AI repo
content = re.sub(
    r"(name='Tadbir AI',[^}]*?repo=)(None|'[^']*?')",
    r"\1'FAWATIR-ROOT'",
    content
)

# 5. In modals_html, add Explore Further section with GitHub link
modal_old = """                <div class="deep-dive-section">
                  <h4>7. {bi("Enseignements tirés (Lessons Learned)", "Lessons Learned")}</h4>
                  <p>{bi(p['fr']['lessons'], p['en']['lessons'])}</p>
                </div>
              </div>"""

modal_new = """                <div class="deep-dive-section">
                  <h4>7. {bi("Enseignements tirés (Lessons Learned)", "Lessons Learned")}</h4>
                  <p>{bi(p['fr']['lessons'], p['en']['lessons'])}</p>
                </div>
                
                <div class="deep-dive-section">
                  <h4>8. {bi("Explorer le projet & Code source (Explore Further)", "Explore Further")}</h4>
                  <p style="margin-bottom: 12px;">{bi("Accédez au dépôt officiel sur GitHub pour examiner le code source, l’architecture et les instructions d’exécution locale :", "Explore the official GitHub repository for source code, architecture specifications, and local execution guides:")}</p>
                  <a class="source-btn" href="{GH+p['repo']}" target="_blank" rel="noopener noreferrer" style="display:inline-flex;">
                    <svg width="15" height="15" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    {bi("Ouvrir le dépôt GitHub", "View GitHub repository")}
                    <span>↗</span>
                  </a>
                </div>
              </div>"""

if modal_old in content:
    content = content.replace(modal_old, modal_new)
    print("Added Section 8 GitHub link to modals!")
else:
    print("Warning: modal_old not matched directly, checking variations...")

file_path.write_text(content, encoding="utf-8")
print("generate_unified_site.py updated with verified GitHub links!")
