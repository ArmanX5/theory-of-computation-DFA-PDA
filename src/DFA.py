import utils

class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states # list ["A", "B", ...]
        self.alphabet = alphabet # list ["a", "b", ...]
        self.transitions = transitions # dict {"A-a": "B", "A-b": "C", ...}
        self.initial_state = initial_state # str "A"
        self.final_states = final_states # list ["A", "B", ...]
        self.num_states = len(states) # int
    
    def state_is_reachable(self, state):
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
    
    def lang_is_empty(self):
        for state in self.final_states:
            if self.state_is_reachable(state):
                return False
        return True
    
    def accept_string(self, string):
        current_state = self.initial_state
        for symbol in string:
            current_state = self.transitions.get(f"{current_state}-{symbol}", None)
        return current_state in self.final_states
    
    def is_lang_finite(self):
        # a language is infinite if we find an accepted string with 
        # length of num_states <= length of string <= 2*num_states
        for i in range(self.num_states, 2*self.num_states+1):
            strings = utils.generate_strings(i, self.alphabet)
            for string in strings:
                if self.accept_string(string):
                    return False
        return True
    
    def all_accepted_strings(self):
        strings = utils.generate_strings(self.num_states, self.alphabet)
        accepted_strings = []
        for string in strings:
            if self.accept_string(string):
                accepted_strings.append(string)
        return accepted_strings