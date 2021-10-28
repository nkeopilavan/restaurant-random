import requests
from flask import render_template, Flask
from config import api_key

my_api_key = api_key


def getRestaurants(search: str):
    search_url = "https://api.yelp.com/v3/businesses/search"
    search_headers = {"Authorization": "bearer %s" % my_api_key}
    search_parameters = {"term":search, "limit": 15, "radius": 10000, "location":"irvine"}

    response = requests.get(url = search_url, params = search_parameters, headers = search_headers)

    results = response.json()

    restaurant_data = []
    for shops in results["businesses"]:
        restaurant_data.append({"name": shops["name"], "address": (shops["location"]["address1"] + " " + shops["location"]["city"] + ", " + shops["location"]["state"] + " " + shops["location"]["zip_code"]), "rating": shops["rating"], "image": shops["image_url"]})

    return restaurant_data