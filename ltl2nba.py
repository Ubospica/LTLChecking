import itertools
from typing import FrozenSet, List, Set, Tuple
from debug import dbgprint

from ltl_ast import *
from nba import GNBA, NBA
from ts import LabelType


ClosureType = List[Tuple[LTLNode, LTLNode]]  # [(node, Negation(node))]
ElementSetType = List[FrozenSet[LTLNode]]


def powerset(ap: List[LabelType]) -> List[FrozenSet[LabelType]]:
    """Return all subsets of ap as a list of frozensets"""
    return map(
        lambda x: frozenset(x),
        sum((list(itertools.combinations(ap, n)) for n in range(len(ap) + 1)), []),
    )


class ClosureFinder(LTLVisitor):
    """Find the closure of a LTL formula. Closure is represented as a list of tuples (a, !a)"""

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
    """Check if a set of formulas is consistant with regard to a given closure"""
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


def get_element_set(ltl: LTLNode, ap: Set[LabelType]) -> Tuple[ElementSetType, ClosureType]:
    """Get the element set of a LTL formula. Element set is represented as a list of frozensets.

    All symbols in ap, and their negations will also be added to the element set"""
    closure, have_constant = ClosureFinder.find(ltl)
    closure = list(
        set(closure + [(AtomicProposition(i), Negation(AtomicProposition(i))) for i in ap])
    )
    iter = itertools.product(*([[0, 1]] * len(closure)))
    element_set = []
    for choice in iter:
        # Check 1.2, 3.1
        formulas = set(closure[i][j] for i, j in enumerate(choice))
        # Check 1.3
        if have_constant:
            formulas.add(Constant(True))
        if is_consistant(formulas, closure):
            element_set.append(frozenset(formulas))
    return element_set, closure


def formula_set_intersect_ap(formulas: FrozenSet[LTLNode], ap: Set[LabelType]):
    """The intersection of formulas and ap. Resquires LabelType == str"""
    return frozenset(
        formula.name
        for formula in formulas
        if isinstance(formula, AtomicProposition) and formula.name in ap
    )


def ltl2gnba(ltl: LTLNode, ap: Set[LabelType]) -> GNBA:
    """convert an LTL formula to a GNBA"""
    states, closure = get_element_set(ltl, ap)
    alphabet = powerset(ap)
    initial = set(state for state in states if ltl in state)
    finals = []
    for formula, _ in closure:
        if isinstance(formula, Until):
            finals.append(
                set(state for state in states if formula not in state or formula.right in state)
            )
    transitions = []
    for start in states:
        alpha = formula_set_intersect_ap(start, ap)
        for end in states:
            flag = True
            for formula, _ in closure:
                if isinstance(formula, Next):
                    if (formula in start) != (formula.child in end):
                        flag = False
                        break
                elif isinstance(formula, Until):
                    if (formula in start) != (
                        formula.right in start or (formula.left in start and formula in end)
                    ):
                        flag = False
                        break
            if flag:
                transitions.append((start, alpha, end))
    return GNBA(states, alphabet, transitions, initial, finals)


def ltl2nba(ltl: LTLNode, ap: Set[LabelType]) -> NBA:
    """convert an LTL formula to am NBA"""
    gnba = ltl2gnba(ltl, ap)
    dbgprint("GNBA: ", gnba)
    nba = gnba.to_nba()
    dbgprint("NBA: ", nba)
    return nba


if __name__ == "__main__":
    ltl = parse_ltl_formula("a U (!a /\ b)")
    print(ltl)
    print(ClosureFinder.find(ltl))
