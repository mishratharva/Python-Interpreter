from enum import Enum 

class Expression:

    class IntConstant:
        def __init__(self, c):
            self.c = c
    
    class BinOpExpression:
        class Operation:
            PLUS = 1
            MINUS = 2
            TIMES = 3
            DIV = 4

        def __init__(self, op, left, right):
            self.left = left
            self.right = right
            self.op = op
    
    class LetExpression:
        def __init__(self, variableName, value, body):
            self.variableName = variableName
            self.value = value
            self.body = body
    
    class VariableExpression:
        def __init__(self, variable):
            self.variable = variable

    class EqExpression:
        def __init__(self, left, right):
            self.left = left
            self.right = right
    
    class NeqExpression:
        def __init__(self, left, right):
            self.left = left
            self.right = right

    class IfExpression:
        def __init__(self, cond, thenSide, elseSide):
            self.cond = cond
            self.thenSide = thenSide
            self.elseSide = elseSide

    class FunctionDeclExpression:
        def __init__(self, name, formalArguments, functionBody, scope):
            self.name = name
            self.formalArguments = formalArguments
            self.functionBody = functionBody
            self.scope = scope 

    class FunctionCallExpression:
        def __init__(self, name, actualArguments):
            self.name = name;
            self.actualArguments = actualArguments;
        
    
    class FirstClassFunctionDeclExpression:
        def __init__(self, name, formalArguments, functionBody):
            self.name = name
            self.formalArguments = formalArguments
            self.functionBody = functionBody
    
    class FirstClassFunctionCallExpression:
        def __init__(self, functionToBeCalled, actualArguments):
            self.functionToBeCalled = functionToBeCalled
            self.actualArguments = actualArguments
    
    class IncExpression:
        def __init__(self, variableName):
            self.variableName = variableName

    class LambdaDeclExpression:
        def __init__(self, formalArguments, functionBody):
            self.formalArguments = formalArguments
            self.functionBody = functionBody
