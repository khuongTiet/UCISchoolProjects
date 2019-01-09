
import json
import urllib.parse
import urllib.request

APP_KEY = 'Fmjtd%7Cluu82161nl%2C70%3Do5-9420lr'

BASE_MAP_URL = 'http://open.mapquestapi.com/directions/v2/route?key=' 

###
### Public functions
###

def build_map_url(locations: list) -> str:
    '''
    Takes a list of locations and provides a URL for use with MapQuest
    based on the locations given to it
    '''

    starting_location = _encode_location(locations[0], 'from')
    MAP_URL = BASE_MAP_URL + APP_KEY + starting_location

    for destinations in locations[1:]:
        MAP_URL += _encode_location(destinations, 'to')
        
    return MAP_URL


def get_result(url: str) -> 'json':
    '''
    Gets the results from the URL and returns it in JSON format
    '''
    
    response = None
    
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()

###
### Private functions
###
            
def _encode_location(location: str, point: str) -> str:
    '''
    Encodes the locations for use in a url to avoid encoding the APP KEY
    '''
    
    encoded_location = '&' + urllib.parse.urlencode([(point, location)])
    
    return encoded_location
