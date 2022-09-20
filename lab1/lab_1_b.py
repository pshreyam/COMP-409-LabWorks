def check_valid_regex(string):
    # Regular expression matching string over alphabets {a, b} starting with a
    # and ending with b
    # REGEX = "a(a+b)a(a+b)*b(a+b)b"
    if len(string) >= 6:
        # For not matching abab
        if string[0] == "a" and string[-1] == "b" and string[2] == "a" and \
            string[-3] == "b" and set(list(string)) == {"a", "b"}:
            return True
    return False


if __name__ == "__main__":
    input_string = input("Enter the string: ")
    print(check_valid_regex(input_string))
