from typing import Any, Dict, List, Set, Tuple, Union

StateType = Any
ActType = Any
LabelType = Any


class TS:
    def __init__(
        self,
        states: List[StateType],
        init_states: Set[StateType],
        acts: List[ActType],
        propositions: List[LabelType],
        transitions: Union[
            List[Tuple[StateType, ActType, StateType]],
            Dict[StateType, List[Tuple[ActType, StateType]]],
        ],
        labels: List[Set[LabelType]],
    ):
        self.states = states
        self.init_states = init_states if isinstance(init_states, set) else set(init_states)
        self.acts = acts
        self.propositions = propositions
        if isinstance(transitions, List):
            self.transitions = {}
            for (s, a, t) in transitions:
                if s not in self.transitions:
                    self.transitions[s] = []
                self.transitions[s].append((a, t))
        else:
            self.transitions = transitions

        self.labels = [l if isinstance(l, set) else set(l) for l in labels]

    def __str__(self):
        return f"""TS(
    states={self.states},
    init_states={self.init_states},
    acts={self.acts},
    propositions={self.propositions},
    transitions={self.transitions},
    labels={self.labels}
)"""

    def with_init(self, init_states: Set[StateType]):
        return TS(
            self.states, init_states, self.acts, self.propositions, self.transitions, self.labels
        )
