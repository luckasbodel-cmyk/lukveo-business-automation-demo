"""Local demonstration using synthetic data; no outbound email or AI request."""
import os
from tempfile import TemporaryDirectory
from pathlib import Path

# Set DB location before loading the module.
with TemporaryDirectory() as tmp:
    os.environ["LUKVEO_BUSINESS_DIR"] = tmp
    from api import business_autopilot, prospect_qualification
    row = business_autopilot.add_entry({"kind": "prospect", "title": "Entreprise DEMO", "detail": "Tableur et emails de contact"})
    print("Prospect de test créé:", row)
    print("Offre indicative:", prospect_qualification.select_offer("Entreprise DEMO", "Automatisation des emails"))
    result = prospect_qualification.generate({"id": row["id"], "action": "proposal"})
    print("Brouillon interne sans envoi:", result["notice"])
    print("Aperçu:", result["text"][:250])
print("La base de test temporaire a été supprimée.")
