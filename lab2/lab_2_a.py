class State:
    def __init__(self, name, accepting=False):
        self.name = name
        self.accepting = accepting

    def __repr__(self):
        return f"{'*' if self.accepting else ''}<State:{self.name}>"

    def __eq__(self, o):
        return self.name == o.name


class DFA:
    def __init__(self, initial_state, transition_table):
        self.current_state = initial_state
        self.transition_table = transition_table

    def transition(self, char):
        new_state = self.transition_table[str(self.current_state)][char]
        return DFA(new_state, transition_table)


def check_string_validity(string, dfa):
    for char in string:
        dfa = dfa.transition(char)

    if dfa.current_state.accepting:
        print("String accepted!")
    else:
        print("String not accepted!")


if __name__ == "__main__":
    s0 = State("s0", True)
    s1 = State("s1", True)
    s2 = State("s2")

    transition_table = {
        str(s0): {"0": s0, "1": s1},
        str(s1): {"0": s0, "1": s2},
        str(s2): {"0": s2, "1": s2},
    }

    dfa = DFA(s0, transition_table)

    string = input("Enter the string: ")
    check_string_validity(string, dfa)
