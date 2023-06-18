# Generated from ltl_parser/LTLLang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        1,
        14,
        48,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        3,
        0,
        24,
        8,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        5,
        0,
        35,
        8,
        0,
        10,
        0,
        12,
        0,
        38,
        9,
        0,
        1,
        1,
        1,
        1,
        3,
        1,
        42,
        8,
        1,
        1,
        2,
        1,
        2,
        1,
        3,
        1,
        3,
        1,
        3,
        0,
        1,
        0,
        4,
        0,
        2,
        4,
        6,
        0,
        1,
        1,
        0,
        12,
        13,
        53,
        0,
        23,
        1,
        0,
        0,
        0,
        2,
        41,
        1,
        0,
        0,
        0,
        4,
        43,
        1,
        0,
        0,
        0,
        6,
        45,
        1,
        0,
        0,
        0,
        8,
        9,
        6,
        0,
        -1,
        0,
        9,
        10,
        5,
        1,
        0,
        0,
        10,
        24,
        3,
        0,
        0,
        10,
        11,
        12,
        5,
        2,
        0,
        0,
        12,
        24,
        3,
        0,
        0,
        9,
        13,
        14,
        5,
        3,
        0,
        0,
        14,
        24,
        3,
        0,
        0,
        8,
        15,
        16,
        5,
        4,
        0,
        0,
        16,
        24,
        3,
        0,
        0,
        7,
        17,
        24,
        3,
        2,
        1,
        0,
        18,
        24,
        5,
        11,
        0,
        0,
        19,
        20,
        5,
        7,
        0,
        0,
        20,
        21,
        3,
        0,
        0,
        0,
        21,
        22,
        5,
        8,
        0,
        0,
        22,
        24,
        1,
        0,
        0,
        0,
        23,
        8,
        1,
        0,
        0,
        0,
        23,
        11,
        1,
        0,
        0,
        0,
        23,
        13,
        1,
        0,
        0,
        0,
        23,
        15,
        1,
        0,
        0,
        0,
        23,
        17,
        1,
        0,
        0,
        0,
        23,
        18,
        1,
        0,
        0,
        0,
        23,
        19,
        1,
        0,
        0,
        0,
        24,
        36,
        1,
        0,
        0,
        0,
        25,
        26,
        10,
        6,
        0,
        0,
        26,
        27,
        5,
        5,
        0,
        0,
        27,
        35,
        3,
        0,
        0,
        6,
        28,
        29,
        10,
        5,
        0,
        0,
        29,
        30,
        7,
        0,
        0,
        0,
        30,
        35,
        3,
        0,
        0,
        6,
        31,
        32,
        10,
        4,
        0,
        0,
        32,
        33,
        5,
        6,
        0,
        0,
        33,
        35,
        3,
        0,
        0,
        5,
        34,
        25,
        1,
        0,
        0,
        0,
        34,
        28,
        1,
        0,
        0,
        0,
        34,
        31,
        1,
        0,
        0,
        0,
        35,
        38,
        1,
        0,
        0,
        0,
        36,
        34,
        1,
        0,
        0,
        0,
        36,
        37,
        1,
        0,
        0,
        0,
        37,
        1,
        1,
        0,
        0,
        0,
        38,
        36,
        1,
        0,
        0,
        0,
        39,
        42,
        3,
        4,
        2,
        0,
        40,
        42,
        3,
        6,
        3,
        0,
        41,
        39,
        1,
        0,
        0,
        0,
        41,
        40,
        1,
        0,
        0,
        0,
        42,
        3,
        1,
        0,
        0,
        0,
        43,
        44,
        5,
        9,
        0,
        0,
        44,
        5,
        1,
        0,
        0,
        0,
        45,
        46,
        5,
        10,
        0,
        0,
        46,
        7,
        1,
        0,
        0,
        0,
        4,
        23,
        34,
        36,
        41,
    ]


