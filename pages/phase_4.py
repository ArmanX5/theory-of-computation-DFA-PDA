import streamlit as st
from src import utils, pda

st.title("PDA Page")
st.subheader("Phase 4")
st.divider()

# pda_details = utils.input_pda()
#
# my_pda = pda.PDA(
#     states=pda_details["states"],
#     alphabet=pda_details["alphabet"],
#     stack_alphabet=pda_details["stack_alphabet"],
#     transition_function=pda_details["transition_function"],
#     initial_state=pda_details["initial_state"],
#     final_states=pda_details["final_states"],
#     initial_stack_symbol=pda_details["initial_stack_symbol"],
# )

# my_pda = pda.PDA(
#     states=['q0', 'q1', 'q2'],
#     alphabet=['0', '1'],
#     stack_alphabet=['X', 'Y', 'Z'],
#     transition_function={
#         ('q0', '0', 'Z'): ('q1', 'XX'),
#         ('q1', '0', 'X'): ('q1', 'XX'),
#         ('q1', '1', 'X'): ('q2', 'e'),
#         ('q2', '1', 'X'): ('q2', 'e')
#     },
#     initial_state='q0',
#     final_states=['q2'],
#     initial_stack_symbol='Z'
# )

my_pda = pda.PDA(
    states=['q1', 'q2', 'q3', 'q4'],
    alphabet=['0', '1'],
    stack_alphabet=['0', '1'],
    transition_function={
        # ('q0', '0', 'Z'): ('q1', 'XX'),
        ('q1', 'e', 'e'): ('q2', '1'),
        ('q2', '0', 'e'): ('q2', '0'),
        ('q2', '1', '0'): ('q3', 'e'),
        ('q3', '1', '0'): ('q3', 'e'),
        ('q3', 'e', '1'): ('q4', 'e'),
    },
    initial_state='q1',
    final_states=['q1', 'q4'],
    initial_stack_symbol=''
)

input_str = '000111'

st.graphviz_chart(my_pda.draw_pda())

st.write(my_pda.accepts("000111"))