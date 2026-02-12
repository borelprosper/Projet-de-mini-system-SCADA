# main.py
# Point d'entrée du système de supervision industrielle
# Gère les menus interactifs pour :
# - Machines
# - Capteurs
# - Supervision
# - Diagnostic & Alarmes
# - Maintenance
# - Journal des événements
# - Rapports industriels

import machines
import sensors
import supervision
import diagnostic
import maintenance
import logger
import reports

# --------------------- MENU MACHINES ---------------------
def menu_machines(machines_list):
    """Menu interactif pour gérer les machines avec journalisation"""
    while True:
        print("\n--- MENU MACHINES ---")
        print("[1] Afficher les machines")
        print("[2] Ajouter une machine")
        print("[3] Modifier l'état d'une machine")
        print("[4] Supprimer une machine")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Choix : ").strip())

            if choix == 1:
                machines.afficher_machines(machines_list)
            elif choix == 2:
                machines.ajouter_machine(machines_list)
                logger.enregistrer_evenement("Ajout d'une machine effectué")
            elif choix == 3:
                machines.modifier_etat_machine(machines_list)
                logger.enregistrer_evenement("Modification de l'état d'une machine effectuée")
            elif choix == 4:
                machines.supprimer_machine(machines_list)
                logger.enregistrer_evenement("Suppression d'une machine effectuée")
            elif choix == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 4.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU CAPTEURS ---------------------
def menu_sensors(capteurs_list, machines_list):
    """Menu interactif pour gérer les capteurs avec journalisation"""
    while True:
        print("\n--- MENU CAPTEURS ---")
        print("[1] Afficher les capteurs")
        print("[2] Ajouter un capteur")
        print("[3] Modifier la valeur d'un capteur")
        print("[4] Supprimer un capteur")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Choix : ").strip())

            if choix == 1:
                sensors.afficher_sensors(capteurs_list)
            elif choix == 2:
                sensors.ajouter_sensor(capteurs_list, machines_list)
                logger.enregistrer_evenement("Ajout d'un capteur effectué")
            elif choix == 3:
                sensors.modifier_valeur_sensor(capteurs_list)
                logger.enregistrer_evenement("Modification d'un capteur effectuée")
            elif choix == 4:
                sensors.supprimer_sensor(capteurs_list)
                logger.enregistrer_evenement("Suppression d'un capteur effectuée")
            elif choix == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 4.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU SUPERVISION ---------------------
def menu_supervision(capteurs_list, machines_list):
    """Menu interactif pour la supervision des machines et capteurs"""
    while True:
        print("\n--- SUPERVISION ---")
        print("[1] Saisir les valeurs des capteurs")
        print("[2] Vérifier les seuils et anomalies")
        print("[3] Simuler un cycle complet de supervision")
        print("[4] Afficher l’état global")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Votre choix : ").strip())

            if choix == 1:
                supervision.saisir_valeurs_capteurs(capteurs_list)
                logger.enregistrer_evenement("Saisie des valeurs des capteurs effectuée")
            elif choix == 2:
                    anomalies = supervision.verifier_seuils_et_diagnostiquer(capteurs_list, machines_list)
                    if anomalies:
                        print("\nAnomalies détectées :")
                        for s in anomalies:
                            print(
                                f"Capteur {s['id']} ({s['type']}) "
                                f"sur machine {s['machine_id']} | "
                                f"Valeur = {s['valeur']} | "
                                f"Seuils [{s['seuil_min']} ; {s['seuil_max']}]")
                    else:
                        print("Aucun problème détecté")
                        machines.sauvegarder_machines(machines_list)
            elif choix == 3:
                supervision.cycle_supervision(capteurs_list, machines_list)
                machines.sauvegarder_machines(machines_list)
                sensors.sauvegarder_sensors(capteurs_list)
                logger.enregistrer_evenement("Cycle complet de supervision effectué")
            elif choix == 4:
                supervision.afficher_etat_global(machines_list)
            elif choix == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 4.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU DIAGNOSTIC ---------------------
