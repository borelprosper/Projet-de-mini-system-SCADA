# supervision.py
# Module de supervision industrielle (SCADA simplifié)
# Intègre la journalisation et les diagnostics automatiques des anomalies

import logger
import diagnostic


def saisir_valeurs_capteurs(sensors):
    """Saisie manuelle des valeurs des capteurs avec journalisation"""
    if not sensors:
        print("Aucun capteur disponible.")
        return

    print("\n--- SAISIE DES VALEURS DES CAPTEURS ---")
    for s in sensors:
        try:
            valeur = float(input(f"Capteur {s['id']} ({s['type']}) - valeur actuelle : "))
            s["valeur"] = valeur
            logger.enregistrer_evenement(f"Capteur {s['id']} valeur modifiée : {valeur}")
        except ValueError:
            print("Valeur invalide, la valeur précédente est conservée.")


def verifier_seuils_et_diagnostiquer(sensors, machines):
    """
    Vérifie les seuils des capteurs, met à jour les machines, et lance un diagnostic
    Retourne la liste des anomalies détectées
    """
    anomalies = []

    for s in sensors:
        if s["valeur"] < s["seuil_min"] or s["valeur"] > s["seuil_max"]:
            anomalies.append(s)

            # Mise en panne automatique si machine en service
            for m in machines:
                if m["id"] == s["machine_id"]:
                    if m["etat"] == "en_service":
                        m["etat"] = "en_panne"
                        logger.enregistrer_evenement(
                            f"Machine {m['id']} mise en panne par supervision (capteur {s['id']})"
                        )

    # Diagnostic automatique
    if anomalies:
        print("\n--- DIAGNOSTICS AUTOMATIQUES ---")
        diagnostic.analyser_diagnostics(anomalies, machines)

    return anomalies


def afficher_etat_global(machines):
    """Affiche l'état global de toutes les machines"""
    print("\n--- ÉTAT GLOBAL DES MACHINES ---")
    for m in machines:
        print(f"ID: {m['id']} | Nom: {m['nom']} | État: {m['etat']}")
    print("--------------------------------")


def cycle_supervision(sensors, machines):
    """
    Exécute un cycle complet de supervision industrielle :
    1. Saisie des valeurs des capteurs
    2. Vérification des seuils
    3. Diagnostic automatique
    4. Affichage des anomalies et état global
    """
    saisir_valeurs_capteurs(sensors)
    anomalies = verifier_seuils_et_diagnostiquer(sensors, machines)

    if anomalies:
        print("\n--- ANOMALIES DÉTECTÉES ---")
        for s in anomalies:
            print(
                f"Capteur {s['id']} ({s['type']}) sur machine {s['machine_id']} | "
                f"Valeur = {s['valeur']} | Seuils [{s['seuil_min']} ; {s['seuil_max']}]"
            )
    else:
        print("\nAucune anomalie détectée.")

    afficher_etat_global(machines)
