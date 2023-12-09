import streamlit as st
from src import utils, dfa

st.title("DFA Page")
st.subheader("Phase 1")
st.divider()

# Input DFA
dfa_details = utils.input_dfa()

# Create DFA Object
dfa_1 = dfa.DFA(
    dfa_details["states"],
    dfa_details["alphabet"],
    dfa_details["transitions"],
    dfa_details["initial_state"],
    dfa_details["final_states"],
)

st.subheader("The DFA:")
st.graphviz_chart(dfa_1.draw_dfa())

tab_1, tab_2, tab_3 = st.tabs(
    ["DFA Info", "Minimized DFA", "Equivalence"]
)

with st.container():
    with tab_1: # DFA Info
        st.subheader("DFA Info:")
        if st.checkbox("Show", value=False, key="show_dfa_info"):
            if dfa_1.is_lang_empty(): # آیا زبان ماشین مورد نظر تهی است؟
                st.write("⚠️ The language of DFA is empty.")
            else:
                st.write("✅ The language of DFA is NOT empty.")
                if dfa_1.is_lang_finite(): # آیازبان ماشین مورد نظر متناهی است؟
                    st.write("✅ The language of DFA is finite.")
                    st.write("🔸 Number of accepted strings: ", len(dfa_1.accepted_strings()))
                    if len(dfa_1.accepted_strings()) <= 20:
                        st.write("🔸 All accepted strings are ==> ", utils.list_to_string(dfa_1.accepted_strings()))
                    else:
                        st.write("🔸 The first 20 accepted strings are ==> ", utils.list_to_string(dfa_1.accepted_strings()[:20]))
                else:
                    st.write("♾️ The language of DFA is infinite.")
                str = st.text_input("Enter the string to check if it is accepted or not: ", value="ab" ,key="string_accept")
                if dfa_1.does_accept_string(str):
                    st.write("✅ The string was accepted.")
                else:
                    st.write("❌ The string was NOT accepted.")

    with tab_2: # Minimized DFA
        st.subheader("Minimized DFA:")
        if st.checkbox("Show", value=False, key="show_minimized_dfa"):
            st.graphviz_chart(dfa_1.minimize().draw_dfa())
    with tab_3: # Equivalence
        dfa_2_details = utils.input_dfa_2()
        dfa_2 = dfa.DFA(
            dfa_2_details["states"],
            dfa_2_details["alphabet"],
            dfa_2_details["transitions"],
            dfa_2_details["initial_state"],
            dfa_2_details["final_states"],
        )
        st.subheader("The DFA:")
        st.graphviz_chart(dfa_2.draw_dfa())
        if st.button("Check Equivalence"):
            if dfa_1.equivalent(dfa_2):
                st.write("✅ The two DFAs are equivalent.")
            else:
                st.write("❌ The two DFAs are not equivalent.")

