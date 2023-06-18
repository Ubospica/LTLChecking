from typing import TextIO
import sys

from ltl_ast import parse_ltl_formula
from ts import TS


def getints(fd: TextIO):
    return [int(i) for i in fd.readline().split()]


def get_TS(fd: TextIO):
    """input a transition system"""
    try:
        n_states, n_transitions = getints(fd)
        states = list(range(n_states))
        init_states = getints(fd)
        acts = getints(fd)
        propositions = fd.readline().split()
        transitions = []
        for _ in range(n_transitions):
            edge = getints(fd)
            transitions.append((states[edge[0]], acts[edge[1]], states[edge[2]]))
        labels = []
        for _ in range(n_states):
            l = getints(fd)
            labels.append([propositions[i] for i in l if i >= 0])
    except (ValueError, IndexError):
        print("Error: Invalid input")
        raise

    return TS(states, init_states, acts, propositions, transitions, labels)


def get_LTLs(fd: TextIO):
    """input LTLs"""
    res = []
    try:
        n_init_formula, n_state_formula = getints(fd)
        for _ in range(n_init_formula):
            res.append((-1, fd.readline()))
        for _ in range(n_state_formula):
            start, formula = fd.readline().split(maxsplit=1)
            res.append((start, formula))
    except (ValueError, IndexError):
        print("Error: Invalid input")
        raise
    return [(start, parse_ltl_formula(formula)) for start, formula in res]


def main():
    # ts_file = sys.stdin
    # ltl_file = sys.stdin
    ts_file = open("TS.txt", "r")
    ltl_file = open("benchmark.txt", "r")
    ts = get_TS(ts_file)
    ltls = get_LTLs(ltl_file)
    print(ts)
    print(ltls)


if __name__ == "__main__":
    main()
