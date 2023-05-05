from Expression import Expression
from Environment import Environment
from Interpreter import Interpreter
from Name import Name
from Statement import Statement

class Program:

    # 474
    p1 = Expression.IntConstant(474)

    # 400 + 74
    p2 = Expression.BinOpExpression(
        Expression.BinOpExpression.Operation.PLUS,
        Expression.IntConstant(400),
        Expression.IntConstant(74)
    )

    # // 400 + (70 + 4)
    p3 = Expression.BinOpExpression(
        Expression.BinOpExpression.Operation.PLUS,
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.IntConstant(70),
            Expression.IntConstant(4)
        )
    )
    # (let var = (400 + 70) in var + 4)
    p4 = Expression.LetExpression(
        Name("var"),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.IntConstant(400),
            Expression.IntConstant(70)
        ),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.VariableExpression(Name("var")),
            Expression.IntConstant(4)
        )
    )

    # // (let v1 = 400 in
    # //    (let v2 = 70 in v2)
    # //    +
    # //    4 + v1
    # // )
    p5 = Expression.LetExpression(
        Name("v1"),
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.LetExpression(
                Name("v2"),
                Expression.IntConstant(70),
                Expression.VariableExpression(Name("v2"))
            ),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.PLUS,
                Expression.IntConstant(4),
                Expression.VariableExpression(Name("v1"))
            )
        )
    )

    # // (let var = 400 in
    # //    (let var = 70 in var)
    # //    +
    # //    4 + var
    # // )
    p6 = Expression.LetExpression(
        Name("var"),
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.LetExpression(
                Name("var"),
                Expression.IntConstant(70),
                Expression.VariableExpression(Name("var"))
            ),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.PLUS,
                Expression.IntConstant(4),
                Expression.VariableExpression(Name("var"))
            )
        )
    )

    # // (let v1 = 400 in
    # //    (let v2 = 70 in v1+v2)
    # //    +
    # //    4
    # // )
    p7 = Expression.LetExpression(
        Name("v1"),
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.LetExpression(
                Name("v2"),
                Expression.IntConstant(70),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.PLUS,
                    Expression.VariableExpression(Name("v1")),
                    Expression.VariableExpression(Name("v2"))
                )
            ),
            Expression.IntConstant(4)
        )
    )

    # // (let divisor = 0 in (divisor == 0))

    p8 = Expression.LetExpression(
        Name("divisor"),
        Expression.IntConstant(0),
        Expression.EqExpression(
            Expression.VariableExpression(Name("divisor")),
            Expression.IntConstant(0)
        )
    )

    # // (let dividend = 474 in
    # //   (let divisor = 2 in
    # //     (divisor == 0) ? 0 : dividend / divisor))

    p9 = Expression.LetExpression(
        Name("dividend"),
        Expression.IntConstant(474),
        Expression.LetExpression(
            Name("divisor"),
            Expression.IntConstant(2),
            Expression.IfExpression(
                Expression.EqExpression(
                    Expression.VariableExpression(Name("divisor")),
                    Expression.IntConstant(0)
                ),
                Expression.IntConstant(0),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.DIV,
                    Expression.VariableExpression(Name("dividend")),
                    Expression.VariableExpression(Name("divisor"))
                )
            )
        )
    )
    # function safeDivision(dividend, divisor) -> (divisor == 0) ? 0 : dividend / divisor))
    # safeDivision(400 + 74,0) + safeDivision(474,1)
    p10 = Expression.FunctionDeclExpression(
        Name("safeDivision"),
        [Name("dividend"),  Name("divisor")],
        Expression.IfExpression(
            Expression.EqExpression(
                Expression.VariableExpression(Name("divisor")),
                Expression.IntConstant(0)
            ),
            Expression.IntConstant(0),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.DIV,
                Expression.VariableExpression(Name("dividend")),
                Expression.VariableExpression(Name("divisor"))
            )
        ),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.FunctionCallExpression(
                Name("safeDivision"),
                [
                    Expression.BinOpExpression(
                        Expression.BinOpExpression.Operation.PLUS,
                        Expression.IntConstant(400),
                        Expression.IntConstant(74)
                    ),
                    Expression.IntConstant(0)
                ]
            ),
            Expression.FunctionCallExpression(
                Name("safeDivision"),
                [
                    Expression.IntConstant(474),
                    Expression.IntConstant(2)
                ]
            )
        )
    )
    #      let error = -1 in
    #        function safeDivision(dividend, divisor) -> (divisor == 0) ? error : dividend / divisor))
    #   let error = -474 in
    #     safeDivision(400 + 74,0) + safeDivision(474,1)
    p11 = Expression.LetExpression(
        Name("error"),
        Expression.IntConstant(-1),
        Expression.FunctionDeclExpression(
            Name("safeDivision"),
            [Name("dividend"),  Name("divisor")],
            Expression.IfExpression(
                Expression.EqExpression(
                    Expression.VariableExpression(Name("divisor")),
                    Expression.IntConstant(0)
                ),
                Expression.VariableExpression(Name("error")),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.DIV,
                    Expression.VariableExpression(Name("dividend")),
                    Expression.VariableExpression(Name("divisor"))
                )
            ),
            Expression.LetExpression(
                Name("error"),
                Expression.IntConstant(-474),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.PLUS,
                    Expression.FunctionCallExpression(
                        Name("safeDivision"),
                        [
                            Expression.BinOpExpression(
                                Expression.BinOpExpression.Operation.PLUS,
                                Expression.IntConstant(400),
                                Expression.IntConstant(74)
                            ),
                            Expression.IntConstant(0)
                        ]
                    ),
                    Expression.FunctionCallExpression(
                        Name("safeDivision"),
                        [
                            Expression.IntConstant(474),
                            Expression.IntConstant(1)
                        ]
                    )
                )
            )
        )
    )

    #     function fact(n) -> ((n == 1) ? 1 : n * fact(n-1))
    #        fact(10)
    p12 = Expression.FunctionDeclExpression(
        Name("fact"),
        [Name("n")],
        Expression.IfExpression(
            Expression.EqExpression(
                Expression.VariableExpression(Name("n")),
                Expression.IntConstant(1)
            ),
            Expression.IntConstant(1),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.TIMES,
                Expression.VariableExpression(Name("n")),
                Expression.FunctionCallExpression(
                    Name("fact"),
                    [
                        Expression.BinOpExpression(
                            Expression.BinOpExpression.Operation.MINUS,
                            Expression.VariableExpression(
                                Name("n")),
                            Expression.IntConstant(1)
                        )
                    ]
                )
            )
        ),
        Expression.FunctionCallExpression(
            Name("fact"),
            [Expression.IntConstant(10)]
        )
    )

