from src import utils
from graphviz import Digraph

class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states # list ["A", "B", ...]
        self.alphabet = alphabet # list ["a", "b", ...]
        self.transitions = transitions # dict {"A-a": "B", "A-b": "C", ...}
        self.initial_state = initial_state # str "A"
        self.final_states = final_states # list ["A", "B", ...]
        self.num_states = len(states) # int
    
    def is_state_reachable(self, state):
        visited = set()  # Set to keep track of visited states during traversal
        stack = [self.initial_state]  # Stack to perform depth-first search

        while stack:
            current_state = stack.pop()

            if current_state == state:
                return True  # The state is reachable

            if current_state not in visited:
                visited.add(current_state)
                # Find next states based on transitions
                next_states = [self.transitions.get(f"{current_state}-{symbol}", None) for symbol in self.alphabet]
                next_states = [next_state for next_state in next_states if next_state is not None]
                stack.extend(next_states)

        return False  # The state is not reachable
    
    def is_lang_empty(self):
        for state in self.final_states:
            if self.is_state_reachable(state):
                return False
        return True
    
    def does_accept_string(self, string):
        current_state = self.initial_state
        for symbol in string:
            current_state = self.transitions.get(f"{current_state}-{symbol}", None)
        return current_state in self.final_states
    
    def is_lang_finite(self):
        for i in range(self.num_states, 2*self.num_states+1):
            strings = utils.generate_strings(i, self.alphabet)
            for string in strings:
                if self.does_accept_string(string):
                    return False
        return True

    def accepted_strings(self):
        accepted_strings = []
        if not self.is_lang_finite():
            return []
        if self.is_lang_empty():
            return []
        if self.initial_state in self.final_states:
            accepted_strings.append("ƛ")
        for i in range(1, self.num_states):
            strings = utils.generate_strings(i, self.alphabet)
            for string in strings:
                if self.does_accept_string(string):
                    accepted_strings.append(string)
        return accepted_strings

    def draw_dfa(self):
        # Create a directed graph using graphviz
        dot = Digraph(comment='DFA')
        dot.attr(rankdir='LR')  # Left to right layout

        # Add states
        for state in self.states:
            if state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')

        # Add an arrow from nowhere to the initial state
        dot.node("Nowhere", style='invisible')
        dot.edge("Nowhere", self.initial_state, label='')

        # Combine transitions with the same source and destination states
        combined_transitions = {}
        for transition, next_state in self.transitions.items():
            current_state, symbol = transition.split('-')
            key = (current_state, next_state)
            combined_transitions[key] = combined_transitions.get(key, []) + [symbol]

        # Add transitions
        for (current_state, next_state), symbols in combined_transitions.items():
            label = ",".join(symbols)
            dot.edge(current_state, next_state, label=label)

        return dot

    def minimize(self):
        # remove unreachable states
        states = [state for state in self.states if self.is_state_reachable(state)]
        final_states = [state for state in self.final_states if self.is_state_reachable(state)]

        # Initialize partition with final and non-final states
        partition = [set(final_states), set(states) - set(final_states)]

        # Function to find the group of a state
        def find_group(state):
            for group in partition:
                if state in group:
                    return group

        # Keep partitioning until no change
        while True:
            new_partition = []

            for group in partition:
                # Split states in the group based on their transitions
                split_dict = {}

                for state in group:
                    key = tuple(
                        frozenset(find_group(self.transitions.get(f"{state}-{symbol}", None)))
                        for symbol in self.alphabet
                    )
                    if key not in split_dict:
                        split_dict[key] = set()
                    split_dict[key].add(state)

                new_partition.extend(split_dict.values())

            if new_partition == partition:  # No change, so we're done
                break

            partition = new_partition

        # Create new DFA from the partition
        new_states = [utils.state_name(state) for state in partition]
        new_initial_state = new_states[next(i for i, group in enumerate(partition) if self.initial_state in group)]
        new_final_states = [
            new_states[i] for i, group in enumerate(partition) if any(state in group for state in self.final_states)
        ]
        new_transitions = {}

        for i, group in enumerate(partition):
            for symbol in self.alphabet:
                next_state = self.transitions.get(f"{next(iter(group))}-{symbol}", None)
                if next_state is not None:
                    new_transitions[f"{new_states[i]}-{symbol}"] = new_states[
                        next(j for j, other_group in enumerate(partition) if next_state in other_group)
                    ]

        return DFA(new_states, self.alphabet, new_transitions, new_initial_state, new_final_states)
