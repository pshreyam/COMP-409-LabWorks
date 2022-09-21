import unittest

from lab_2_a import State, DFA, check_string_validity


class TestDFA(unittest.TestCase):
    def test_dfa_1(self):
        # DFA that accepts strings that start with 1 and ends with 0

        # 4 states with q2 as the accepting state
        # q3 is the trap state
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2", accepting=True)
        q3 = State("q3")

        transition_table = {
            str(q0): {"0": q3, "1": q1},
            str(q1): {"0": q2, "1": q1},
            str(q2): {"0": q2, "1": q1},
            str(q3): {"0": q3, "1": q3},
        }

        dfa = DFA(q0, transition_table)

        self.assertEqual(check_string_validity("00001", dfa), False)
        self.assertEqual(check_string_validity("01", dfa), False)
        self.assertEqual(check_string_validity("1", dfa), False)
        self.assertEqual(check_string_validity("10", dfa), True)
        self.assertEqual(check_string_validity("1100", dfa), True)
        self.assertEqual(check_string_validity("101010", dfa), True)

    def test_dfa_2(self):
        # DFA that accepts strings accepts only 101

        # 5 states with q3 as the accepting state
        # q4 is the trap state
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2")
        q3 = State("q3", accepting=True)
        q4 = State("q4")

        transition_table = {
            str(q0): {"0": q4, "1": q1},
            str(q1): {"0": q2, "1": q4},
            str(q2): {"0": q4, "1": q3},
            str(q3): {"0": q4, "1": q4},
            str(q4): {"0": q4, "1": q4},
        }

        dfa = DFA(q0, transition_table)

        self.assertEqual(check_string_validity("101", dfa), True)
        self.assertEqual(check_string_validity("1010", dfa), False)
        self.assertEqual(check_string_validity("0101", dfa), False)
        self.assertEqual(check_string_validity("10101", dfa), False)
