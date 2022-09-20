# Regular expression matching string over alphabets {a, b} starting with a 
# and ending with b
REGEX = "a(a+b)*b"


def check_valid(regex, string):
    if string[0] == regex[0] and string[-1] == regex[-1] and set(list(string)) == {"a", "b"}:
        return True
    return False

if __name__ == "__main__":
    input_string = input("Enter the string: ")
    print(check_valid(REGEX, input_string))