#     /let error = -1 in
#       let safeDivision = function safeDivision(dividend, divisor) -> (divisor == 0) ? error : dividend / divisor)) in
    #   let error = -474 in
    #     safeDivision(400 + 74,0) + safeDivision(474,1)
    p13 = Expression.LetExpression(
        Name("error"),
        Expression.IntConstant(-1),
        Expression.LetExpression(
            Name("safeDivision"),
            Expression.FirstClassFunctionDeclExpression(
                Name("safeDivision"),
                [Name("dividend"),  Name("divisor")],
                Expression.IfExpression(
                    Expression.EqExpression(
                        Expression.VariableExpression(Name("divisor")),
                        Expression.IntConstant(0)
                    ),
                    Expression.VariableExpression(Name("error")),
                    Expression.BinOpExpression(
                        Expression.BinOpExpression.Operation.DIV,
                        Expression.VariableExpression(Name("dividend")),
                        Expression.VariableExpression(Name("divisor"))
                    )
                )
            ),
            Expression.LetExpression(
                Name("error"),
                Expression.IntConstant(-474),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.PLUS,
                    Expression.FirstClassFunctionCallExpression(
                        Expression.VariableExpression(Name("safeDivision")),
                        [
                            Expression.BinOpExpression(
                                Expression.BinOpExpression.Operation.PLUS,
                                Expression.IntConstant(
                                    400),
                                Expression.IntConstant(74)
                            ),
                            Expression.IntConstant(0)
                        ]
                    ),
                    Expression.FirstClassFunctionCallExpression(
                        Expression.VariableExpression(Name("safeDivision")),
                        [
                            Expression.IntConstant(474),
                            Expression.IntConstant(1)
                        ]
                    )
                )
            )
        )
    )
