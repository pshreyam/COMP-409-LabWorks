import unittest

from lab_2_a import State, DFA, check_string_validity


class TestDFA(unittest.TestCase):
    def test_dfa_1(self):
        # DFA that accepts strings that start with 1 and ends with 0
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2", True)
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
