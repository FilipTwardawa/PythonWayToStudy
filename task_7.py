# For those willing to create a python script that connects to an API that
# contains information about breweries (documentation
# https://www.openbrewerydb.org/documentation).
# You should make a class in python
# Brawery , which will contain such attributes that the API provides along with the
# appropriate typing.
# In the class you should implement the magic method
# __str__ which will describe the data stored in the object.
# The script is to connect to the API and retrieve the first 20 objects, and then
# create a list of 20 instances of the class
# Brawery , which it will #iterate and display each object individually.
#
# Arithmetic operators, logical operators and typing 4
#
# 8. For those willing Extend the script from point 7 to accept the parameter city ,
# which can be passed on the command line during execution (e.g.
# python main.py --city=Berlin ). Use the argparse module to
# load the passed parameters, and if passed a value
# limit the fetched brews to the city that was indicated.

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
