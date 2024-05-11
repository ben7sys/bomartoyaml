import yaml

# URL als Eingabe nehmen
url = input("Bitte geben Sie die URL ein: ")

# URL formatieren
formatierte_url = url.replace("http://", "").replace("www.", "")

# Formatierter URL in einem Diktionsobjekt speichern
data = {"url": formatierte_url}

# Informationen als Eingabe nehmen
kategorie = input("Bitte geben Sie die Kategorie ein: ") # Die Kategorie kann aus den Tags der Webseite extrahiert werden
name = input("Bitte geben Sie den Namen ein: ") # Der Name wird aus der URL oder dem Titel der Webseite extrahiert
abbr = input("Bitte geben Sie die Abkürzung ein: ") # Die Abkürzung kann aus den Anfangsbuchstaben des Namens oder der URL bestehen
icon = input("Bitte geben Sie das Icon ein: ") # Das Icon kommt entweder von simpleicons.org oder es könnte auch von ChatGPT erzeugt werden
description = input("Bitte geben Sie die Beschreibung ein: ") # ChatGPT soll später die Beschreibung erzeugen

# Informationen in einem verschachtelten Diktionsobjekt speichern
data = {
    kategorie: {
        name: {
            "abbr": abbr,
            "icon": icon,
            "href": url,
            "description": description
        }
    }
}

# Diktionsobjekt in eine YAML-Datei schreiben
with open("url.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)