# maintenance.py
# Module de gestion de la maintenance (GMAO) avec journalisation

import os
from datetime import datetime
import logger  # Module pour enregistrer les événements

FICHIER_MAINTENANCE = "data/maintenance.txt"


def verifier_dossier_data():
    if not os.path.exists("data"):
        os.makedirs("data")


def enregistrer_maintenance(machine_id, nouvel_etat, commentaire):
    """Enregistre une opération de maintenance dans le fichier"""
    verifier_dossier_data()
    date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(FICHIER_MAINTENANCE, "a", encoding="utf-8") as f:
            f.write(f"{date_heure};{machine_id};{nouvel_etat};{commentaire}\n")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de maintenance : {e}")


def afficher_maintenance():
    """Affiche l'historique des opérations de maintenance"""
    if not os.path.exists(FICHIER_MAINTENANCE):
        print("Aucune opération de maintenance enregistrée.")
        return

    print("\n--- HISTORIQUE DE MAINTENANCE ---")
    try:
        with open(FICHIER_MAINTENANCE, "r", encoding="utf-8") as f:
            for ligne in f:
                date, machine_id, etat, commentaire = ligne.strip().split(";")
                print(f"{date} | Machine {machine_id} | {etat} | {commentaire}")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    print("--------------------------------")


def mettre_en_maintenance(machines):
    """Met une machine en état de maintenance"""
    machine_id = input("ID de la machine à mettre en maintenance : ").strip()

    for m in machines:
        if m["id"] == machine_id:
            m["etat"] = "maintenance"
            commentaire = input("Commentaire maintenance : ").strip()
            enregistrer_maintenance(machine_id, "maintenance", commentaire)
            logger.enregistrer_evenement(f"Machine {machine_id} mise en maintenance | Commentaire : {commentaire}")
            print("Machine mise en maintenance.")
            return

    print("Machine non trouvée.")


def remettre_en_service(machines):
    """Sort une machine de maintenance et la remet en service"""
    machine_id = input("ID de la machine à sortir de maintenance : ").strip()

    for m in machines:
        if m["id"] == machine_id:
            m["etat"] = "en_service"
            commentaire = "Fin de maintenance"
            enregistrer_maintenance(machine_id, "en_service", commentaire)
            logger.enregistrer_evenement(f"Machine {machine_id} remise en service")
            print("Machine remise en service.")
            return

    print("Machine non trouvée.")


def afficher_etat_maintenance(machines):
    """Affiche l'état de maintenance de toutes les machines"""
    if not machines:
        print("Aucune machine enregistrée.")
        return

    print("\n--- ÉTAT DE MAINTENANCE DES MACHINES ---")
    for m in machines:
        print(f"ID: {m['id']} | Nom: {m['nom']} | État: {m['etat']}")
    print("----------------------------------------")
