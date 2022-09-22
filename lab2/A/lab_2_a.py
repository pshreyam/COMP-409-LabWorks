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
        return DFA(new_state, self.transition_table)


def check_string_validity(string, dfa):
    for char in string:
        dfa = dfa.transition(char)

    return dfa.current_state.accepting


if __name__ == "__main__":
    # Three states with s0 and s1 as accepting states
    # s2 is trap state
    s0 = State("s0", accepting=True)
    s1 = State("s1", accepting=True)
    s2 = State("s2")

    # Defining a state transition table for accepting a string
    # with no consecutive 1's together
    transition_table = {
        str(s0): {"0": s0, "1": s1},
        str(s1): {"0": s0, "1": s2},
        str(s2): {"0": s2, "1": s2},
    }

    dfa = DFA(s0, transition_table)

    string = input("Enter the string: ")

    if check_string_validity(string, dfa):
        print("String accepted!")
    else:
        print("String not accepted!")
