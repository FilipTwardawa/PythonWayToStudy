# Dla chętnych Stworzyć skrypt pythonowy, który połączy się z API, które
# zawiera informacje o browarach (dokumentacja
# https://www.openbrewerydb.org/documentation).
# Należy w pythonie zrobić klasę
# Brawery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
# odpowiednim typowaniem.
# W klasie należy zaimplementować magiczną metodę
# __str__ która będzie opisywała dane przechowywane w obiekcie.
# Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
# utworzyć listę 20 instancji klasy
# Brawery , którą przeiteruje i wyświetli każdy obiekt z osobna.
#
# Operatory arytmetyczne, logiczne i typowanie 4
#
# 8. Dla chętnych Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city ,
# który może być przekazywany w wierszu poleceń podczas wykonywania (np.
# python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
# wczytywania przekazywanych parametrów, a w razie przekazania wartości
# ograniczyć pobierane browary do miasta, które zostało wskazane.

from typing import Optional

import requests
from fastapi import FastAPI, Query

app = FastAPI()


class Brewery:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.brewery_type = data.get('brewery_type')
        self.street = data.get('street')
        self.city = data.get('city')
        self.state = data.get('state')
        self.country = data.get('country')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')


@app.get("/breweries/")
async def get_breweries(city: Optional[str] = Query(None)):
    url = "https://api.openbrewerydb.org/breweries"
    params = {'by_city': city} if city else {}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        breweries = [Brewery(brewery_data) for brewery_data in response.json()[:20]]
        return {"breweries": breweries}
    else:
        return {"error": "Error fetching breweries", "status_code": response.status_code}
