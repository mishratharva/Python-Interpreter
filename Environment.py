from Binding import Binding


class Environment:
    EMPTY = None
    
    def __init__(self, binding, referencingEnvironment):
        self.binding = binding
        self.referencingEnvironment = referencingEnvironment
    
    def is_empty(self):
        return self.binding == None and self.referencingEnvironment == None
	

    def bind(self, name, value):
        return Environment(Binding(name, value), self)
    
    def __eq__(self,o):
        if not isinstance(o, Environment):
            return False
        return self.binding == o.binding and self.referencingEnvironment == o.referencingEnvironment
    
    def lookup(self, name):
        if self==Environment(None,None):
            raise Exception("No Such Element Exist")	
        if self.binding.name.theName == name.theName:
            return self.binding.value
        return self.referencingEnvironment.lookup(name)
    
    def update(self, name, value):
        if self==Environment(None,None):
            raise Exception("No Such Element Exist")	
        if self.binding.name.theName == name.theName:
            self.binding.value = value
            return
        return self.referencingEnvironment.update(name, value)
	
    def __str__(self):
        return ("Environment { " + str(self.binding) + ", " + str(self.referencingEnvironment) + " } ")    
    


















