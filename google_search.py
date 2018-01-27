import requests
import json


NUM_RESULTS = 5
KEY = 'AIzaSyBJZndfl1NXL0oZDsEw2LE3zLNar7etftU'
CX = '002149522544821780182:e6gky6pwac8'

def return_search_results(str_query):
    url = "https://www.googleapis.com/customsearch/v1?"+ \
        'key='+KEY+ \
        '&cx='+CX+ \
        '&q='+ str_query
    response = requests.get(url)
    json_response = json.loads(response.text)
    results = [item['link'] for item in json_response['items']]
    str_results = ''
    for r in results:
        str_results += r+'\n'
    return str_results
