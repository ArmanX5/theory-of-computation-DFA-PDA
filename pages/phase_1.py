import streamlit as st
from src import utils, dfa

st.title("DFA Page")
st.subheader("Phase 1")
st.divider()

dfa_details = utils.input_dfa()

dfa = dfa.DFA(
    dfa_details["states"],
    dfa_details["alphabet"],
    dfa_details["transitions"],
    dfa_details["initial_state"],
    dfa_details["final_states"],
)