import re, traceback, keyword, prompt
from keyword import kwlist

def pnamedtuple(type_name, field_names, mutable=False):
    re_test = re.compile('^\D\w*$')
    if not re_test.match(str(type_name)):
        raise SyntaxError
    if type(field_names) != list and type(field_names) != str:
        raise SyntaxError
    if type(field_names) == str:
        field_names = re.split(' *|,',field_names)
    for item in field_names:
        if not re_test.match(item) or item in kwlist:
            raise SyntaxError
    
    
    def show_listing(s):
        for i, l in enumerate(s.split('\n'),1):
            print('{num: >3} {text}'.format(num= i, text= l.rstrip()))
    

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_definition = '''\
class {class_name}:
    def __init__(self, field_names, mutable=False):
        self.type_name = type_name
        self.field_names
    '''.format(class_name = type_name)


    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local name-space and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError,TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]



if __name__ == '__main__':
    import driver
    driver.driver()
