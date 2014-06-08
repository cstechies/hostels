from bson.json_util import loads
import requests
from Web.models import Hostels
import config

__author__ = 'Abhinav'


def getPlacesBy(query):
    results = ""
    iterate = True
    token = None
    page = 0
    while iterate:
        data = placeSearch(query,nextPageToken=token)
        for result in data["results"]:
            results += result["name"]+"\n"
            print result["name"]," INSERTED"
            insertPlaceToDB(result)
        page += 1
        # if page >= 15:
        #     break
        if "next_page_token" in data:
            token = data["next_page_token"]
        else:
            iterate = False
        if "error_message" in data:
            results += data["error_message"]
    print results
    return results

def insertPlaceToDB(result):
    rating = 2
    if "rating" in result:
        rating = result["rating"]
    hostel = Hostels(name=result["name"],
                    avgRating = rating,
                    gmapsReference = result["reference"],
                    address = result["formatted_address"],
                    latitude = result["geometry"]["location"]["lat"],
                    longitude = result["geometry"]["location"]["lng"],
                    )
    hostel.save()

def placeSearch(query,nextPageToken=None):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&sensor=true&key="+config.MAPS_PLACES_KEY
    if nextPageToken:
        url += "&pagetoken="+nextPageToken
    response = requests.get(url)
    return loads(response.content)