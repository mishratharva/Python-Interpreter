from Expression import Expression
from Statement import Statement
from Value import Value
from Name import Name


class Interpreter:
    def eval(self, c, e, known_function={}):
        cond = type(c).__name__
        # print(cond)
        if cond == "IntConstant":
            intConst = c.c
            return Value.IntValue(intConst)

        elif cond == "BinOpExpression":
            left = self.eval(c.left, e, known_function)
            right = self.eval(c.right, e, known_function)
            if c.op == Expression.BinOpExpression.Operation.PLUS:
                return Value.IntValue(left.val + right.val)
            elif c.op == Expression.BinOpExpression.Operation.MINUS:
                return Value.IntValue(left.val - right.val)
            elif c.op == Expression.BinOpExpression.Operation.TIMES:
                return Value.IntValue(left.val * right.val)
            elif c.op == Expression.BinOpExpression.Operation.DIV:
                return Value.IntValue(left.val / right.val)

        elif cond == "LetExpression":
            val = self.eval(c.value, e, known_function)
            newE = e.bind(c.variableName, val)

            return self.eval(c.body, newE, known_function)

        elif cond == "VariableExpression":
            return e.lookup(c.variable)

        elif cond == "IncExpression":
            val = e.lookup(c.variableName)
            # e.update(c.variableName, Value.IntValue(val.val + 1))
            e.update(c.variableName, Value.IntValue(val.val + 1))
            return Value.IntValue(val.val + 1)

        elif cond == "VariableExpression":
            return e.lookup(c.variable)

        elif cond == "EqExpression":
            left = self.eval(c.left, e, known_function)
            right = self.eval(c.right, e, known_function)

            if left.val == right.val:
                return Value.BoolValue(1)

            return Value.BoolValue(0)

        elif cond == "NeqExpression":
            left = self.eval(c.left, e, known_function)
            right = self.eval(c.right, e, known_function)

            if left.val != right.val:
                return Value.BoolValue(1)

            return Value.BoolValue(0)

        elif cond == "IfExpression":
            value = self.eval(c.cond, e, known_function)
            if value.val == 1:
                return self.eval(c.thenSide, e, known_function)
            return self.eval(c.elseSide, e, known_function)

        elif cond == "FunctionDeclExpression":
            def f(actualValues):
                env_that_knows_the_arguement = e
                for i in range(len(actualValues)):
                    env_that_knows_the_arguement = env_that_knows_the_arguement.bind(
                        c.formalArguments[i], actualValues[i])
                return self.eval(c.functionBody, env_that_knows_the_arguement, known_function)

            known_function[c.name.theName] = f

            return self.eval(c.scope, e, known_function)

        elif cond == "FunctionCallExpression":
            if c.name.theName in known_function:
                py_function = known_function[c.name.theName]
                actualValues = []
                for i in range(len(c.actualArguments)):
                    actualValues.append(
                        self.eval(c.actualArguments[i], e, known_function))
                return py_function(actualValues)
            else:
                raise Exception("Function Not Exist")

        elif cond == "FirstClassFunctionDeclExpression":
            cc = Value.Closure(e, c.formalArguments, c.functionBody)
            cc.capturedEnvironment = cc.capturedEnvironment.bind(c.name, cc)
            return cc

        elif cond == "FirstClassFunctionCallExpression":
            closure = self.eval(c.functionToBeCalled, e, known_function)

            actualValues = []

            for i in range(len(c.actualArguments)):
                actualValues.append(
                    self.eval(c.actualArguments[i], e, known_function))
            return self.apply(closure, actualValues)

        elif cond == "LambdaDeclExpression":
            cc = Value.Closure(e, c.formalArguments, c.functionBody)
            return cc

        elif cond == "SeqStatement":
            for i in range(len(c.statements) - 1):
                self.eval(c.statements[i], e)

            return self.eval(c.statements[-1], e)

        elif cond == "SetStatement":
            data = self.eval(c.newValue, e)
            e.update(c.variableName, Value.IntValue(data.val))
            return Value.VoidValue()

        elif cond == "WhileStatement":

            g = self.eval(c.guard, e)
            if not g.val:
                return Value.VoidValue()
            self.eval(c.body, e)
            return self.eval(c, e)

        elif cond == "LoopStatement":
            self.eval(c.body, e)
            return self.eval(c, e)

        elif cond == "ReturnStatement":
            a = self.eval(c.value, e)
            raise Statement.ReturnException(a)

    def apply(self, closure, actualValues):
        try:
            env_that_knows_the_arguement = closure.capturedEnvironment
            for i in range(len(actualValues)):
                env_that_knows_the_arguement = env_that_knows_the_arguement.bind(
                    closure.formalArguments[i], actualValues[i])
            return self.eval(closure.functionBody, env_that_knows_the_arguement, {})
        except Exception as err:
            return err
