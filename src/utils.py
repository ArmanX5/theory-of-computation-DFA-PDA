import streamlit as st



def input_dfa():
    st.header("Input DFA")
    st.write("Please enter the DFA's details below:")

    with st.container():
        # Input states
        states = st.text_input("Enter States (separated by comma):", value="A, B")
        states = states.split(",")
        states = [st.strip() for st in states]
        states = [st for st in states if st != ""]
        states = list(set(states))
        states.sort()
        num_states = len(states)

        # Input alphabet
        alphabet = st.text_input("Enter Alphabet (separated by comma):", value="a, b")
        alphabet = alphabet.split(",")
        alphabet = [st.strip() for st in alphabet]
        alphabet = [st for st in alphabet if st != ""]
        alphabet = list(set(alphabet))
        alphabet.sort()

    with st.container():
        left, right = st.columns(2)
        with left:
            # Input initial state
            initial_state = st.selectbox("Enter Initial state:", options=states)
        with right:
            # Input final states
            final_states = st.multiselect("Enter final states:", options=states)

    # Input transitions
    st.divider()
    transitions = {}
    for state in states:
        st.write(f"Enter transitions for state '{state}':")
        left, right = st.columns(2)
        i = 1
        for symbol in alphabet:
            if i % 2 == 0:
                with right:
                    transitions[f"{state}-{symbol}"] = st.selectbox(
                        f"'{state}' with '{symbol}' goes to:",
                        options=states,
                    )
            else:
                with left:
                    transitions[f"{state}-{symbol}"] = st.selectbox(
                        f"'{state}' with '{symbol}' goes to:",
                        options=states,
                    )
            i += 1
            # transitions[f"{state}-{symbol}"] = st.selectbox(
            #     f"'{state}' with '{symbol}' goes to:",
            #     options=states,
            # )
        st.divider()

    return {
        "states": states,
        "initial_state": initial_state,
        "alphabet": alphabet,
        "final_states": final_states,
        "transitions": transitions,
    }

            
# function that returns a list of all strings with length n with given alphabet.
def generate_strings(n, alphabet):
    """
    Generates all possible strings of length n using the characters in the given alphabet.

    Parameters:
        n (int): The length of the strings to be generated.
        alphabet (list): A list of characters representing the available symbols for the strings.

    Returns:
        list: A list of strings containing all possible combinations of the characters in the alphabet.
    """
    if n == 0:
        return [""]
    else:
        strings = []
        for symbol in alphabet:
            for string in generate_strings(n - 1, alphabet):
                strings.append(string + symbol)
        return strings


def print_dfa(dfa):
    print("States: ", dfa.states)
    print("Alphabet: ", dfa.alphabet)
    print("Initial State: ", dfa.initial_state)
    print("Final States: ", dfa.final_states)
    print("Transitions: ")
    for key, value in dfa.transitions.items():
        print(key, "->", value)

def state_name(state):
    state = list(state)
    name = ""
    if len(state) == 1:
        name = state[0]
    else:
        for i in range(len(state)):
            name += state[i]
            # if i < len(state) - 1:
            #     name += ","
    return name

def list_to_string(list):
    string = ""
    for i in range(len(list)):
        string += list[i]
        if i < len(list) - 1:
            string += ", "
    return string