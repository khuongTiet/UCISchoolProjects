from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0,'DictList.__init__:{} is not a dictionary'.format('')
        self.dl = []
        for item in args:
            assert type_as_str(item) == 'dict' and len(item.keys()) > 0,'DictList.__init__:{} is not a dictionary'.format(item)
            self.dl.append(item)
            
    def __len__(self):
        key_len = set()
        for item in self.dl:
            for key in item.keys():
                key_len.update(key)
        return len(key_len)
    
    def __bool__(self):
        return len(self.dl) > 1
    
    def __repr__(self):
        return_string = 'DictList('
        for item in self.dl:
            return_string += str(item)+','
        return_string = return_string[:-1] + ')'
        return return_string
    
    def __contains(self, item):
        return item in self.dl


    
                



##            
##if __name__ == '__main__':
##    #Simple tests before running driver
##    #Put your own test code here to test DictList before doing bsc tests
##
##    d = DictList(dict(a=1,b=2), dict(b=12,c=13))
##    """
##    print('len(d): ', len(d))
##    print('bool(d):', bool(d))
##    print('repr(d):', repr(d))
##    print(', '.join("'"+x+"'" + ' in d = '+str(x in d) for x in 'abcx'))
##    print("d['a']:", d['a'])
##    print("d['b']:", d['b'])
##    print("d('b'):", d('b'))
##    print('iter results:', ', '.join(i for i in d))
##    print('item iter results:', ', '.join(str(i) for i in d.items()))
##    print('d.collapse():', d.collapse())
##    print('d==d:', d==d)
##    print('d+d:', d+d)
##    print('(d+d).collapse():', (d+d).collapse())
##    """
##    
##    print()
##    import driver
##    driver.default_file_name = 'bsc1.txt'
###     driver.default_show_exception=True
###     driver.default_show_exception_message=True
###     driver.default_show_traceback=True
##    driver.driver()
