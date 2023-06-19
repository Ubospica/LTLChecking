from sre_parse import State
from typing import Any, Dict, Iterator, List, Set, Tuple, Union

StateType = Any
AlphabetType = Any
TransitionType = Dict[StateType, Dict[AlphabetType, Set[StateType]]]


class NBA:
    """Nondeterministic Büchi Automaton"""

    def __init__(
        self,
        states: List[StateType],
        alphabet: Set[AlphabetType],
        transitions: Union[
            List[Tuple[StateType, AlphabetType, StateType]],
            TransitionType,
        ],
        initial: Set[StateType],
        final: Set[StateType],
    ):
        self.states = states
        self.alphabet = set(alphabet)
        self.initial = set(initial)
        if isinstance(transitions, List):
            self.transitions: TransitionType = {s: {} for s in states}
            for s, a, t in transitions:
                if a not in self.transitions[s]:
                    self.transitions[s][a] = set()
                self.transitions[s][a].add(t)
        else:
            self.transitions = transitions

        self.final = set(final)

    def __repr__(self):
        return f"""NBA(
    states={self.states},
    alphabet={self.alphabet},
    transitions={self.transitions},
    initial={self.initial},
    final={self.final}
)"""

    def all_edges(self) -> Iterator[Tuple[StateType, AlphabetType, StateType]]:  # type: ignore
        """Returns all edges of the automaton"""
        for s, edges in self.transitions.items():
            for a, t_set in edges.items():
                for t in t_set:
                    yield (s, a, t)


class GNBA(NBA):
    """Generalized Nondeterministic Büchi Automaton"""

    def __init__(
        self,
        states: List[StateType],
        alphabet: Set[AlphabetType],
        transitions: Union[
            List[Tuple[StateType, AlphabetType, StateType]],
            TransitionType,
        ],
        initial: Set[StateType],
        finals: List[Set[StateType]],
    ):
        self.states = states
        self.alphabet = set(alphabet)
        self.initial = set(initial)
        if isinstance(transitions, List):
            self.transitions: TransitionType = {s: {} for s in states}
            for s, a, t in transitions:
                if a not in self.transitions[s]:
                    self.transitions[s][a] = set()
                self.transitions[s][a].add(t)
        else:
            self.transitions = transitions

        self.finals = list(map(lambda x: set(x), finals))
        if len(self.finals) == 0:
            self.finals.append(set(self.states))

    def __repr__(self):
        return f"""GNBA(
    states={self.states},
    alphabet={self.alphabet},
    transitions={self.transitions},
    initial={self.initial},
    finals={self.finals}
)"""

    def to_nba(self) -> NBA:
        """Converts a GNBA to an NBA"""
        n_finals = len(self.finals)
        states = [(q, i) for q in self.states for i in range(n_finals)]
        initial = [(q, 0) for q in self.initial]
        final = [(q, 0) for q in self.finals[0]]
        alphabet = self.alphabet
        transitions = []
        for i in range(n_finals):
            for s, a, t in self.all_edges():
                enter_new_g = s in self.finals[i]
                new_t = (t, i) if not enter_new_g else (t, i + 1) if i + 1 < n_finals else (t, 0)
                transitions.append(((s, i), a, new_t))
        return NBA(states, alphabet, transitions, initial, final)
