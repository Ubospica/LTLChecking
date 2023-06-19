from ltl_parser import LTLLangParser, LTLLangVisitor, LTLLangParser


class LTLNode:
    def tostr(self) -> str:
        return str(self) if isinstance(self, Atomic) else "(" + str(self) + ")"

    def __repr__(self):
        raise NotImplementedError

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, other) -> bool:
        return repr(self) == repr(other)


class Atomic(LTLNode):
    pass


class Unary(LTLNode):
    def __init__(self, child: LTLNode):
        self.child = child


class Binary(LTLNode):
    def __init__(self, left: LTLNode, right: LTLNode):
        self.left = left
        self.right = right


class AtomicProposition(Atomic):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Constant(Atomic):
    def __init__(self, value: bool):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Negation(Unary):
    def __repr__(self):
        return "!" + self.child.tostr()


class Conjunction(Binary):
    def __repr__(self):
        return self.left.tostr() + " /\\ " + self.right.tostr()


class Disjunction(Binary):
    def __repr__(self):
        return self.left.tostr() + " \\/ " + self.right.tostr()


class Implication(Binary):
    def __repr__(self):
        return self.left.tostr() + " -> " + self.right.tostr()


class Next(Unary):
    def __repr__(self):
        return "(=)" + self.child.tostr()


class Always(Unary):
    def __repr__(self):
        return "[]" + self.child.tostr()


class Eventually(Unary):
    def __repr__(self):
        return "<>" + self.child.tostr()


class Until(Binary):
    def __repr__(self):
        return self.left.tostr() + " U " + self.right.tostr()


class LTLBuilder(LTLLangVisitor):
    # Visit a parse tree produced by LTLLangParser#formula_in_parentheses.
    def visitFormula_in_parentheses(self, ctx: LTLLangParser.Formula_in_parenthesesContext):
        return self.visit(ctx.children[1])

    # Visit a parse tree produced by LTLLangParser#logic_formula.
    def visitLogic_formula(self, ctx: LTLLangParser.Logic_formulaContext):
        Node = Conjunction if ctx.children[1].getText() == "/\\" else Disjunction
        return Node(self.visit(ctx.children[0]), self.visit(ctx.children[2]))

    # Visit a parse tree produced by LTLLangParser#not_formula.
    def visitNot_formula(self, ctx: LTLLangParser.Not_formulaContext):
        return Negation(self.visit(ctx.children[1]))

    # Visit a parse tree produced by LTLLangParser#logic_const.
    def visitLogic_const(self, ctx: LTLLangParser.Logic_constContext):
        return Constant(True) if ctx.children[0].getText() == "true" else Constant(False)

    # Visit a parse tree produced by LTLLangParser#g_formula.
    def visitG_formula(self, ctx: LTLLangParser.G_formulaContext):
        return Always(self.visit(ctx.children[1]))

    # Visit a parse tree produced by LTLLangParser#atomic_proposition.
    def visitAtomic_proposition(self, ctx: LTLLangParser.Atomic_propositionContext):
        return AtomicProposition(ctx.children[0].getText())

    # Visit a parse tree produced by LTLLangParser#u_formula.
    def visitU_formula(self, ctx: LTLLangParser.U_formulaContext):
        return Until(self.visit(ctx.children[0]), self.visit(ctx.children[2]))

    # Visit a parse tree produced by LTLLangParser#x_formula.
    def visitX_formula(self, ctx: LTLLangParser.X_formulaContext):
        return Next(self.visit(ctx.children[1]))

    # Visit a parse tree produced by LTLLangParser#implication_formula.
    def visitImplication_formula(self, ctx: LTLLangParser.Implication_formulaContext):
        return Implication(self.visit(ctx.children[0]), self.visit(ctx.children[2]))

    # Visit a parse tree produced by LTLLangParser#f_formula.
    def visitF_formula(self, ctx: LTLLangParser.F_formulaContext):
        return Eventually(self.visit(ctx.children[1]))


class LTLVisitor:
    def visit(self, expr: LTLNode):
        pass


class LTLSimplifier(LTLVisitor):
    def visit(self, expr: LTLNode):
        if isinstance(expr, Atomic):
            return expr
        elif isinstance(expr, Negation):
            child = self.visit(expr.child)
            if isinstance(child, Negation):
                return child.child
            elif isinstance(child, Constant):
                return Constant(not child.value)
            return Negation(child)
        elif isinstance(expr, Conjunction):
            left = self.visit(expr.left)
            right = self.visit(expr.right)
            return Conjunction(left, right)
        elif isinstance(expr, Disjunction):
            left = self.visit(expr.left)
            right = self.visit(expr.right)
            return self.visit(Negation(Conjunction(Negation(left), Negation(right))))
        elif isinstance(expr, Implication):
            left = self.visit(expr.left)
            right = self.visit(expr.right)
            return self.visit(Negation(Conjunction(left, Negation(right))))
        elif isinstance(expr, Next):
            child = self.visit(expr.child)
            return Next(child)
        elif isinstance(expr, Always):
            child = self.visit(expr.child)
            return self.visit(Negation(Eventually(Negation(child))))
        elif isinstance(expr, Eventually):
            child = self.visit(expr.child)
            return self.visit(Until(Constant(True), child))
        elif isinstance(expr, Until):
            left = self.visit(expr.left)
            right = self.visit(expr.right)
            return Until(left, right)

        return expr


def parse_ltl_formula(formula: str) -> LTLNode:
    from ltl_parser.LTLLangLexer import LTLLangLexer
    from ltl_parser.LTLLangParser import LTLLangParser
    from antlr4 import CommonTokenStream, InputStream

    input_stream = InputStream(formula)
    lexer = LTLLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LTLLangParser(token_stream)
    tree = parser.formula()
    expr = LTLBuilder().visit(tree)
    simplified = LTLSimplifier().visit(expr)
    return simplified


if __name__ == "__main__":
    formula = "G((a /\ b) -> (c \/ d)) U (e /\ f /\ true /\ !false) "
    print(parse_ltl_formula(formula))
