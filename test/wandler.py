import yaml

# Zuordnung von URLs zu ihrem Namen und weiteren Attributen
# Beispielformatierung:
#            sites = {
#                "https://youtube.com/": {
#                    "name": "YouTube",
#                    "abbr": "YT",
#                    "icon": "si-youtube-#FF0000",
#                    "description": "YouTube"
#                },
#                "https://www.twitch.tv": {
#                    "name": "Twitch",
#                    "abbr": "TW",
#                    "icon": "si-twitch-#9146FF",
#                    "description": "Twitch"
#                }
#            }


# Funktion zum Formatieren der URLs aus einem Textdokument
def process_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
    
    
    formatted_data = {"$Hauptkategorie": []}
    
    for url in urls:
        formatted_site = generate_format(url)
        if formatted_site:
            formatted_data["$Hauptkategorie"].append(formatted_site)

    with open('output.yaml', 'w') as file:
        yaml.dump(formatted_data, file, allow_unicode=True)


sites = {
    "https://youtube.com/": {
        "name": "YouTube",
        "abbr": "YT",
        "icon": "si-youtube-#FF0000",
        "description": "YouTube"
    },
    "https://www.twitch.tv": {
        "name": "Twitch",
        "abbr": "TW",
        "icon": "si-twitch-#9146FF",
        "description": "Twitch"
    }
}

def generate_format(url):
    site_info = sites.get(url.strip())
    if site_info:
        return {
            site_info["name"]: {
                "abbr": site_info["abbr"],
                "icon": site_info["icon"],
                "href": url.strip(),
                "description": site_info["description"]
            }
        }
    else:
        return None

# Dateiname der Eingabe-Textdatei
input_filename = 'urls.txt'
process_file(input_filename)