#    let fact = function fact(n) -> ((n == 1) ? 1 : n * fact(n-1))
#    fact(10)
    p14 = Expression.LetExpression(
        Name("fact"),
        Expression.FirstClassFunctionDeclExpression(
            Name("fact"),
            [Name("n")],
            Expression.IfExpression(
                Expression.EqExpression(
                    Expression.VariableExpression(Name("n")),
                    Expression.IntConstant(1)
                ),
                Expression.IntConstant(1),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.TIMES,
                    Expression.VariableExpression(Name("n")),
                    Expression.FirstClassFunctionCallExpression(
                        Expression.VariableExpression(Name("fact")),
                        [
                            Expression.BinOpExpression(
                                Expression.BinOpExpression.Operation.MINUS,
                                Expression.VariableExpression(
                                    Name("n")),
                                Expression.IntConstant(1)
                            )
                        ]
                    )
                )
            )
        ),
        Expression.FirstClassFunctionCallExpression(
            Expression.VariableExpression(Name("fact")),
            [Expression.IntConstant(10)]
        )
    )
#        let safeDivisionGenerator = (error) -> function safeDivision(dividend, divisor) -> (divisor == 0) ? error : dividend / divisor)) in
#        let safeDivision-1 = safeDivisionGenerator(-1) in
#        let safeDivision+1 = safeDivisionGenerator(1) in
#        safeDivision-1(474,0) + safeDivision+1(474,0)
    p15 =  Expression.LetExpression(
             Name("safeDivisionGenerator"),
             Expression.LambdaDeclExpression(
                     [Name("error") ],
                     Expression.FirstClassFunctionDeclExpression(
                             Name("safeDivision"),
                             [ Name("dividend"),  Name("divisor")],
                             Expression.IfExpression(
                                     Expression.EqExpression(
                                             Expression.VariableExpression( Name("divisor")),
                                             Expression.IntConstant(0)
                                    ),
                                     Expression.VariableExpression( Name("error")),
                                     Expression.BinOpExpression(
                                            Expression.BinOpExpression.Operation.DIV,
                                             Expression.VariableExpression( Name("dividend")),
                                             Expression.VariableExpression( Name("divisor"))
                                    )
                            )
                    )),
             Expression.LetExpression(
                     Name("safeDivision-1"),
                     Expression.FirstClassFunctionCallExpression(
                             Expression.VariableExpression( Name("safeDivisionGenerator")),
                             [ Expression.IntConstant(-1)]
                    ),
                     Expression.LetExpression(
                             Name("safeDivision+1"),
                             Expression.FirstClassFunctionCallExpression(
                                     Expression.VariableExpression( Name("safeDivisionGenerator")),
                                     [Expression.IntConstant(1)]
                            ),
                             Expression.BinOpExpression(
                                    Expression.BinOpExpression.Operation.PLUS,
                                     Expression.FirstClassFunctionCallExpression(
                                             Expression.VariableExpression( Name("safeDivision-1")),
                                             [Expression.IntConstant(474),  Expression.IntConstant(0) ]
                                    ),
                                     Expression.FirstClassFunctionCallExpression(
                                             Expression.VariableExpression( Name("safeDivision+1")),
                                             [Expression.IntConstant(474),  Expression.IntConstant(0) ]
                                    )
                            )
                    )
            )
    )

#     let count = 0 in (++count + ++count)
    p16 = Expression.LetExpression(
            Name("count"),
            Expression.IntConstant(0),
            Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.PLUS,
                    Expression.IncExpression(Name("count")),
                    Expression.IncExpression(Name("count"))
            )
    )


