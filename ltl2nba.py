import itertools
from typing import List, Set, Tuple

from ltl_ast import *
from nba import GNBA, NBA
from ts import LabelType


ClosureType = List[Tuple[LTLNode, LTLNode]]  # [(node, Negation(node))]
ElementSetType = List[Set[LTLNode]]


def powerset(ap: List[LabelType]) -> List[Set[LabelType]]:
    return sum((list(itertools.combinations(ap, n)) for n in range(len(ap) + 1)), [])


class ClosureFinder(LTLVisitor):
    def __init__(self):
        self.closure: ClosureType = []
        self.have_constant = False

    @staticmethod
    def find(expr: LTLNode) -> Tuple[ClosureType, bool]:
        finder = ClosureFinder()
        finder.visit(expr)
        return finder.closure, finder.have_constant

    def visit(self, expr: LTLNode):
        if isinstance(expr, Constant):
            self.have_constant = True
        elif not isinstance(expr, Negation):
            self.closure.append((expr, Negation(expr)))

        if isinstance(expr, Unary):
            self.visit(expr.child)
        elif isinstance(expr, Binary):
            self.visit(expr.left)
            self.visit(expr.right)


def is_consistant(formulas: Set[LTLNode], closure: ClosureType) -> bool:
    for a, _ in closure:
        # Check 1.1
        if isinstance(a, Conjunction):
            flag1 = a in formulas
            flag2 = a.left in formulas and a.right in formulas
            if not flag1 == flag2:
                return False
        # Check 2.1, 2.2
        elif isinstance(a, Until):
            phi1 = a.left
            phi2 = a.right
            if phi2 in formulas and a not in formulas:
                return False
            if a in formulas and phi2 not in formulas and phi1 not in formulas:
                return False
    return True


def get_element_set(ltl: LTLNode) -> Tuple[ElementSetType, ClosureType]:
    closure, have_constant = ClosureFinder.find(ltl)
    iter = itertools.product(*([[0, 1]] * len(closure)))
    element_set = []
    for choice in iter:
        # Check 1.2, 3.1
        formulas = set(closure[i][j] for i, j in enumerate(choice))
        # Check 1.3
        if have_constant:
            formulas.add(Constant(True))
        if is_consistant(formulas, closure):
            element_set.append(formulas)
    return element_set, closure

    # def __init__(
    #     self,
    #     states: List[StateType],
    #     alphabet: List[AlphabetType],
    #     transitions: Union[
    #         List[Tuple[StateType, AlphabetType, StateType]],
    #         Dict[StateType, List[Tuple[AlphabetType, StateType]]],
    #     ],
    #     initial: Set[StateType],
    #     finals: List[Set[StateType]],
    # ):


def ltl2gnba(ltl: LTLNode, ap: Set[LabelType]) -> GNBA:
    """convert an LTL formula to a GNBA"""
    states, closure = get_element_set(ltl)
    alphabet = powerset(ap)
    initial = set(state for state in states if ltl in state)
    finals = []
    for formula, _ in closure:
        if isinstance(formula, Until):
            finals.append(
                set(state for state in states if formula not in state and formula.right in state)
            )
    transitions = []
    for start in states:
        alpha = start.intersection(ap)
        for end in states:
            flag = True
            for formula, _ in closure:
                if isinstance(formula, Next):
                    if (formula in start) != (formula.child in end):
                        flag = False
                        break
                elif isinstance(formula, Until):
                    if (formula in start) != (
                        formula.left in end or formula.right in end or formula in end
                    ):
                        flag = False
                        break
            if flag:
                transitions.append((start, alpha, end))
    return GNBA(states, alphabet, transitions, initial, finals)


def ltl2nba(ltl: LTLNode, ap: Set[LabelType]) -> NBA:
    gnba = ltl2gnba(ltl, ap)
    return gnba.to_nba()


if __name__ == "__main__":
    ltl = parse_ltl_formula("a U (!a /\ b)")
    print(ltl)
    print(ClosureFinder.find(ltl))
