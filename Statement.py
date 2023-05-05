class Statement:
    class SeqStatement:
        def __init__(self, *statements):
            self.statements = statements

    class SetStatement:
        def __init__(self, variableName, newValue):
            self.variableName = variableName
            self.newValue = newValue

    class WhileStatement:
        def __init__(self, guard, body):
            self.guard = guard
            self.body = body

    class LoopStatement:
        def __init__(self, body):
            self.body = body

    class ReturnStatement:
        def __init__(self, value):
            self.value = value

    class ReturnException(Exception):
        def __init__(self, ret):
            self.ret = ret