import goody


def read_fa(file : open) -> {str:{str:str}}:
    return_dict = {}
    for line in file:
        split_line = line.split(';')
        split_line[-1] = split_line[-1].replace('\n','')
        return_dict.update({split_line[0]: {z[0]:z[1] for z in list(zip(split_line[1::2], split_line[2::2]))}})
    return return_dict


def fa_as_str(fa : {str:{str:str}}) -> str:
    pass

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    pass


def interpret(fa_result : [None]) -> str:
    pass




if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