#     let count = 0 in ++count ; ++count ; ++count ; ++count ; count
    p17 = Expression.LetExpression(
            Name("count"),
            Expression.IntConstant(0),
            Statement.SeqStatement(
                    Expression.IncExpression(Name("count")),
                    Expression.IncExpression(Name("count")),
                    Expression.IncExpression(Name("count")),
                    Expression.IncExpression(Name("count")),
                    Expression.VariableExpression(Name("count"))
            )
    )

        # // let variable = 0 in variable = (400 + 70) ; (variable + 4)
    p18 = Expression.LetExpression(
            Name("variable"),
            Expression.IntConstant(5),
            Statement.SeqStatement(
                    Statement.SetStatement(
                            Name("variable"),
                            Expression.BinOpExpression(
                                    Expression.BinOpExpression.Operation.PLUS,
                                    Expression.IntConstant(400),
                                    Expression.IntConstant(70)
                            )
                    ),
                    Expression.BinOpExpression(
                            Expression.BinOpExpression.Operation.PLUS,
                            Expression.VariableExpression(Name("variable")),
                            Expression.IntConstant(4)
                    )
            )
    )


# #     // let fact = function fact(n) -> { let ret = 1 in let i = 1 in { while (i != n) { ret = ret * i ; ++i; } ; ret } in
# #     //   fact(10)
    p19 = Expression.LetExpression(
            Name("fact"),
            Expression.FirstClassFunctionDeclExpression(
                    Name("fact"),
                    [ Name("n") ],
                    Expression.LetExpression(
                            Name("ret"),
                            Expression.IntConstant(1),
                            Expression.LetExpression(
                                    Name("i"),
                                    Expression.IntConstant(1),
                                    Statement.SeqStatement(
                                            Statement.WhileStatement(
                                                    Expression.NeqExpression(
                                                            Expression.VariableExpression(Name("i")),
                                                            Expression.VariableExpression(Name("n"))
                                                    ),
                                                    Statement.SeqStatement(
                                                            Statement.SetStatement(
                                                                    Name("ret"),
                                                                    Expression.BinOpExpression(
                                                                            Expression.BinOpExpression.Operation.TIMES,
                                                                            Expression.VariableExpression(Name("ret")),
                                                                            Expression.VariableExpression(Name("i"))
                                                                    )
                                                            ),
                                                            Expression.IncExpression(Name("i"))
                                                    )
                                            ),
                                            Expression.VariableExpression(Name("ret"))
                                    )
                            )
                    )
            ),
            Expression.FirstClassFunctionCallExpression(
                    Expression.VariableExpression(Name("fact")),
                    [ Expression.IntConstant(10) ]
            )
    )
    
# #     // let fact = function fact(n) -> { let ret = 1 in let i = 1 in { loop { (i == n) ? return ret : { ret = ret * i ; ++i; } } ; ret/0 } in
# #     //   fact(10)
        
    p20 = Expression.LetExpression(
            Name("fact"),
            Expression.FirstClassFunctionDeclExpression(
                    Name("fact"),
                    [Name("n") ],
                    Expression.LetExpression(
                            Name("ret"),
                            Expression.IntConstant(1),
                            Expression.LetExpression(
                                    Name("i"),
                                    Expression.IntConstant(1),
                                    Statement.SeqStatement(
                                            Statement.LoopStatement(
                                                    Expression.IfExpression(
                                                            Expression.EqExpression(
                                                                    Expression.VariableExpression(Name("n")),
                                                                    Expression.VariableExpression(Name("i"))
                                                            ),
                                                            Statement.ReturnStatement(Expression.VariableExpression(Name("ret"))),
                                                            Statement.SeqStatement(
                                                                    Statement.SetStatement(
                                                                            Name("ret"),
                                                                            Expression.BinOpExpression(
                                                                                    Expression.BinOpExpression.Operation.TIMES,
                                                                                    Expression.VariableExpression(Name("ret")),
                                                                                    Expression.VariableExpression(Name("i"))
                                                                            )
                                                                    ),
                                                                    Expression.IncExpression(Name("i"))
                                                            )
                                                    )),
                                            Expression.BinOpExpression(
                                                    Expression.BinOpExpression.Operation.DIV,
                                                    Expression.VariableExpression(Name("ret")),
                                                    Expression.IntConstant(0)
                                            )
                                    )
                            )
                    )
            ),
            Expression.FirstClassFunctionCallExpression(
                    Expression.VariableExpression(Name("fact")),
                    [ Expression.IntConstant(10) ]
            )
    )


    @staticmethod
    def main():
        environment = Environment(None, None)

        print(Interpreter().eval(Program.p17, environment, {}))


Program.main()
