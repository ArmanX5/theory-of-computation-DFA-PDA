from src import utils
from graphviz import Digraph
import streamlit as st

class PDA:
    def __init__(self,states,alphabet,stack_alphabet,transition_function,initial_state,final_states,initial_stack_symbol):
        """
        Initializes a new instance of the class.

        Parameters:
            states (list): A list of states in the automaton.
            alphabet (list): A list of symbols in the input alphabet.
            stack_alphabet (list): A list of symbols in the stack alphabet.
            transition_function (dict): A dictionary representing the transition function of the automaton.
                The keys are tuples (current_state, input_symbol, stack_top), and the values are tuples (new_state, stack_operation).
            initial_state (str): The initial state of the automaton.
            final_states (list): A list of final states in the automaton.
            initial_stack_symbol (str): The initial symbol on the stack.

        Note:
            - states, alphabet, stack_alphabet, and final_states should be non-empty lists.
            - transition_function should be a non-empty dictionary.
            - The input alphabet and stack alphabet should contain the empty symbol 'e'.
        """
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
        self.alphabet.append('e')
        self.stack_alphabet.append('e')

    
    def accepts(self, input_string):
        """
        Check if the given input string is accepted by the current state machine.

        Parameters:
        - input_string (str): The input string to be checked.

        Returns:
        - bool: True if the input string is accepted, False otherwise.
        """
        input_string = 'e' + input_string + 'e'
        current_state = self.initial_state
        stack = self.initial_stack
        for symbol in input_string:
            try:
                if (current_state, symbol, stack[-1]) in self.transition_function:
                    new_state, stack_operation = self.transition_function[(current_state, symbol, stack[-1])]
                    current_state = new_state
                    stack = stack[:-1]
                    if stack_operation != 'e':
                        stack += stack_operation[::-1]
                elif (current_state, symbol, 'e') in self.transition_function:
                    new_state, stack_operation = self.transition_function[(current_state, symbol, 'e')]
                    current_state = new_state
                    if stack_operation != 'e':
                        stack += stack_operation[::-1]
                else:
                    if symbol != 'e':
                        return False
            except:
                return False

        return current_state in self.final_states


    def stack_monitor(self, input_string):
        """
        Monitors the stack based on an input string.

        Parameters:
            input_string (str): The input string to be monitored.

        Returns:
            bool: True if the monitoring is successful, False otherwise.
        """
        if st.button("Monitor Stack"):
            input_string = 'e' + input_string + 'e'
            string = ''
            current_state = self.initial_state
            stack = self.initial_stack
            for symbol in input_string:
                st.write("-----------------------------------")
                st.write(f"The current symbol: {symbol}")
                st.write(f"The string so far: {string}")
                st.write(f"The current state: {current_state}")
                st.write(f"The current stack status: {stack}")
                try:
                    if (current_state, symbol, stack[-1]) in self.transition_function:
                        new_state, stack_operation = self.transition_function[(current_state, symbol, stack[-1])]
                        current_state = new_state
                        stack = stack[:-1]
                        if stack_operation != 'e':
                            stack += stack_operation[::-1]
                    elif (current_state, symbol, 'e') in self.transition_function:
                        new_state, stack_operation = self.transition_function[(current_state, symbol, 'e')]
                        current_state = new_state
                        if stack_operation != 'e':
                            stack += stack_operation[::-1]
                    else:
                        if symbol != 'e':
                            return False
                except:
                    return False
                if symbol != 'e':
                    string += symbol

            return current_state in self.final_states


    def show_accepted_failed_strings(self, number):
        """
        Show the accepted and failed strings.

        This function generates a list of accepted strings and a list of failed strings. It starts by initializing the variables `n`, `ac`, `fa` to 1, 0, and 0 respectively. It also initializes empty lists `ac_strings` and `fa_strings` to store the accepted and failed strings.

        The function then enters a while loop that continues until both `ac` and `fa` are greater than or equal to 10. Inside the loop, it generates a list of strings using the `utils.generate_strings()` function with the current value of `n` and `self.alphabet`. It then iterates over each string in the generated_strings list.

        If the number of accepted strings (`ac`) is already equal to or greater than 10, and the number of failed strings (`fa`) is also equal to or greater than 10, the loop is exited using the `break` statement.

        If the current string is accepted, it is appended to the `ac_strings` list and the `ac` counter is incremented by 1. Otherwise, the string is appended to the `fa_strings` list and the `fa` counter is incremented by 1.

        After each iteration, the value of `n` is incremented by 1.

        Finally, the function returns the `ac_strings` and `fa_strings` lists.

        Returns:
            ac_strings (List[str]): A list of accepted strings.
            fa_strings (List[str]): A list of failed strings.
        """
        n = 1
        ac = 0
        fa = 0
        ac_strings = []
        fa_strings = []
        while ac < number or fa < number:
            generated_strings = utils.generate_strings(n, self.alphabet)
            for string in generated_strings:
                if ac >= number and fa >= number:
                    break
                if self.accepts(string):
                    ac_strings.append(string)
                    ac += 1
                elif not self.accepts(string):
                    fa_strings.append(string)
                    fa += 1
            n += 1
        return ac_strings[:number], fa_strings[:number]


    def draw_pda(self):
        """
        Generate a visualization of the Pushdown Automaton (PDA).

        Returns:
            Digraph: A graph object representing the PDA visualization.
        """
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