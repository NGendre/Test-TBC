import requests
import json

url = 'http://www.omdbapi.com/?apikey=e5675762&'

def sendQuery(strParameters):
    req = requests.get("http://www.omdbapi.com/?apikey=e5675762&"+strParameters);
    return req.json()