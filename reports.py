# reports.py
# Module de génération de rapports industriels
# Permet de générer un rapport complet de l'état des machines,
# des capteurs et du dernier incident enregistré dans le journal.

import os
import logger  # Pour récupérer le dernier incident et le journal des événements


def generer_rapport(machines, sensors):
    """
    Affiche le rapport industriel complet.
    Comprend :
    - Nombre total de machines et état de chacune
    - Nombre de capteurs en alerte
    - Dernier incident enregistré dans le journal
    """

    # Calcul du nombre total de machines et leur état
    total_machines = len(machines)
    en_service = sum(1 for m in machines if m["etat"] == "en_service")
    en_panne = sum(1 for m in machines if m["etat"] == "en_panne")
    maintenance_count = sum(1 for m in machines if m["etat"] == "maintenance")

    # Calcul des alertes détectées par les capteurs
    # Une alerte est déclenchée si la valeur du capteur est hors des seuils
    alertes = sum(
        1 for s in sensors if s["valeur"] < s["seuil_min"] or s["valeur"] > s["seuil_max"]
    )

    # Récupérer le dernier incident depuis le journal des événements
    # Si le journal est vide, afficher "Aucun incident"
    dernier_incident = logger.journal[-1] if hasattr(logger, "journal") and logger.journal else "Aucun incident"

    # Affichage du rapport
    print("\n========= RAPPORT INDUSTRIEL =========")
    print(f"Machines totales : {total_machines}")
    print(f"En service       : {en_service}")
    print(f"En panne         : {en_panne}")
    print(f"En maintenance   : {maintenance_count}")
    print(f"Alertes détectées: {alertes}")
    print(f"Dernier incident : {dernier_incident}")
    print("=====================================")
