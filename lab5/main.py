def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def find_longest_prefix(first_term, second_term):
    zipped_list = list(zip(first_term, second_term))
    matched_list = [x[0] if x[0] == x[1] else "" for x in zipped_list]
    longest_prefix_list = []
    for letter in matched_list:
        if letter == "":
            break
        longest_prefix_list.append(letter)
    longest_prefix = "".join(longest_prefix_list)
    return longest_prefix


def left_factor(rules):
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))

        if len(right_side) >= 2:
            for term in right_side:
                pass

        print(f"{A}, {right_side}")
    return rules


if __name__ == "__main__":
    production_rules = read_rules("rules.txt")
    print("Production Rules:")
    for rule in production_rules:
        print(rule)
    new_rules = left_factor(production_rules[:])
    print("After left factoring: ")
    for rule in new_rules:
        print(rule)
