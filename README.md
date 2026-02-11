# Projet-de-mini-system-SCADA
Système de supervision industrielle en Python permettant la gestion des machines et capteurs, la détection d’anomalies, la mise en maintenance, la génération de rapports et la journalisation des événements. Projet modulaire simulant un environnement industriel avec diagnostic automatique et suivi en temps réel.


Voici une **version optimisée et professionnelle pour GitHub**, prête à copier-coller dans ton `README.md` :

---

# 🏭 Industrial Supervision System (Python)

A modular **industrial supervision system** developed in Python.
This project simulates a simplified SCADA environment for managing machines, sensors, diagnostics, maintenance, logging, and industrial reporting.

---

## 🚀 Features

### ⚙️ Machine Management

* Add / delete machines
* Change machine state (`en_service`, `en_panne`, `maintenance`)
* Persistent storage (JSON)
* Automatic event logging

### 📡 Sensor Management

* Add sensors linked to machines
* Define min/max thresholds
* Modify sensor values
* Automatic anomaly detection
* Persistent storage

### 🖥️ Supervision

* Sensor value input
* Threshold verification
* Production cycle simulation
* Global system state display

### 🚨 Diagnostics & Alarms

* Detect abnormal sensor values
* Generate diagnostic messages:

  * Overheating
  * Overpressure
  * Pressure drop
  * Low temperature
* Automatically switch machines to `en_panne`
* Log all alarm events

### 🔧 Maintenance (Simplified CMMS)

* Set machine to maintenance
* Restore machine to service
* Maintenance status tracking
* Event history recording

### 📘 Event Logging System

* Records:

  * Add / delete / modify actions
  * Alarms
  * Maintenance operations
  * Application start & stop
* Save and load journal
* Incident tracking

### 📊 Industrial Reports

Generates a summary report including:

* Total machines
* Machines by state
* Active alerts
* Last recorded incident

---

## 🏗️ Project Structure

```
.
├── main.py
├── machines.py
├── sensors.py
├── supervision.py
├── diagnostics.py
├── maintenance.py
├── logger.py
├── reports.py
├── machines.json
├── sensors.json
└── journal.json
```

---

## ⚙️ Installation & Usage

### Requirements

* Python 3.8+

### Run the project

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
python main.py
```

No external libraries required (standard Python only).

---

## 🧠 System Logic

1. Data is loaded from JSON files at startup.
2. User interacts via CLI menus.
3. All actions are:

   * Executed
   * Saved
   * Logged
4. Anomalies trigger:

   * Diagnostics
   * Machine state updates
   * Event logging
5. Reports summarize the global system state.

---

## 📌 Machine States

* `en_service`
* `en_panne`
* `maintenance`

---

## 🎓 Purpose

This project is designed for:

* Industrial automation students
* SCADA system simulation
* Python modular architecture practice
* Industrial monitoring system modeling

---

## 🔮 Possible Improvements

* GUI interface (Tkinter / PyQt)
* SQLite database integration
* Real-time dashboard
* REST API
* Modbus simulation
* IoT integration

---

## 👨‍💻 ATANGANA BOREL
