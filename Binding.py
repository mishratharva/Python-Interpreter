class Binding:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __eq__(self,o):
        if not isinstance(o, Binding):
            return False
        return self.name==o.name and self.value==o.value
    
    def __str__(self):
        return ("Binding { " + str(self.name) + ", " + str(self.value) + " } ")