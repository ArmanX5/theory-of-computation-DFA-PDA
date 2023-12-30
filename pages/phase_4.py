import streamlit as st
from src import utils, pda

st.title("PDA Page")
st.subheader("Phase 4")
st.divider()

states = ['q0', 'q1']
alphabet = ['a', 'b']
stack_alphabet = ['A', 'Z']
initial_state = 'q0'
final_states = ['q1']
initial_stack_symbol = 'Z'
transition_function = {
    ('q0', 'a', 'Z'): ('q0', 'AZ'),
    ('q0', 'a', 'A'): ('q0', 'AA'),
    ('q0', 'b', 'A'): ('q1', 'e'),
    ('q1', 'b', 'A'): ('q1', 'e'),
    ('q1', 'e', 'Z'): ('q1', 'e'),
    # ('q1', '0', 'X'): ('q1', 'XX'),
    # ('q1', '1', 'X'): ('q2', 'e'), # | e = epsilon
    # ('q2', '1', 'X'): ('q2', 'e')
}

my_pda = pda.PDA(states, alphabet, stack_alphabet, transition_function, initial_state, final_states, initial_stack_symbol)

st.graphviz_chart(my_pda.draw_pda())

st.write(my_pda.does_accept_string("aabb"))