class LTLLangParser(Parser):

    grammarFileName = "LTLLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'!'",
        "'G'",
        "'F'",
        "'X'",
        "'U'",
        "'->'",
        "'('",
        "')'",
        "'true'",
        "'false'",
        "<INVALID>",
        "'/\\'",
        "'\\/'",
    ]

    symbolicNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "Identifier",
        "AndOp",
        "OrOp",
        "WS",
    ]

    RULE_formula = 0
    RULE_logicConstant = 1
    RULE_true_literal = 2
    RULE_false_literal = 3

    ruleNames = ["formula", "logicConstant", "true_literal", "false_literal"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    Identifier = 11
    AndOp = 12
    OrOp = 13
    WS = 14

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class FormulaContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return LTLLangParser.RULE_formula

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class Formula_in_parenthesesContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLLangParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFormula_in_parentheses"):
                listener.enterFormula_in_parentheses(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFormula_in_parentheses"):
                listener.exitFormula_in_parentheses(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFormula_in_parentheses"):
                return visitor.visitFormula_in_parentheses(self)
            else:
                return visitor.visitChildren(self)

    class Logic_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.op = None  # Token
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLLangParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLLangParser.FormulaContext, i)

        def AndOp(self):
            return self.getToken(LTLLangParser.AndOp, 0)

        def OrOp(self):
            return self.getToken(LTLLangParser.OrOp, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLogic_formula"):
                listener.enterLogic_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLogic_formula"):
                listener.exitLogic_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLogic_formula"):
                return visitor.visitLogic_formula(self)
            else:
                return visitor.visitChildren(self)

    class Not_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLLangParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNot_formula"):
                listener.enterNot_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNot_formula"):
                listener.exitNot_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNot_formula"):
                return visitor.visitNot_formula(self)
            else:
                return visitor.visitChildren(self)

    class Logic_constContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicConstant(self):
            return self.getTypedRuleContext(LTLLangParser.LogicConstantContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLogic_const"):
                listener.enterLogic_const(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLogic_const"):
                listener.exitLogic_const(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLogic_const"):
                return visitor.visitLogic_const(self)
            else:
                return visitor.visitChildren(self)

    class G_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLLangParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterG_formula"):
                listener.enterG_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitG_formula"):
                listener.exitG_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitG_formula"):
                return visitor.visitG_formula(self)
            else:
                return visitor.visitChildren(self)

    class Atomic_propositionContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LTLLangParser.Identifier, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtomic_proposition"):
                listener.enterAtomic_proposition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtomic_proposition"):
                listener.exitAtomic_proposition(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtomic_proposition"):
                return visitor.visitAtomic_proposition(self)
            else:
                return visitor.visitChildren(self)

    class U_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLLangParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLLangParser.FormulaContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterU_formula"):
                listener.enterU_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitU_formula"):
                listener.exitU_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitU_formula"):
                return visitor.visitU_formula(self)
            else:
                return visitor.visitChildren(self)

    class X_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLLangParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterX_formula"):
                listener.enterX_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitX_formula"):
                listener.exitX_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitX_formula"):
                return visitor.visitX_formula(self)
            else:
                return visitor.visitChildren(self)

    class Implication_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLLangParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLLangParser.FormulaContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterImplication_formula"):
                listener.enterImplication_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitImplication_formula"):
                listener.exitImplication_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitImplication_formula"):
                return visitor.visitImplication_formula(self)
            else:
                return visitor.visitChildren(self)

    class F_formulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLLangParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLLangParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterF_formula"):
                listener.enterF_formula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitF_formula"):
                listener.exitF_formula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitF_formula"):
                return visitor.visitF_formula(self)
            else:
                return visitor.visitChildren(self)

    def formula(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLLangParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = LTLLangParser.Not_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(LTLLangParser.T__0)
                self.state = 10
                self.formula(10)
                pass
            elif token in [2]:
                localctx = LTLLangParser.G_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(LTLLangParser.T__1)
                self.state = 12
                self.formula(9)
                pass
            elif token in [3]:
                localctx = LTLLangParser.F_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LTLLangParser.T__2)
                self.state = 14
                self.formula(8)
                pass
            elif token in [4]:
                localctx = LTLLangParser.X_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(LTLLangParser.T__3)
                self.state = 16
                self.formula(7)
                pass
            elif token in [9, 10]:
                localctx = LTLLangParser.Logic_constContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.logicConstant()
                pass
            elif token in [11]:
                localctx = LTLLangParser.Atomic_propositionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(LTLLangParser.Identifier)
                pass
            elif token in [7]:
                localctx = LTLLangParser.Formula_in_parenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(LTLLangParser.T__6)
                self.state = 20
                self.formula(0)
                self.state = 21
                self.match(LTLLangParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = LTLLangParser.U_formulaContext(
                            self, LTLLangParser.FormulaContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 25
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 26
                        self.match(LTLLangParser.T__4)
                        self.state = 27
                        self.formula(6)
                        pass

                    elif la_ == 2:
                        localctx = LTLLangParser.Logic_formulaContext(
                            self, LTLLangParser.FormulaContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == 12 or _la == 13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.formula(6)
                        pass

                    elif la_ == 3:
                        localctx = LTLLangParser.Implication_formulaContext(
                            self, LTLLangParser.FormulaContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        self.match(LTLLangParser.T__5)
                        self.state = 33
                        self.formula(5)
                        pass

                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LogicConstantContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def true_literal(self):
            return self.getTypedRuleContext(LTLLangParser.True_literalContext, 0)

        def false_literal(self):
            return self.getTypedRuleContext(LTLLangParser.False_literalContext, 0)

        def getRuleIndex(self):
            return LTLLangParser.RULE_logicConstant

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLogicConstant"):
                listener.enterLogicConstant(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLogicConstant"):
                listener.exitLogicConstant(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLogicConstant"):
                return visitor.visitLogicConstant(self)
            else:
                return visitor.visitChildren(self)

    def logicConstant(self):

        localctx = LTLLangParser.LogicConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_logicConstant)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.true_literal()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.false_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class True_literalContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return LTLLangParser.RULE_true_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTrue_literal"):
                listener.enterTrue_literal(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTrue_literal"):
                listener.exitTrue_literal(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTrue_literal"):
                return visitor.visitTrue_literal(self)
            else:
                return visitor.visitChildren(self)

    def true_literal(self):

        localctx = LTLLangParser.True_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_true_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(LTLLangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class False_literalContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return LTLLangParser.RULE_false_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFalse_literal"):
                listener.enterFalse_literal(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFalse_literal"):
                listener.exitFalse_literal(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFalse_literal"):
                return visitor.visitFalse_literal(self)
            else:
                return visitor.visitChildren(self)

    def false_literal(self):

        localctx = LTLLangParser.False_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_false_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(LTLLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx: FormulaContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 6)

        if predIndex == 1:
            return self.precpred(self._ctx, 5)

        if predIndex == 2:
            return self.precpred(self._ctx, 4)
