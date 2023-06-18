from typing import Any, Dict, List, Set, Tuple, Union

StateType = Any
AlphabetType = Any


class NBA:
    """Nondeterministic Büchi Automaton"""

    def __init__(
        self,
        states: List[StateType],
        alphabet: List[AlphabetType],
        transitions: Union[
            List[Tuple[StateType, AlphabetType, StateType]],
            Dict[StateType, List[Tuple[AlphabetType, StateType]]],
        ],
        initial: Set[StateType],
        final: Set[StateType],
    ):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial if isinstance(initial, set) else set(initial)
        self.final = final if isinstance(final, set) else set(final)
        if isinstance(transitions, List):
            self.transitions = {}
            for (s, t, a) in transitions:
                if s not in self.transitions:
                    self.transitions[s] = []
                self.transitions[s].append((t, a))
        else:
            self.transitions = transitions

    def __str__(self):
        return f"""NBA(
    states={self.states},
    alphabet={self.alphabet},
    transitions={self.transitions},
    initial={self.initial},
    final={self.final}
)"""


class GNBA:
    """Generalized Nondeterministic Büchi Automaton"""

    def __init__(
        self,
        states: List[StateType],
        alphabet: List[AlphabetType],
        transitions: Union[
            List[Tuple[StateType, AlphabetType, StateType]],
            Dict[StateType, List[Tuple[AlphabetType, StateType]]],
        ],
        initial: Set[StateType],
        finals: List[Set[StateType]],
    ):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial if isinstance(initial, set) else set(initial)
        self.finals = [final if isinstance(final, set) else final for final in finals]
        if isinstance(transitions, List):
            self.transitions = {}
            for (s, a, t) in transitions:
                if s not in self.transitions:
                    self.transitions[s] = []
                self.transitions[s].append((a, t))
        else:
            self.transitions = transitions

    def __str__(self):
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
        initial = [(q, 1) for q in self.initial]
        final = [(q, 1) for q in self.finals[0]]
        alphabet = self.alphabet
        transitions = []
        for i in range(n_finals):
            for s, edges in self.transitions.items():
                enter_new_g = s in self.finals[i]
                for a, t in edges:
                    new_t = (
                        (t, i) if not enter_new_g else (t, i + 1) if i + 1 < n_finals else (t, 0)
                    )
                    transitions.add(((s, i), a, new_t))
        return NBA(states, alphabet, transitions, initial, final)
