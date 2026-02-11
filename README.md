# Système de Supervision Industrielle (SCADA léger)

Bienvenue dans le manuel utilisateur de votre application de supervision industrielle. Ce programme est un **SCADA simplifié** (Supervisory Control And Data Acquisition) conçu pour surveiller et contrôler des machines et des capteurs dans un environnement de production.

Pas besoin d'être un expert en informatique : ce guide vous explique, avec des exemples, ce que fait chaque partie du système.

---

## À quoi sert ce programme ?

Imaginez une usine avec des machines (des convoyeurs, des presses, des fours...). Chaque machine est équipée de **capteurs** (température, pression, etc.). Votre rôle est de vous assurer que tout fonctionne correctement.

Ce programme vous permet de :

* **Gérer vos machines** (les ajouter, les supprimer, changer leur état).
* **Surveiller les capteurs** (voir leurs valeurs, détecter les dépassements de seuils).
* **Déclencher des alarmes** et diagnostiquer les pannes.
* **Planifier de la maintenance**.
* **Tenir un journal** de tous les événements.
* **Générer des rapports** sur l'état de votre atelier.

---

## Comment utiliser l'application ?

Lorsque vous lancez le programme, vous arrivez sur le **menu principal** :

```
===== SUPERVISION INDUSTRIELLE =====
[1] Gestion des machines
[2] Gestion des capteurs
[3] Supervision de l'installation
[4] Diagnostic & Alarmes
[5] Maintenance
[6] Journal des événements
[7] Rapports industriels
[0] Quitter
```

Il vous suffit de taper le chiffre correspondant à l'action souhaitée, puis de valider avec `Entrée`.

---

## 1. Gestion des machines

Ce menu vous permet de faire l'inventaire de vos équipements.

### Exemple concret :

Vous venez d'acheter une nouvelle **presse hydraulique**. Vous voulez l'ajouter dans le système.

1. Menu `[1]` → `[2]` Ajouter une machine
2. On vous demande un **ID** (ex: `PR001`) et un **nom** (ex: `Presse Hydraulique`)
3. La machine est créée avec l'état par défaut : **"en_service"**.

Vous pouvez également :

