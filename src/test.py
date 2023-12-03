import DFA
import utils

# dfa = DFA.DFA(
#     ["q0", "q1", "q2", "q3", "q4"], # states
#     ["a", "b"], # alphabet
#     {
#         "q0-a": "q1",
#         "q0-b": "q2",
#         "q1-a": "q3",
#         "q1-b": "q0",
#         "q2-a": "q0",
#         "q2-b": "q3",
#         "q3-a": "q2",
#         "q3-b": "q1",
#         "q4-a": "q2",
#         "q4-b": "q3"
#     }, # transitions
#     "q0", # initial state
#     ["q1", "q3"] # final states
# )

dfa = DFA.DFA(
    ["A", "B", "C"], # states
    ["a", "b"], # alphabet
    {
        "A-a": "B",
        "A-b": "B",
        "B-a": "C",
        "B-b": "C",
        "C-a": "D",
        "C-b": "D",
        "D-a": "D",
        "D-b": "D"
    },
    "A",
    ["C"]
)

# print(dfa.state_is_reachable("q4"))
# print(dfa.lang_is_empty())
# print(dfa.accept_string("abb"))
# dfa.is_lang_finite()
print(dfa.is_lang_finite())
# print(utils.generate_strings(2, ["a", "b"]))