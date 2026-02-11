# machines.py
# Module de gestion des machines industrielles avec journalisation

import os
import logger  # Pour enregistrer les événements

# Fichier de stockage des machines
FICHIER_MACHINES = "data/machines.txt"


def charger_machines():
    """Charge les machines depuis le fichier texte"""
    machines_list = []

    if not os.path.exists(FICHIER_MACHINES):
        return machines_list

    try:
        with open(FICHIER_MACHINES, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    id_m, nom, etat = ligne.split(";")
                    machines_list.append({"id": id_m, "nom": nom, "etat": etat})
    except Exception as e:
        print(f"Erreur lors du chargement des machines : {e}")

    return machines_list


def sauvegarder_machines(machines_list):
    """Sauvegarde les machines dans le fichier texte"""
    try:
        if not os.path.exists("data"):
            os.makedirs("data")

        with open(FICHIER_MACHINES, "w", encoding="utf-8") as f:
            for m in machines_list:
                f.write(f"{m['id']};{m['nom']};{m['etat']}\n")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des machines : {e}")


def afficher_machines(machines_list):
    """Affiche toutes les machines présentes dans la liste"""
    if not machines_list:
        print("Aucune machine enregistrée.")
        return

    print("\n--- LISTE DES MACHINES ---")
    for m in machines_list:
        print(f"ID: {m['id']} | Nom: {m['nom']} | État: {m['etat']}")
    print("--------------------------")


def ajouter_machine(machines_list):
    """Permet d'ajouter une nouvelle machine"""
    id_m = input("ID de la machine : ").strip()
    nom = input("Nom de la machine : ").strip()

    for m in machines_list:
        if m["id"] == id_m:
            print("Erreur : une machine avec cet ID existe déjà.")
            return

    machine = {"id": id_m, "nom": nom, "etat": "en_service"}
    machines_list.append(machine)
    sauvegarder_machines(machines_list)

    # Journalisation
    logger.enregistrer_evenement(f"Machine ajoutée : {id_m} | {nom}")
    print("Machine ajoutée avec succès.")


def modifier_etat_machine(machines_list):
    """Permet de modifier l'état d'une machine existante"""
    id_m = input("ID de la machine à modifier : ").strip()

    for m in machines_list:
        if m["id"] == id_m:
            print("États possibles :")
            print("1 - en_service")
            print("2 - en_panne")
            print("3 - maintenance")

            choix = input("Votre choix : ").strip()

            if choix == "1":
                m["etat"] = "en_service"
            elif choix == "2":
                m["etat"] = "en_panne"
            elif choix == "3":
                m["etat"] = "maintenance"
            else:
                print("Choix invalide.")
                return

            sauvegarder_machines(machines_list)
            logger.enregistrer_evenement(f"État de la machine {id_m} modifié en {m['etat']}")
            print("État de la machine mis à jour.")
            return

    print("Machine non trouvée.")


def supprimer_machine(machines_list):
    """Supprime une machine existante selon son ID"""
    id_m = input("ID de la machine à supprimer : ").strip()

    for m in machines_list:
        if m["id"] == id_m:
            machines_list.remove(m)
            sauvegarder_machines(machines_list)
            logger.enregistrer_evenement(f"Machine supprimée : {id_m} | {m['nom']}")
            print("Machine supprimée.")
            return

    print("Machine non trouvée.")
