class Value:

    class IntValue:
            def __init__(self, val):
                self.val = val

            def __str__(self):
                return "IntValue{" + "val=" + str(self.val) + '}'

    class VoidValue:

            def __str__(self):
                return "IntValue{" + "val= void"  '}'

    class BoolValue:
            def __init__(self, val):
                self.val = val

            def __str__(self):
                return "BoolValue{" + "val=" + str(self.val) + '}'

    class FunctionValue:
            def __init__(self, pyFunction):
                self.pyFunction = pyFunction
        
    class Closure:
            def __init__(self, capturedEnvironment, formalArguments, functionBody):
                self.capturedEnvironment = capturedEnvironment
                self.formalArguments = formalArguments
                self.functionBody = functionBody