def menu_diagnostic(capteurs_list, machines_list):
    """Menu interactif pour le diagnostic et les alarmes"""
    anomalies = []

    while True:
        print("\n--- Diagnostic & Alarmes ---")
        print("[1] Lancer le diagnostic des machines")
        print("[2] Détecter les anomalies des capteurs")
        print("[3] Déclencher les alarmes")
        print("[4] Mettre à jour l’état des machines selon anomalies")
        print("[5] Afficher les anomalies détectées")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Votre choix : ").strip())

            if choix == 1:
                print("\nDiagnostic des machines")
                en_panne = [m for m in machines_list if m["etat"] == "en_panne"]
                if not en_panne:
                    print("Toutes les machines sont en service.")
                else:
                    print("Machines en panne :")
                    for m in en_panne:
                        print(f"{m['id']} | {m['nom']} | État : {m['etat']}")
            elif choix == 2:
                anomalies = [
                    s for s in capteurs_list
                    if s["valeur"] < s["seuil_min"] or s["valeur"] > s["seuil_max"] ]
                if not anomalies:
                    print("Aucun capteur en anomalie.")
                else:
                    print(f"{len(anomalies)} anomalies détectées.")
            elif choix == 3:
                if not anomalies:
                    print("Aucune alarme à déclencher.")
                else:
                    for s in anomalies:
                        message = diagnostic.diagnostiquer_anomalie(s)
                        print(f"ALERTE ! Machine {s['machine_id']} | Capteur {s['id']} ({s['type']}) : {message}")
                        logger.enregistrer_evenement(f"Alerte déclenchée : {message} sur machine {s['machine_id']}")
            elif choix == 4:
                if not anomalies:
                    print("Aucun changement d’état nécessaire.")
                else:
                    for s in anomalies:
                        for m in machines_list:
                            if m["id"] == s["machine_id"]:
                                m["etat"] = "en_panne"
                    machines.sauvegarder_machines(machines_list)
                    logger.enregistrer_evenement("Mise à jour des machines selon anomalies effectuée")
                    print("État des machines mis à jour selon les anomalies détectées.")
            elif choix == 5:
                if not anomalies:
                    print("Aucune anomalie détectée.")
                else:
                    for s in anomalies:
                        print(
                            f"Capteur {s['id']} ({s['type']}) sur machine {s['machine_id']} | "
                            f"Valeur = {s['valeur']} | Seuils [{s['seuil_min']} ; {s['seuil_max']}]")
            elif choix == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 5.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU MAINTENANCE ---------------------
def menu_maintenance(machines_list):
    """Menu interactif pour la maintenance (GMAO)"""
    while True:
        print("\n--- MAINTENANCE ---")
        print("[1] Mettre une machine en maintenance")
        print("[2] Sortir une machine de maintenance")
        print("[3] Afficher l’état de maintenance")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Votre choix : ").strip())

            if choix == 1:
                maintenance.mettre_en_maintenance(machines_list)
            elif choix == 2:
                maintenance.remettre_en_service(machines_list)
            elif choix == 3:
                maintenance.afficher_maintenance()
            elif choix == 0:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 3.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU JOURNAL ---------------------
def menu_journal():
    """Menu interactif pour le journal des événements"""
    while True:
        print("\n--- JOURNAL ---")
        print("[1] Afficher les événements")
        print("[2] Sauvegarder le journal")
        print("[3] Charger le journal")
        print("[0] Retour menu principal")

        try :
            choix = int(input("Votre choix : ").strip())

            if choix == 1:
                logger.afficher_evenements()
            elif choix == 2:
                logger.sauvegarder_journal()
            elif choix == 3:
                logger.charger_journal()
            elif choix == 0:
                break
            else :
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 3.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- MENU RAPPORTS ---------------------
def menu_rapports(machines_list, capteurs_list):
    """Affiche le rapport industriel complet"""
    reports.generer_rapport(machines_list, capteurs_list)

# --------------------- MENU PRINCIPAL ---------------------
def menu_principal():
    """Menu principal de l'application"""
    logger.enregistrer_evenement("Démarrage de l'application de supervision")

    # Chargement des données
    machines_list = machines.charger_machines()
    capteurs_list = sensors.charger_sensors()

    while True:
        print("\n===== SUPERVISION INDUSTRIELLE =====")
        print("[1] Gestion des machines")
        print("[2] Gestion des capteurs")
        print("[3] Supervision de l'installation")
        print("[4] Diagnostic & Alarmes")
        print("[5] Maintenance")
        print("[6] Journal des événements")
        print("[7] Rapports industriels")
        print("[0] Quitter")

        try :
            choix = int(input("Votre choix : ").strip())
            
            if choix == 1:
                menu_machines(machines_list)
            elif choix == 2:
                menu_sensors(capteurs_list, machines_list)
            elif choix == 3:
                menu_supervision(capteurs_list, machines_list)
            elif choix == 4:
                menu_diagnostic(capteurs_list, machines_list)
            elif choix == 5:
                menu_maintenance(machines_list)
            elif choix == 6:
                menu_journal()
            elif choix == 7:
                menu_rapports(machines_list, capteurs_list)
            elif choix == 0:
                reponse = input("Voulez-vous vraiment quitter ? (oui/non) : ").strip().lower()

                if reponse in ["oui", "o", "yes", "y"]:
                    logger.enregistrer_evenement("Arrêt de l'application")
                    print("Fin du programme")
                    break
                else:
                    print("Retour au menu principal.")
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 0 et 7.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

# --------------------- EXECUTION PRINCIPALE ---------------------
if __name__ == "__main__":
    menu_principal()