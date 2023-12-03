import sys
sys.path.append("")
import streamlit as st
from src import utils, DFA

st.title("DFA Page")
st.subheader("Phase 1")
st.divider()

dfa_details = utils.input_dfa()

dfa = DFA.DFA(
    dfa_details["states"],
    dfa_details["alphabet"],
    dfa_details["transitions"],
    dfa_details["initial_state"],
    dfa_details["final_states"],
)