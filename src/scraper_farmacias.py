import requests
import json
import os


def extraer_farmacias():
    # Los dos endpoints del MINSAL
    rutas_api = {
        "Nacionales": "https://midas.minsal.cl/farmacia_v2/WS/getLocales.php",
        "De_Turno": "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'
    }

    directorio_guardado = os.path.join(
        os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(directorio_guardado, exist_ok=True)

    for tipo, url in rutas_api.items():
        print(f"Consultando API para farmacias {tipo}...")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            datos_json = response.json()
            print(f"Se descargaron {len(datos_json)} farmacias {tipo}.")

            nombre_archivo = f"farmacias_{tipo.lower()}.json"
            ruta_guardado = os.path.join(directorio_guardado, nombre_archivo)

            with open(ruta_guardado, 'w', encoding='utf-8') as f:
                json.dump(datos_json, f, ensure_ascii=False, indent=4)

            print(f"Guardado en: {ruta_guardado}\n")
        else:
            print(
                f"Error HTTP {response.status_code} al extraer {tipo}: {response.text}\n")


if __name__ == "__main__":
    extraer_farmacias()
