from src import utils
# import utils
from graphviz import Digraph

class PDA:
    def __init__(self,
                 states,
                 alphabet,
                 stack_alphabet,
                 transition_function,
                 initial_state,
                 final_states,
                 initial_stack_symbol):
        self.states = states # ['q0', 'q1', 'q2']
        self.alphabet = alphabet # ['0', '1']
        self.stack_alphabet = stack_alphabet # ['X', 'Y', 'Z']
        self.initial_state = initial_state # 'q0'
        self.final_states = final_states # ['q1', 'q2']
        self.initial_stack = initial_stack_symbol # 'Z'
        self.transition_function = transition_function
        # Transition function: {(current_state, input_symbol, stack_top): (new_state, stack_operation)}
        # transition_function = {
        #     ('q0', '0', 'Z'): ('q1', 'XZ'), from state q0, input symbol 0, pop Z from stack, goto state q1, push XZ
        #     ('q1', '0', 'X'): ('q1', 'XX'),
        #     ('q1', '1', 'X'): ('q2', 'e'),  | e = epsilon
        #     ('q2', '1', 'X'): ('q2', 'e')
        # }
        # self.alphabet.append('e')
        # self.stack_alphabet.append('e')

    
    def accepts(self, input_string):
        current_state = self.initial_state
        stack = [self.initial_stack]
        for symbol in input_string:
            # for a normal transition (q0, a, X)
            if (current_state, symbol, stack[-1]) in self.transition_function:
                new_state, stack_operation = self.transition_function[(current_state, symbol, stack[-1])]
                current_state = new_state
                stack.pop()
                if stack_operation != 'e':
                    stack.append(stack_operation[::-1])
            # for stack epsilon transition (q0, a, e)
            elif (current_state, symbol, 'e') in self.transition_function:
                new_state, stack_operation = self.transition_function[(current_state, symbol, 'e')]
                current_state = new_state
                if stack_operation != 'e':
                    stack.append(stack_operation[::-1])
            # for epsilon transition (q0, e, X)
            flag = True
            while flag:
                if (current_state, 'e', stack[-1]) in self.transition_function:
                    new_state, stack_operation = self.transition_function[(current_state, 'e', stack[-1])]
                    current_state = new_state
                    stack.pop()
                    if stack_operation != 'e':
                        stack.append(stack_operation[::-1])
                elif (current_state, 'e', 'e') in self.transition_function:
                    new_state, stack_operation = self.transition_function[(current_state, 'e', 'e')]
                    current_state = new_state
                    if stack_operation != 'e':
                        stack.append(stack_operation[::-1])
                else:
                    flag = False
            # if transition doesn't exist
            if current_state not in self.states:
                return False
        return current_state in self.final_states


    # This function shows the first 10 string that the PDA accepts
    def show_first_10(self):
        n = 1
        i = 0
        strings = []
        while i <= 10:
            generated_strings = utils.generate_strings(n, self.alphabet)
            for string in generated_strings:
                if self.accepts(string):
                    strings.append(string)
                    i += 1
            n += 1
        return strings

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