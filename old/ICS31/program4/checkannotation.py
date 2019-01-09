from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (raises AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (raise AssertionError) this classes raises AssertionError and prints its
      failure, along with a list of all annotations tried followed by the check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        
        def check_lists_tuples():
            assert isinstance(value, type(annot)), "'{}' failed annotation check(wrong type): value = '{}' was type {} ... should be type {}'".format(param, value, type(value), annot)
            if len(annot) == 1:
                for item in value:
                    self.check(param,annot[0],item,check_history='')
            else:
                assert len(annot) == len(value)
                for item in range(len(value)):
                    self.check(param,annot[item],value[item],check_history='')
        
        def check_dict():
            assert isinstance(value, type(annot)), "'{}' failed annotation check(wrong type): value = '{}' was type {} ... should be type {}'".format(param, value, type(value), annot)
            assert len(annot) == 1, "'{}' annotation inconsistency: dict should have 1 item but had 2 annotation = {}".format(param,annot)
            for item in value.values():
                for annot_item in annot.values():
                    self.check(param,annot_item,item,check_history)
            for key in value.keys():
                for annot_key in annot.keys():
                    self.check(param,annot_key,key,check_history)
                
        def check_set():
            assert isinstance(value, type(annot)), "'{}' failed annotation check(wrong type): value = '{}' was type {} ... should be type {}'".format(param, value, type(value), annot)
            assert len(annot) == 1, "'{}' annotation inconsistency: set should have 1 item but had 2 annotation = {}".format(param,annot)
            for item in value:
                for annot_item in annot:
                    self.check(param,annot_item,item,check_history)
        
        def check_function():
            try:
                assert len(annot.__code__.co_varnames) == 1, "'{}' annotation inconsistency: predicate should have 1 parameter but had 2 predicate = {}".format(param,annot)
                assert annot(value), "'{}' failed annotation check: value = {}\npredicate = {}".format(param,value,annot)
            except Exception as e:
                raise AssertionError("'{}' annotation predicate({}) raised exception\nexception = {}: {}\n{}".format(param,annot,type_as_str(e),e,check_history))
        
        def check_str():

            try:
                assert eval(annot,{param:value}),"ASSERTION ERROR"
            except Exception as e:
                raise AssertionError
            pass

        # Decode annotation and check it 
        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value, annot), "'{}' failed annotation check(wrong type): value = '{}' was type {} ... should be type {}'".format(param, value, type(value), annot)
        
        elif type(annot) is list or type(annot) is tuple:
            check_lists_tuples()
            
        elif type(annot) is dict:
            check_dict()
        
        elif type(annot) is set or type(annot) is frozenset:
            check_set()
            
        elif inspect.isfunction(annot):
            check_function()
        
        elif type(annot) is str:
            check_str()
            
            
        else:
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except AttributeError:
                raise AssertionError("'{}' annotation undecipherable: {}".format(param,annot))
            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError("'{}' annotation predicate({}) raised exception\nexception = {}: {}".format(param,annot,type_as_str(e),e))
            
            
        
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if self.checking_on:
            try:
                # Check the annotation for every parameter (if there is one)
                for item,value in param_arg_bindings().items():
                    self.check(item, self._f.__annotations__[item],value, '')
                # Compute/remember the value of the decorated function
                decorated_result = self._f(value)
                # If 'return' is in the annotation, check it
                if 'return' in self._f.__annotations__:
                    self.check(item, self._f.__annotations__['return'], decorated_result, '')
                # Return the decorated answer
                return decorated_result
                
            # On first AssertionError, print the source lines of the function and reraise 
            except AssertionError:
                #print(80*'-')
                #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
                #    print(l.rstrip())
                #print(80*'-')
                raise 
        else:
            return self._f(*args, **kargs)


if __name__ == '__main__':     
    #an example of testing a simple annotation  
    #===========================================================================
    # def f(x:int): pass
    # f = Check_Annotation(f)
    # f(3)
    # f('a')
    #===========================================================================
    
    import driver
    driver.driver()
        
