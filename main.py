import streamlit as st

# Title
st.title("Theory of Computation Project")
st.divider()

# Content
with st.container():
    
    with st.container():
        r1, l1 = st.columns(2)
        with r1:
            st.subheader("Phase 1: DFA")
            st.write("This phase is capable of the following tasks:")
            st.markdown('''
            - Defines whether the language is empty or not.
            - Defines whether the language is finite or not.
            - If the language is finite, how many strings are accepted and print some of them.
            - Defines whether the machine accepts string X or not.
            - Minimize the given DFA.
            - Defines whether two DFAs are equivalent or not.
                        ''')
        
        with l1:
            st.subheader("Phase 2: Expressions")
            st.write("This phase is capable of the following tasks:")
            st.markdown('''
            - Defines whether the expression's language is regular or not.
            - Create DFA from regular expression.
            - Defines whether two regular expressions are equivalent or not.
            - Defines whether two expressions are subset or superset of each other.
                        ''')

    with st.container():
        r1, l1 = st.columns(2)
        with r1:
            st.subheader("Phase 3: Degree Function")
            st.write("This phase is capable of the following tasks:")
            st.markdown('''
            - Defines the Degree function for a given regular expression.
                        ''')
        
        with l1:
            st.subheader("Phase 4: PDA")
            st.write("This phase is capable of the following tasks:")
            st.markdown('''
            - Printing 10 strings that are accepted by the PDA.
            - Printing 10 strings that are rejected by the PDA.
            - Monitoring the stack of the PDA.
            - Defines whether the machine accepts string X or not.
                        ''')

# Footer
st.divider()
st.caption("Made with 💖 by: Arman Akhoundy & M. Saleh Taleb")
