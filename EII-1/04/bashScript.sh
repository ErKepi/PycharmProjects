#!/bin/bash

# Erstellung einer virtuellen Umgebung im Verzeichnis
python3 -m venv venv

# Starten / Aktivieren der virtuellen Umgebung
source venv/bin/activate

#pip updaten, falls Update vorhanden
pip install --upgrade pip

# Vorher angelegte requirements.txt anpingen und Inhalt installieren
pip install -r requirements.txt

# Python-Skript ausfuehren
python EII04.py

# Virtuelle Umgebung stoppen / deaktivieren
deactivate
