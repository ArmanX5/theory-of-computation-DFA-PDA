import streamlit as st
from src import utils, pda

st.title("PDA Page")
st.subheader("Phase 4")
st.divider()

# To input the PDA from Streamlit UI, uncomment below code

# pda_details = utils.input_pda()
# my_pda = pda.PDA(**pda_details)

# Test Case
my_pda = pda.PDA( # PDA = { a^n b^2n | n >= 1 }
    states=['q0', 'q1', 'q2'],
    alphabet=['a', 'b'],
    stack_alphabet=['a', 'Z'],
    transition_function={
        ('q0', 'a', 'Z'): ('q0', 'aaZ'),
        ('q0', 'a', 'a'): ('q0', 'aaa'),
        ('q0', 'b', 'a'): ('q1', 'e'),
        ('q1', 'b', 'a'): ('q1', 'e'),
        ('q1', 'e', 'Z'): ('q2', 'e'),
    },
    initial_state='q0',
    final_states=['q2'],
    initial_stack_symbol='Z'
)

# print(my_pda.accepts("aabbbbb")) # accept
# print(my_pda.accepts("aabbbb")) # fail
# print(my_pda.accepts("aaaaaabbb")) # fail

st.divider()
st.graphviz_chart(my_pda.draw_pda())
st.divider()

# accepted_strings, failed_strings =  my_pda.show_accepted_failed_strings()
# st.write("10 strings that the PDA accepts:")
# print(accepted_strings)
# st.write("10 strings that the PDA doesn't accept:")
# print(failed_strings)
# st.divider()

string = st.text_input("Input a string:", value='aabbbb')
if my_pda.accepts(string):
    st.write("✅ Accepted!")
else:
    st.write("❌ Rejected!")

my_pda.stack_monitor(string)