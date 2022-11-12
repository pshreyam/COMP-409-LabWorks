def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def get_table(rules):
    table = {}
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))
        table[A] = right_side
    return table


def generate_first_and_follow_table(rules):
    first_table = {}
    follow_table = {}
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))
        first_table[A] = set()
        follow_table[A] = set()
    return first_table, follow_table


def first(expr, rules):
    first_set = set()
    right_side = rules[expr]
    for term in right_side:
        first_character = term[0]
        if first_character.islower() or first_character.isdigit():
            first_set.add(first_character)
        elif first_character.isupper():
            first_set = first_set.union(first(first_character, rules))
    return first_set


if __name__ == "__main__":
    production_rules = read_rules("rules.txt")
    print("Production Rules:")
    for rule in production_rules:
        print(rule)
    for i in range(50):
        print("-", end="")
    print()
    first_table, follow_table = generate_first_and_follow_table(production_rules)
    rules_table = get_table(production_rules)
    print(first("S", rules_table))
    print(first("A", rules_table))
    print(first("B", rules_table))
    print(first("C", rules_table))
