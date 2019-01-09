#
# Khuong Tiet 88812261 Project 3 ICS 32 Lab Section 8
#

import api_mapquest
import output_mapquest

###
### Functions
###

def n_locations() -> list:
    '''
    Prints n lines of input that each describe one location
    Each location can be a such such as Irvine, CA,
    an address such as 4545 Campus Dr, Irvine, CA,
    or anything that the MapQuest API will accept as a location
    '''

    num_of_locations = _location_number()
    locations = _n_amount_of_input(num_of_locations)
    
    return locations

def output_generator():
    '''
    Takes an integer and then the same number of inputs as locations
    '''
    
    num_of_output = _number_taker()
    outputs = _n_amount_of_input(num_of_output)
    outputs = _refine_output(outputs)
    
    return outputs

def retrieve_output(listof: list, JSON: 'json'):
    '''
    Retrieves the output from the JSON object based upon user specifications
    and then prints the output
    '''
    
    output = None
    
    try:
        for options in listof:
            output = options.generate(JSON)
    except KeyError:
        print('Response is missing route property; no route found.\n')
        print('The most common cause for this is one of your locations'\
            ' does not existor was not specified in a format that MapQuest supports.')
    else:
        print('Directions Courtesy of MapQuest; '\
          'Map Data Copyright OpenStreetMap Contributors.')                

def user_input() -> list:
    '''
    Runs and handles the user input part of the MapQuest API program
    and then returns an input key to be used for the program
    '''
    
    locations = n_locations()
    outputs = output_generator()
    input_key = [locations, outputs]
    
    return input_key

def run_program(user_input: list):
    '''
    Enters the user input and checks for input error, if none then it prints
    out the outputs that the user specified for
    '''
    
    if type(user_input[-1]) != list:
        print(user_input[-1])
    else:
        url = api_mapquest.build_map_url(user_input[0])
        results = api_mapquest.get_result(url)
        retrieve_output(user_input[-1], results)


###
### Private Functions
###

def _location_number()-> int:
    '''
    Takes an integer whose value is at least 2,alone on a line,
    that specifies how many locations the trip will consist of.
    '''
    
    ERROR = 'Please enter an integer value whose value is at least 2.'
    num_of_locations = 0
    
    while num_of_locations < 2:
        try:
            num_of_locations = _number_taker()
            if num_of_locations < 2:
                print(ERROR)
        except:
            print(ERROR)
            
    return num_of_locations

def _number_taker() -> int:
    '''
    Takes an integer as user input to be used in other functions
    '''
    
    while True:
        try:
            number = int(input())
        except:
            print('Please enter an integer')
        else:
            break
        
    return number

def _n_amount_of_input(n: int) -> list:
    '''
    Takes an n amount of lines as user input and returns a list of the input
    '''
    
    count = 0
    inputs = []
    
    while count < n:
        new_input = input()
        inputs.append(new_input)
        count += 1
        
    return inputs

def _refine_output(output: list):
    '''
    Takes the list of user output commands and turns each string into an
    actual Python object to be used for generating outputs and compiles a
    list of these objects. If an output command is invalid, it does not
    return a list and instead returns an error message.
    '''
    
    for j in range(len(output)):
        if output[j] == 'STEPS':
            output[j] = output_mapquest.STEPS()
        elif output[j] == 'TOTALDISTANCE':
            output[j] = output_mapquest.TOTALDISTANCE()
        elif output[j] == 'TOTALTIME':
            output[j] = output_mapquest.TOTALTIME()
        elif output[j] == 'LATLONG':
            output[j] = output_mapquest.LATLONG()
        else:
            fail = 'Invalid output type: {}'.format(output[j])
            
            return fail
        
    return output


###
### Program call
###

if __name__ == '__main__':
    input_key = user_input()
    print()
    run_program(input_key)
    
