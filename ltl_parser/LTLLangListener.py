# Generated from ltl_parser/LTLLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LTLLangParser import LTLLangParser
else:
    from LTLLangParser import LTLLangParser

# This class defines a complete listener for a parse tree produced by LTLLangParser.
class LTLLangListener(ParseTreeListener):

    # Enter a parse tree produced by LTLLangParser#formula_in_parentheses.
    def enterFormula_in_parentheses(self, ctx:LTLLangParser.Formula_in_parenthesesContext):
        pass

    # Exit a parse tree produced by LTLLangParser#formula_in_parentheses.
    def exitFormula_in_parentheses(self, ctx:LTLLangParser.Formula_in_parenthesesContext):
        pass


    # Enter a parse tree produced by LTLLangParser#logic_formula.
    def enterLogic_formula(self, ctx:LTLLangParser.Logic_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#logic_formula.
    def exitLogic_formula(self, ctx:LTLLangParser.Logic_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#not_formula.
    def enterNot_formula(self, ctx:LTLLangParser.Not_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#not_formula.
    def exitNot_formula(self, ctx:LTLLangParser.Not_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#logic_const.
    def enterLogic_const(self, ctx:LTLLangParser.Logic_constContext):
        pass

    # Exit a parse tree produced by LTLLangParser#logic_const.
    def exitLogic_const(self, ctx:LTLLangParser.Logic_constContext):
        pass


    # Enter a parse tree produced by LTLLangParser#g_formula.
    def enterG_formula(self, ctx:LTLLangParser.G_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#g_formula.
    def exitG_formula(self, ctx:LTLLangParser.G_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#atomic_proposition.
    def enterAtomic_proposition(self, ctx:LTLLangParser.Atomic_propositionContext):
        pass

    # Exit a parse tree produced by LTLLangParser#atomic_proposition.
    def exitAtomic_proposition(self, ctx:LTLLangParser.Atomic_propositionContext):
        pass


    # Enter a parse tree produced by LTLLangParser#u_formula.
    def enterU_formula(self, ctx:LTLLangParser.U_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#u_formula.
    def exitU_formula(self, ctx:LTLLangParser.U_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#x_formula.
    def enterX_formula(self, ctx:LTLLangParser.X_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#x_formula.
    def exitX_formula(self, ctx:LTLLangParser.X_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#implication_formula.
    def enterImplication_formula(self, ctx:LTLLangParser.Implication_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#implication_formula.
    def exitImplication_formula(self, ctx:LTLLangParser.Implication_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#f_formula.
    def enterF_formula(self, ctx:LTLLangParser.F_formulaContext):
        pass

    # Exit a parse tree produced by LTLLangParser#f_formula.
    def exitF_formula(self, ctx:LTLLangParser.F_formulaContext):
        pass


    # Enter a parse tree produced by LTLLangParser#logicConstant.
    def enterLogicConstant(self, ctx:LTLLangParser.LogicConstantContext):
        pass

    # Exit a parse tree produced by LTLLangParser#logicConstant.
    def exitLogicConstant(self, ctx:LTLLangParser.LogicConstantContext):
        pass


    # Enter a parse tree produced by LTLLangParser#true_literal.
    def enterTrue_literal(self, ctx:LTLLangParser.True_literalContext):
        pass

    # Exit a parse tree produced by LTLLangParser#true_literal.
    def exitTrue_literal(self, ctx:LTLLangParser.True_literalContext):
        pass


    # Enter a parse tree produced by LTLLangParser#false_literal.
    def enterFalse_literal(self, ctx:LTLLangParser.False_literalContext):
        pass

    # Exit a parse tree produced by LTLLangParser#false_literal.
    def exitFalse_literal(self, ctx:LTLLangParser.False_literalContext):
        pass



del LTLLangParser