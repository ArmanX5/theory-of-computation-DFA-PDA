import streamlit as st
from src import utils, dfa

st.title("DFA Page")
st.subheader("Phase 1")
st.divider()

# Input DFA
dfa_details = utils.input_dfa()

# Create DFA Object
dfa = dfa.DFA(
    dfa_details["states"],
    dfa_details["alphabet"],
    dfa_details["transitions"],
    dfa_details["initial_state"],
    dfa_details["final_states"],
)

st.subheader("The DFA:")
st.graphviz_chart(dfa.draw_dfa())

tab_1, tab_2, tab_3 = st.tabs(
    ["DFA Info", "Minimized DFA", "Equivalence"]
)

with st.container():
    with tab_1: # DFA Info
        st.subheader("DFA Info:")
        if dfa.is_lang_empty():
            st.write("The language of DFA is empty.")
            st.write("The language of DFA is finite.")
        else:
            st.write("The language of DFA is not empty.")
            if dfa.is_lang_finite():
                st.write("The language of DFA is finite.")
                st.write("Number of accepted strings: ", len(dfa.accepted_strings()))
                if len(dfa.accepted_strings()) < 20:
                    st.write("All accepted strings are ==> ", utils.list_to_string(dfa.accepted_strings()))
                else:
                    st.write("The first 20 accepted strings are ==> ", utils.list_to_string(dfa.accepted_strings()[:20]))
            else:
                st.write("The language of DFA is infinite.")

    with tab_2: # Minimized DFA
        st.subheader("Minimized DFA:")
        if st.checkbox("Show", value=False):
            st.graphviz_chart(dfa.minimize().draw_dfa())
    with tab_3: # Equivalence
        pass

