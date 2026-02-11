# sensors.py
# Module de gestion des capteurs industriels avec journalisation

import os
import logger  # Pour enregistrer les événements

FICHIER_SENSORS = "data/sensors.txt"


def verifier_dossier_data():
    if not os.path.exists("data"):
        os.makedirs("data")


def charger_sensors():
    """Charge les capteurs depuis le fichier texte"""
    verifier_dossier_data()
    sensors_list = []

    if not os.path.exists(FICHIER_SENSORS):
        return sensors_list

    try:
        with open(FICHIER_SENSORS, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    id_s, type_s, val, smin, smax, machine_id = ligne.split(";")
                    sensors_list.append({
                        "id": id_s,
                        "type": type_s,
                        "valeur": float(val),
                        "seuil_min": float(smin),
                        "seuil_max": float(smax),
                        "machine_id": machine_id
                    })
    except Exception as e:
        print(f"Erreur lors du chargement des capteurs : {e}")

    return sensors_list


def sauvegarder_sensors(sensors_list):
    """Sauvegarde les capteurs dans le fichier texte"""
    verifier_dossier_data()
    try:
        with open(FICHIER_SENSORS, "w", encoding="utf-8") as f:
            for s in sensors_list:
                f.write(f"{s['id']};{s['type']};{s['valeur']};{s['seuil_min']};{s['seuil_max']};{s['machine_id']}\n")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des capteurs : {e}")


def afficher_sensors(sensors_list):
    if not sensors_list:
        print("Aucun capteur enregistré.")
        return

    print("\n--- LISTE DES CAPTEURS ---")
    for s in sensors_list:
        print(f"ID: {s['id']} | Type: {s['type']} | Valeur: {s['valeur']} | Seuils: [{s['seuil_min']} ; {s['seuil_max']}] | Machine: {s['machine_id']}")
    print("--------------------------")


def ajouter_sensor(sensors_list, machines_list):
    """Permet d'ajouter un nouveau capteur"""
    id_s = input("ID du capteur : ").strip()

    for s in sensors_list:
        if s["id"] == id_s:
            print("Erreur : un capteur avec cet ID existe déjà.")
            return

    type_s = input("Type du capteur (température, pression, etc.) : ").strip()

    try:
        seuil_min = float(input("Seuil minimum : "))
        seuil_max = float(input("Seuil maximum : "))
    except ValueError:
        print("Erreur : seuils invalides.")
        return

    if seuil_min >= seuil_max:
        print("Erreur : le seuil minimum doit être inférieur au seuil maximum.")
        return

    machine_id = input("ID de la machine associée : ").strip()

    if not any(m["id"] == machine_id for m in machines_list):
        print("Erreur : machine inexistante.")
        return

    sensor = {
        "id": id_s,
        "type": type_s,
        "valeur": 0.0,
        "seuil_min": seuil_min,
        "seuil_max": seuil_max,
        "machine_id": machine_id
    }

    sensors_list.append(sensor)
    sauvegarder_sensors(sensors_list)
    logger.enregistrer_evenement(f"Capteur ajouté : {id_s} | Type : {type_s} | Machine : {machine_id}")
    print("Capteur ajouté avec succès.")


def modifier_valeur_sensor(sensors_list):
    """Permet de modifier la valeur d'un capteur existant"""
    id_s = input("ID du capteur à modifier : ").strip()

    for s in sensors_list:
        if s["id"] == id_s:
            print(f"Valeur actuelle : {s['valeur']}")
            try:
                nouvelle_valeur = float(input("Nouvelle valeur : "))
            except ValueError:
                print("Erreur : valeur invalide.")
                return

            s["valeur"] = nouvelle_valeur
            sauvegarder_sensors(sensors_list)
            logger.enregistrer_evenement(f"Valeur du capteur {id_s} modifiée en {nouvelle_valeur}")
            print("Valeur du capteur mise à jour.")
            return

    print("Capteur non trouvé.")


def supprimer_sensor(sensors_list):
    """Supprime un capteur existant selon son ID"""
    id_s = input("ID du capteur à supprimer : ").strip()

    for s in sensors_list:
        if s["id"] == id_s:
            sensors_list.remove(s)
            sauvegarder_sensors(sensors_list)
            logger.enregistrer_evenement(f"Capteur supprimé : {id_s} | Type : {s['type']}")
            print("Capteur supprimé.")
            return

    print("Capteur non trouvé.")
