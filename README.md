# bomartoyaml
Bookmark or URL to YAML converter for the awesome gethomepage projekt

# Usage
Input any URL and the Script will generate a YAML Block which is used by https://github.com/gethomepage/homepage.git


# First Description

Bitte hilf mir ein Script zu schreiben.
Ich habe eine Datei mit Urls, Beschreibung, Titel, und weiteren Daten
Die Datei könnte eine txt, csv, json oder eine andere ähnlich textdatei sein
Die Daten in der Datei enthalten immer ein oder mehrere URLs
Die Daten sind nicht durch Komma oder andere Zeichen getrennt


Für jede URL soll ein YAML Array erstellt werden.
Die Arrays für jedes YAML sollen in eine output.yaml anhänglich geschrieben werden.

Das YAML Array hat die folgende Formatierung:
Hauptkategorie:
- Titel-der-URL:
    abbr: UR
    description: URL-Description
    href: URL
    icon: icon.png

hauptkategorie  # Die Kategorie kann Default sein könnte von ChatGPT gefüllt werden
titel           # Der Titel wird aus der URL und oder dem Titel der Webseite extrahiert
abbr            # Die Abkürzung kann aus den Anfangsbuchstaben des Namens oder der URL bestehen
description     # Wenn in der Datei keine Daten verfügbar könnte ChatGPT die Beschreibung erzeugen
icon            # Das Icon kommt entweder von simpleicons.org oder es könnte von ChatGPT erzeugt werden
href            # Das ist die URL die zum Ziel führt


**Beispiel bookmark.yaml:**
```yaml
- Entertainment:
    - YouTube:
        - abbr: YT
          icon: si-youtube-#FF0000
          href: https://youtube.com/
          description: YouTube

    - Twitch:
        - abbr: TW
          icon: si-twitch-#9146FF
          href: https://www.twitch.tv
          description: Twitch
```


