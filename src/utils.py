import streamlit as st


def input_dfa():
    st.header("Input DFA")
    st.caption("Please enter the DFA's details below:")

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

    # Input initial state
    initial_state = st.selectbox("Enter Initial state:", options=states)

    # Input final states
    final_states = st.multiselect("Enter final states:", options=states)

    # Input transitions
    st.divider()
    transitions = {}
    for state in states:
        st.caption(f"Enter transitions for state '{state}':")
        for symbol in alphabet:
            transitions[f"{state}-{symbol}"] = st.selectbox(
                f"Enter transition for '{state}' on '{symbol}':",
                options=states,
            )
        st.divider()

    return {
        "states": states,
        "initial_state": initial_state,
        "alphabet": alphabet,
        "final_states": final_states,
        "transitions": transitions,
    }
            
# function that returns a list of all strings with length n with given alphabet. the elements of returend list be in string format like ["aaa", "aab", ...]
def generate_strings(n, alphabet):
    if n == 0:
        return [""]
    else:
        strings = []
        for symbol in alphabet:
            for string in generate_strings(n - 1, alphabet):
                strings.append(string + symbol)
        return strings