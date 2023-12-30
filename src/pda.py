from src import utils
from graphviz import Digraph

class PDA:
    def __init__(self, states, alphabet, stack_alphabet, transition_function, initial_state, final_states, initial_stack_symbol):
        self.states = states # ['q0', 'q1', 'q2']
        self.alphabet = alphabet # ['0', '1']
        self.stack_alphabet = stack_alphabet # ['X', 'Y', 'Z']
        self.initial_state = initial_state # 'q0'
        self.final_states = final_states # ['q1', 'q2']
        self.initial_stack = initial_stack_symbol # 'Z'
        self.transition_function = transition_function
        # Transition function: {(current_state, input_symbol, stack_top): (new_state, stack_operation)}
        # transition_function = {
        #     ('q0', '0', 'Z'): ('q1', 'XZ'),
        #     ('q1', '0', 'X'): ('q1', 'XX'),
        #     ('q1', '1', 'X'): ('q2', 'e'), | e = epsilon
        #     ('q2', '1', 'X'): ('q2', 'e')
        # }
        self.alphabet.append('e')
        self.stack_alphabet.append('e')


    def does_accept_string(self, input_string):
        current_state = self.initial_state
        stack = [self.initial_stack]
        for symbol in input_string:
            stack_top = stack[-1]
            if (current_state, symbol, stack_top) in self.transition_function:
                new_state, stack_operation = self.transition_function[(current_state, symbol, stack_top)]
                current_state = new_state
                if stack_operation == 'e':
                    stack.pop()
                else:
                    stack.append(stack_operation)
            else:
                return False

        return current_state in self.final_states

    def draw_pda(self):
        dot = Digraph(comment='PDA')
        dot.attr(rankdir='LR')  # Left to right layout

        # Add states
        for state in self.states:
            if state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')

        # Add an arrow from nowhere to the initial state
        dot.node("Nowhere", shape='point', style='invisible')
        dot.edge("Nowhere", self.initial_state, label='')

        for state in self.states:
            for symbol in self.alphabet:
                for stack_top in self.stack_alphabet:
                    if (state, symbol, stack_top) in self.transition_function:
                        new_state, stack_operation = self.transition_function[(state, symbol, stack_top)]
                        dot.edge(state, new_state, label=f"{symbol}, {stack_top} → {stack_operation}")
        return dot