* Voir la liste des machines.
* Mettre une machine en **panne**, en **maintenance** ou la **remettre en service**.
* Supprimer une machine (si elle est retirée de l'usine).

> Chaque action est automatiquement enregistrée dans le journal.

---

## 2. Gestion des capteurs

Les capteurs sont les "yeux" du système. Ils mesurent en temps réel des grandeurs physiques.

### Exemple concret :

Vous installez un capteur de **température** sur la presse `PR001`.

1. Menu `[2]` → `[2]` Ajouter un capteur
2. Vous renseignez :

   * **ID** du capteur : `TEMP001`
   * **Type** : `temperature`
   * **Seuil min** : `10.0`
   * **Seuil max** : `80.0`
   * **Machine associée** : `PR001`
3. Le capteur est créé. Sa valeur par défaut est `0.0` (vous la modifierez plus tard).

Vous pouvez aussi modifier la **valeur lue** par un capteur, ou supprimer un capteur défectueux.

---

## 3. Supervision

C'est le cœur du système. Ici, vous simulez la **lecture des capteurs** et le système vérifie automatiquement si tout va bien.

### Exemple concret :

Il est 14h00, vous faites votre tournée. Vous saisissez les valeurs des capteurs :

* Capteur `TEMP001` : `95.0` (c'est trop haut ! Le seuil max est de 80).

Le système détecte l'anomalie et :

1. Passe automatiquement la machine `PR001` en état **"en_panne"**.
2. Enregistre un événement dans le journal.
3. Vous affiche un diagnostic : **"Surchauffe détectée"**.

Vous pouvez aussi exécuter un **"Cycle complet"** qui enchaîne toutes ces étapes en une seule commande.

---

## 4. Diagnostic & Alarmes

Ce menu analyse les anomalies et déclenche des alertes.

### Exemple concret :

Après avoir saisi la valeur excessive de `95.0` sur le capteur de température, vous allez dans le menu Diagnostic :

1. `[2]` Détecter les anomalies → le système liste les capteurs hors seuils.
2. `[3]` Déclencher les alarmes → le système affiche **"ALERTE ! Machine PR001 : Surchauffe détectée"**.
3. `[4]` Mettre à jour l’état des machines → le système confirme le passage en panne.

---

## 5. Maintenance

Quand une machine tombe en panne ou nécessite une révision, vous passez par ce menu.

### Exemple concret :

Un technicien intervient sur la presse `PR001`.

1. Menu `[5]` → `[1]` Mettre une machine en maintenance
2. Vous entrez l'ID `PR001` et un commentaire : `"Remplacement sonde de température"`
3. La machine passe en état **"maintenance"**.
4. Une fois la réparation terminée, vous utilisez l'option `[2]` Sortir de maintenance pour la remettre en **"en_service"**.

Toutes ces opérations sont horodatées et conservées dans un historique dédié.

---

## 6. Journal des événements

Toutes les actions importantes sont enregistrées. Ce menu vous permet de les consulter.

### Exemple d'affichage :

```
--- JOURNAL DES ÉVÉNEMENTS ---
2025-04-08 14:05:00 | Machine ajoutée : PR001 | Presse Hydraulique
2025-04-08 14:12:00 | Capteur TEMP001 valeur modifiée : 95.0
2025-04-08 14:12:05 | Machine PR001 mise en panne par supervision
2025-04-08 14:15:00 | Machine PR001 mise en maintenance | Commentaire : Remplacement sonde
```

Vous pouvez **sauvegarder** ce journal ou **charger** un ancien journal.

---

## 7. Rapports industriels

Ce menu génère un **instantané** de l'état de votre atelier.

### Exemple de rapport :

```
========= RAPPORT INDUSTRIEL =========
Machines totales : 5
En service       : 3
En panne         : 1
En maintenance   : 1
Alertes détectées: 1
Dernier incident : 2025-04-08 14:12:05 | Machine PR001 mise en panne par supervision
```

C’est l’outil idéal pour un **briefing rapide** en début de poste.

---

## Comment sont stockées les données ?

Pas besoin de base de données complexe ! Tout est sauvegardé dans des **fichiers texte** simples, dans le dossier `data/` :

| Fichier           | Contenu                                       |
| ----------------- | --------------------------------------------- |
| `machines.txt`    | ID;Nom;État                                   |
| `sensors.txt`     | ID;Type;Valeur;Seuil_min;Seuil_max;Machine_ID |
| `maintenance.txt` | Date;Machine;Nouvel état;Commentaire          |
| `logs.txt`        | Historique complet des événements             |

Vous pouvez ouvrir ces fichiers avec le Bloc-notes pour voir les données brutes.

---

## Résumé : qui fait quoi ?

| Module           | Rôle principal                                               |
| ---------------- | ------------------------------------------------------------ |
| `main.py`        | Chef d'orchestre : affiche les menus et dirige l'utilisateur |
| `machines.py`    | Gère le cycle de vie des équipements                         |
| `sensors.py`     | Gère les capteurs et leurs mesures                           |
| `supervision.py` | Surveille les seuils et réagit aux anomalies                 |
| `diagnostic.py`  | Analyse les pannes (ex: surchauffe, fuite)                   |
| `maintenance.py` | Gère les interventions techniques                            |
| `logger.py`      | Tient le journal de bord                                     |
| `reports.py`     | Synthétise l'état de l'usine                                 |

---

## Pour commencer

1. Assurez-vous que tous les fichiers (`.py`) sont dans le **même dossier**.
2. Lancez le programme avec la commande :

   ```bash
   python main.py
   ```
3. Le dossier `data/` sera créé automatiquement dès la première sauvegarde.

---

## Un dernier conseil

Pensez à ce système comme à un **tableau de bord virtuel** de votre atelier. Il ne commande pas directement les machines (c’est une simulation), mais il vous apprend la logique des vrais systèmes de supervision industrielle.

Amusez-vous à créer des scénarios :

* Ajoutez 3 machines, 5 capteurs.
* Faites varier les valeurs pour déclencher des pannes.
* Gérez la maintenance.
* Générez un rapport.

Vous verrez, en quelques minutes, vous maîtriserez l'outil !
