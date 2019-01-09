
## INPUT CLASSES AND METHODS

class STEPS:
    def __init__(self):
        '''
        Initializes a JSON path and an outline for the output
        '''
    
        self._STEPS = 'DIRECTIONS\n'
        self._path = None
        
    def generate(self, json: 'json'):
        '''
        Generates one line of output for each maneuver that needs to
        be made along the path from the first location to the last
        '''
        
        self._path = json['route']['legs']
        for elements in self._path:
            for maneuvers in elements['maneuvers']:
                self._STEPS += maneuvers['narrative'] + '\n'
        print(self._STEPS)


class TOTALDISTANCE:
    def __init__(self):
        '''
        Initializes a JSON path and an outline for the output
        '''
        
        self._TOTALDISTANCE = None
        self._path = None
        
    def generate(self, json: 'json'):
        '''
        Generates the total distance (in an integer number of miles,
        rounded to the nearest mile) for the entire trip.
        '''
        
        self._path = json['route']
        output = self._path['distance']
        self._TOTALDISTANCE = 'Total Distance: {:.0f} miles\n'.format(output)
        print(self._TOTALDISTANCE)

class TOTALTIME:
    def __init__(self):
        '''
        Initializes a JSON path and an outline for the output
        '''
        
        self._TOTALTIME = ''
        self._path = None
        
    def generate(self, json: 'json'):
        '''
        Generates the total time (in an integer number of minutes,
        rounded to the nearest minute) that would be required
        to take the entire trip
        '''
        
        self._path = json['route']
        self._minutes = self._path['time']/60
        self._TOTALTIME = 'Total Time: {:.0f} minutes\n'.format(self._minutes)
        print(self._TOTALTIME)

class LATLONG:
    def __init__(self):
        '''
        Initializes a JSON path and an outline for the output
        '''
        
        self._LATLONG = ''
        self._preFormat = []
        self._path = None
        
    def generate(self, json: 'json'):
        '''
        Generates an output for the latitude and longitude
        for each of the locations specified in the input,
        in the order specified in the input
        '''
        latOrientation = 'N'
        lngOrientation = 'W'
        self._path = json['route']['legs']
        for latlong in range(len(self._path)):
            self._preFormat.append(self._path[latlong]['maneuvers'][0]['startPoint'])
        self._preFormat.append(self._path[latlong]['maneuvers'][-1]['startPoint'])
        for elements in self._preFormat:
            if elements['lat'] < 0:
                direction = 'S'
                elements['lat'] = elements['lat'] * -1
                
            if elements['lng'] < 0:
                direction = 'E'
                elements['lng'] = elements['lng'] * -1
                
            output = '{:.2f}{} {:.2f}{}'.format(
                elements['lat'],latOrientation,
                elements['lng'],lngOrientation)
            self._LATLONG += output + '\n'
        print(self._LATLONG)
