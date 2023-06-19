import itertools
from typing import Callable, List, Set, Tuple
from debug import dbgprint
from ltl2nba import ltl2nba
from ltl_ast import Negation

import nba as nba_module
import ts as ts_module
from nba import NBA
from ts import TS

PhiType = Callable[[Set[nba_module.StateType]], bool]


def prod_ts_nba(ts: TS, nba: NBA) -> Tuple[TS, PhiType]:
    """Product of a TS and an NBA"""
    states = list(itertools.product(ts.states, nba.states))
    init_states = set()
    for s in ts.init_states:
        for q in nba.initial:
            label = ts.labels[s]
            if label in nba.transitions[q]:
                init_states.update((s, t) for t in nba.transitions[q][label])
    ap = nba.states

    transitions = []
    for s in ts.states:
        for a, t_set in ts.transitions[s].items():
            for t in t_set:
                for q in nba.states:
                    label = ts.labels[t]
                    if label in nba.transitions[q]:
                        transitions.extend(
                            ((s, q), a, (t, q_new)) for q_new in nba.transitions[q][label]
                        )

    labels = {}
    for s in states:
        labels[s] = set([s[1]])

    phi: PhiType = lambda label: len(label.intersection(nba.final)) == 0
    return TS(states, init_states, ts.acts, ap, transitions, labels), phi


def persistance_checking(ts: TS, phi: PhiType) -> Tuple[bool, List[ts_module.StateType]]:
    """Check TS |= P_pers(phi)"""
    stack_out = []
    visited_out = set()
    stack_in = []
    visited_in = set()

    def cycle_check(s: ts_module.StateType, init_s: ts_module.StateType) -> bool:
        if s in visited_in:
            return False
        stack_in.append(s)
        visited_in.add(s)
        for t_set in ts.transitions[s].values():
            for t in t_set:
                if t == init_s:
                    stack_in.append(t)
                    return True
                elif cycle_check(t, init_s):
                    return True
        stack_in.pop()
        return False

    def reachable_cycle(s: ts_module.StateType) -> bool:
        if s in visited_out:
            return False
        stack_out.append(s)
        visited_out.add(s)
        for t_set in ts.transitions[s].values():
            for t in t_set:
                if reachable_cycle(t):
                    return True
        stack_out.pop()
        if not phi(ts.labels[s]):
            if cycle_check(s, s):
                return True

    for s in ts.init_states:
        if s in visited_out:
            continue
        if reachable_cycle(s):
            return False, stack_out + stack_in

    return True, []


def check_satisfy(ts: TS, nba: NBA) -> Tuple[bool, List[ts_module.StateType]]:
    ts_prod, phi = prod_ts_nba(ts, nba)
    dbgprint("prod ts: ", ts_prod)
    return persistance_checking(ts_prod, phi)


def check_satisfy_ltl(ts: TS, ltl: str) -> Tuple[bool, List[ts_module.StateType]]:
    negation = ltl.child if isinstance(ltl, Negation) else Negation(ltl)
    nba = ltl2nba(negation, ts.propositions)
    return check_satisfy(ts, nba)
