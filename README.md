# bomartoyaml
Bookmark or URL to YAML converter for the awesome gethomepage projekt

# Usage
Input any URL and the Script will generate a YAML Block which is used by https://github.com/gethomepage/homepage.git


# First Description

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

kategorie       # Die Kategorie kann aus den Tags der Webseite extrahiert werden
name            # Der Name wird aus der URL oder dem Titel der Webseite extrahiert
abbr            # Die Abkürzung kann aus den Anfangsbuchstaben des Namens oder der URL bestehen
icon            # Das Icon kommt entweder von simpleicons.org oder es könnte auch von ChatGPT erzeugt werden
description     # ChatGPT soll später die Beschreibung erzeugen
