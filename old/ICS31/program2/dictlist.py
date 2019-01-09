from goody import type_as_str  # Useful in some exceptions
from builtins import KeyError

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
    
    def __contains__(self, item):
        for dicts in self.dl:
            for keys in dicts:
                if keys == item:
                    return True
        return False
    
    def __getitem__(self, index):
        return_item = []
        for lists in self.dl:
            if index in lists:
                return_item.append(lists[index])
        if len(return_item) == 0:
            raise KeyError
        else:
            return max(return_item)
    
    def __setitem__(self, index, value): #Re do this
        index_list = []
        for item in range(len(self.dl)):
            if index in self.dl[item]:
                index_list.append(item)
        if len(index_list) == 0:
            self.dl.append({index: value})
            return self.dl[-1]
        self.dl[max(index_list)][index] = value
        return self.dl[max(index_list)][index]
    
    def __delitem__(self,index):
        index_list = []
        for item in range(len(self.dl)):
            if index in self.dl[item]:
                index_list.append(item)
        if len(index_list) == 0:
            raise KeyError
        del self.dl[max(index_list)][index]
        if len(self.dl[max(index_list)]) == 0:
            self.dl.remove([max(index_list)])
            
    def __call__(self, index):
        index_list = []
        return_list = []
        for item in range(len(self.dl)):
            if index in self.dl[item]:
                index_list.append(item)
        if len(index_list) == 0:
            return index_list
        for items in index_list:
            return_list.append((items, self.dl[items][index]))
        return return_list
        
    def __iter__(self):
        self.return_list = sorted([item for item in key] for key in self.dl)
        return self
    
    def __next__(self):
        self.return_list.pop(0)
            
                
    

    
                


            
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests

    d = DictList(dict(a=1,b=2), dict(b=12,c=13))
    """
    print('len(d): ', len(d))
    print('bool(d):', bool(d))
    print('repr(d):', repr(d))
    print(', '.join("'"+x+"'" + ' in d = '+str(x in d) for x in 'abcx'))
    print("d['a']:", d['a'])
    print("d['b']:", d['b'])
    print("d('b'):", d('b'))
    print('iter results:', ', '.join(i for i in d))
    print('item iter results:', ', '.join(str(i) for i in d.items()))
    print('d.collapse():', d.collapse())
    print('d==d:', d==d)
    print('d+d:', d+d)
    print('(d+d).collapse():', (d+d).collapse())
    """
    
    print()
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
