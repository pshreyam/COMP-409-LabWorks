import unittest

from lab_1_b import check_valid_regex


class TestRegex(unittest.TestCase):
    def test_strings(self):
        self.assertEqual(check_valid_regex("ababbb"), True)
        self.assertEqual(check_valid_regex("aabb"), False)
        self.assertEqual(check_valid_regex("aba-bab"), False)
        self.assertEqual(check_valid_regex("abaabbbababab"), True)
        self.assertEqual(check_valid_regex("abaaaaabbbbbbab"), True)
        self.assertEqual(check_valid_regex("ababab"), True)
        self.assertEqual(check_valid_regex("baabbb"), False)
        self.assertEqual(check_valid_regex("ababba"), False)
        self.assertEqual(check_valid_regex("abab"), False)
