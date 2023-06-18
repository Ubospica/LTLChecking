# Generated from ltl_parser/LTLLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LTLLangParser import LTLLangParser
else:
    from LTLLangParser import LTLLangParser

# This class defines a complete generic visitor for a parse tree produced by LTLLangParser.

class LTLLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LTLLangParser#formula_in_parentheses.
    def visitFormula_in_parentheses(self, ctx:LTLLangParser.Formula_in_parenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#logic_formula.
    def visitLogic_formula(self, ctx:LTLLangParser.Logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#not_formula.
    def visitNot_formula(self, ctx:LTLLangParser.Not_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#logic_const.
    def visitLogic_const(self, ctx:LTLLangParser.Logic_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#g_formula.
    def visitG_formula(self, ctx:LTLLangParser.G_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#atomic_proposition.
    def visitAtomic_proposition(self, ctx:LTLLangParser.Atomic_propositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#u_formula.
    def visitU_formula(self, ctx:LTLLangParser.U_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#x_formula.
    def visitX_formula(self, ctx:LTLLangParser.X_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#implication_formula.
    def visitImplication_formula(self, ctx:LTLLangParser.Implication_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#f_formula.
    def visitF_formula(self, ctx:LTLLangParser.F_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#logicConstant.
    def visitLogicConstant(self, ctx:LTLLangParser.LogicConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#true_literal.
    def visitTrue_literal(self, ctx:LTLLangParser.True_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLLangParser#false_literal.
    def visitFalse_literal(self, ctx:LTLLangParser.False_literalContext):
        return self.visitChildren(ctx)



del LTLLangParser
