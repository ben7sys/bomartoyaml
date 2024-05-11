import requests
from bs4 import BeautifulSoup
import yaml

# Funktion, um Titel und Beschreibung von einer URL zu holen
def fetch_title_and_description(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.text if soup.title else 'No Title'
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No description available.'
            return title, description
        else:
            return 'No Title', 'No description available due to fetch error.'
    except Exception:
        return 'No Title', 'Failed to fetch the site.'
    

# Funktion, um eine Icon-URL zu generieren
def icon_url(title):
    base_url = "https://www.google.com/search?tbm=isch&q="
    search_term = title.replace(' ', '+')
    return base_url + search_term


# Hauptfunktion zum Verarbeiten der Textdatei
def process_urls(input_filename, output_filename):
    entries = []
    with open(input_filename, 'r') as file:
        for line in file:
            url = line.strip()
            title, description = fetch_title_and_description(url)
            # Erstelle das YAML-Array-Element
            entry = {
                    title: {
                        'abbr': ''.join(word[0] for word in title.split() if word).upper()[:2],  # Begrenze die Länge auf 2 Zeichen
                        'description': description,
                        'href': url,
                        'icon': icon_url # Generierte Icon-URL
                    }
                }
            
            entries.append(entry)
    
    # Schreibe die gesammelten Einträge in die YAML-Datei
    with open(output_filename, 'w') as yaml_file:
        for entry in entries:
            yaml.dump([entry], yaml_file, default_flow_style=False)
            yaml_file.write('\n')

# Hauptprogramm
if __name__ == '__main__':
    input_filename = 'urls.txt'  # Name der Eingabedatei
    output_filename = 'txtoutput.yaml'  # Name der Ausgabedatei
    process_urls(input_filename, output_filename)
