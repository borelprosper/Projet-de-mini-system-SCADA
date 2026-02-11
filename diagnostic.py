# diagnostic.py
# Module de diagnostic et alarmes industrielles
# Permet d'analyser les capteurs et de mettre à jour l'état des machines en cas d'anomalie
import logger

def diagnostiquer_anomalie(sensor):
    """
    Analyse un capteur et retourne un message de diagnostic
    selon son type et ses seuils.

    Paramètres :
        sensor (dict) : dictionnaire contenant les informations du capteur
                         - id : ID du capteur
                         - type : type du capteur (temperature, pression, etc.)
                         - valeur : valeur actuelle
                         - seuil_min : seuil minimum
                         - seuil_max : seuil maximum
                         - machine_id : machine associée

    Retour :
        str : message de diagnostic
    """
    # Capteur de température
    if sensor["type"].lower() == "temperature":
        if sensor["valeur"] > sensor["seuil_max"]:
            return "Surchauffe détectée"
        elif sensor["valeur"] < sensor["seuil_min"]:
            return "Température anormalement basse"

    # Capteur de pression
    elif sensor["type"].lower() == "pression":
        if sensor["valeur"] > sensor["seuil_max"]:
            return "Surpression détectée"
        elif sensor["valeur"] < sensor["seuil_min"]:
            return "Chute de pression (fuite possible)"

    # Cas général pour tout autre capteur
    return "Anomalie capteur détectée"


def analyser_diagnostics(anomalies, machines):
    """
    Analyse une liste de capteurs en anomalie et met à jour l'état
    des machines si nécessaire.

    Paramètres :
        anomalies (list) : liste de dictionnaires de capteurs présentant des anomalies
        machines (list) : liste de dictionnaires de machines
    """
    if not anomalies:
        print("Aucun diagnostic à effectuer.")
        return

    print("\n--- DIAGNOSTICS INDUSTRIELS ---")

    for s in anomalies:
        message = diagnostiquer_anomalie(s)
        print(
            f"Machine {s['machine_id']} | "
            f"Capteur {s['id']} ({s['type']}) | "
            f"{message}"
        )
        logger.enregistrer_evenement(
            f"Diagnostic : {message} | Machine {s['machine_id']} | Capteur {s['id']} ({s['type']})"
        )

        # Mise à jour de l'état de la machine en panne si nécessaire
        for m in machines:
            if m["id"] == s["machine_id"] and m["etat"] != "en_panne":
                m["etat"] = "en_panne"
                logger.enregistrer_evenement(
                    f"Mise à jour état machine {m['id']} : en_panne suite à l'anomalie détectée"
                )

    print("-------------------------------")
