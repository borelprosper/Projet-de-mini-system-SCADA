# logger.py
# Module de journalisation des événements industriels
# Permet d'enregistrer, afficher, sauvegarder et charger le journal des événements

import os
from datetime import datetime

# Fichier de stockage des logs
FICHIER_LOGS = "data/logs.txt"

# Journal en mémoire (liste)
journal = []


def verifier_dossier_data():
    """
    Vérifie que le dossier 'data' existe.
    Si ce n'est pas le cas, le crée.
    """
    if not os.path.exists("data"):
        os.makedirs("data")


def enregistrer_evenement(message):
    """
    Enregistre un événement dans le journal mémoire et dans le fichier.
    Chaque événement est horodaté.
    """
    verifier_dossier_data()  # S'assurer que le dossier data existe
    date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"{date_heure} | {message}"

    # Ajouter l'événement dans le journal mémoire
    journal.append(ligne)

    # Sauvegarder immédiatement l'événement dans le fichier
    with open(FICHIER_LOGS, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def afficher_evenements():
    """
    Affiche tous les événements stockés en mémoire.
    Si le journal est vide, affiche un message approprié.
    """
    if not journal:
        print("Aucun événement enregistré en mémoire.")
        return

    print("\n--- JOURNAL DES ÉVÉNEMENTS (Mémoire) ---")
    for ligne in journal:
        print(ligne)
    print("----------------------------------------")


def sauvegarder_journal():
    """
    Sauvegarde tout le journal mémoire dans le fichier logs.
    Remplace le contenu du fichier existant.
    """
    verifier_dossier_data()  # S'assurer que le dossier data existe
    with open(FICHIER_LOGS, "w", encoding="utf-8") as f:
        for ligne in journal:
            f.write(ligne + "\n")
    print("Journal sauvegardé dans le fichier.")


def charger_journal():
    """
    Charge le journal depuis le fichier dans la mémoire.
    Si le fichier n'existe pas, informe l'utilisateur.
    """
    verifier_dossier_data()
    journal.clear()  # Vider la mémoire avant le chargement

    if not os.path.exists(FICHIER_LOGS):
        print("Aucun fichier de journal à charger.")
        return

    with open(FICHIER_LOGS, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                journal.append(ligne)

    print("Journal chargé depuis le fichier.")
