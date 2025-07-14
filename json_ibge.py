import requests
import json
from tqdm import tqdm

geojson_collection = {
    "type": "FeatureCollection",
    "features": []
}

# Códigos das 5 grandes regiões do IBGE
codigos_regioes = [1, 2, 3, 4, 5]

for codigo in tqdm(codigos_regioes):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/regioes/{codigo}?formato=application/vnd.geo+json&qualidade=maxima"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        geojson_data = response.json()

        # Garante que o GeoJSON retornado tem estrutura FeatureCollection
        if geojson_data["type"] == "FeatureCollection":
            geojson_collection["features"].extend(geojson_data["features"])
        elif geojson_data["type"] == "Feature":
            geojson_collection["features"].append(geojson_data)
        else:
            print(f"⚠️ Estrutura inesperada para a região {codigo}")
    else:
        print(f"❌ Erro ao baixar a região {codigo}: {response.status_code}")

# Salvar o GeoJSON completo com as 5 regiões
with open("geojson_regioes_2022.json", "w", encoding="utf-8") as f:
    json.dump(geojson_collection, f)

print("✅ GeoJSON completo salvo como geojson_regioes_2022.json")
