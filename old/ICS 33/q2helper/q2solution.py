import re
from goody import irange

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the file pattern.txt


def pages (page_spec : str) -> [int]: #result in ascending order (no duplicates)
    return_list = []
    page_check = re.split(',', page_spec)
    pattern_str = "^(?:(\s*[1-9]+\d*\s*|\s*[1-9]+\s*)(?:(?:([:,-]))([1-9]+\d*\s*|\s+[1-9]\d*\s*)?)?)$"
    object_list = [re.match(pattern_str, ''.join(page_check[query].split())) for query in range(len(page_check))]
    assert object_list != [None]
    for match_object in object_list:
        assert match_object != None
        if match_object.group(2) == '-':
            assert int(match_object.group(1)) < int(match_object.group(3)), 'pages: in page sequence {1}-{0}, {1} > {0}'.format(match_object.group(3),match_object.group(1))
            return_list.extend([page for page in irange(int(match_object.group(1)),int(match_object.group(3)))])
        elif match_object.group(2) == ':':
            return_list.extend([page for page in range(int(match_object.group(1)), int(match_object.group(1)) + int(match_object.group(3)))])
        else:   
            return_list.append(int(match_object.group(1)))
    return sorted(set(return_list))

        

def expand_re(pat_dict:{str:str}):
    pass





if __name__ == '__main__':
    print('Testing  examples of pages that returns lists')
    #pages('4-3')
    print("  pages('5,3,9'): ", pages('5,3,9'))
    print("  pages('3-5,10:2'): ", pages('3-5,10:2'))
    print("  pages('5  -8,10: 3,3'): ", pages('5  -8,10: 3,3'))
         
    print('\nTesting  examples of expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
     
    pd = dict(integer       =r'[+-]?\d+',
              integer_range =r'#integer#(..#integer#)?',
              integer_list  =r'#integer_range#(?,#integer_range#)*',
              integer_set   =r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer'      : '[+-]?\\d+',
    #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
    #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
    #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
    # }
     
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'d': '(((correct)))',
    #  'c': '((correct))',
    #  'b': '(correct)',
    #  'a': 'correct',
    #  'g': '((((((correct))))))',
    #  'f': '(((((correct)))))',
    #  'e': '((((correct))))'
    # }
 
    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
