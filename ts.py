from typing import Any, Dict, List, Set, Tuple, Union

StateType = Any
ActType = Any
LabelType = Any
TransitionType = Dict[StateType, Dict[ActType, Set[StateType]]]


class TS:
    """Transition system

    transitions: Can be a list of tuples (s, a, t) or a dictionary (s -> a -> {t})
    """

    def __init__(
        self,
        states: List[StateType],
        init_states: Set[StateType],
        acts: Set[ActType],
        propositions: List[LabelType],
        transitions: Union[
            List[Tuple[StateType, ActType, StateType]],
            TransitionType,
        ],
        labels: Union[Dict[StateType, Set[LabelType]], List[Set[LabelType]]],
    ):
        self.states = states
        self.init_states = set(init_states)
        self.acts = set(acts)
        self.propositions = propositions

        if isinstance(transitions, List):
            self.transitions: TransitionType = {s: {} for s in states}
            for s, a, t in transitions:
                if a not in self.transitions[s]:
                    self.transitions[s][a] = set()
                self.transitions[s][a].add(t)
        else:
            self.transitions = transitions

        if isinstance(labels, List):
            self.labels = {}
            for s, l in enumerate(labels):
                self.labels[states[s]] = frozenset(l)
        else:
            self.labels = labels

    def __repr__(self):
        return f"""TS(
    states={self.states},
    init_states={self.init_states},
    acts={self.acts},
    propositions={self.propositions},
    transitions={self.transitions},
    labels={self.labels}
)"""

    def with_init(self, init_states: Set[StateType]):
        """Returns a copy of the TS with the given initial states"""
        return TS(
            self.states, init_states, self.acts, self.propositions, self.transitions, self.labels
        )
