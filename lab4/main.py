def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def parse_rules(rules):
    table = {}
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))
        table[A] = right_side
    return table


def get_table(rules):
    table = {}
    for rule in rules:
        A = rule.split("->")[0].strip()
        table[A] = set()
    return table


def is_nullable(expr, rules):
    if expr.islower() or expr.isdigit():
        return False
    if expr in rules:
        right_side = rules[expr]
        for term in right_side:
            if term == "ε":
                return True
    else:
        terms_list = parse_term(expr)
        return all([is_nullable(x, rules) for x in terms_list])
    return False


def parse_term(term):
    term_list = []
    for character in term:
        if character.islower() or character.isdigit():
            term_list.append(character)
        elif character.isupper():
            term_list.append(character)
        elif character == "'":
            term_list[-1] = term_list[-1] + character
    return term_list


def first(expr, rules):
    global first_table

    if expr.islower() or expr.isdigit():
        return set([expr])
    if not first_table[expr] == set():
        return first_table[expr]

    right_side = rules[expr]

    for term in right_side:
        term_list = parse_term(term)

        terms = iter(term_list)
        x = next(terms)
        while is_nullable(x, rules):
            first_table[expr] = first_table[expr].union(first(x, rules) - {"ε"})
            try:
                x = next(terms)
            except StopIteration:
                first_table[expr].add("ε")
                break
        first_table[expr] = first_table[expr].union(first(x, rules) - {"ε"})
        if x == "ε":
            first_table[expr].add("ε")

    # if is_nullable(expr, rules):
    #     first_table[expr].add("ε")
    # elif any([is_nullable(term, rules) for term in right_side]):
    #     first_table[expr].add("ε")

    return first_table[expr]


def follow(expr, rules):
    global follow_table

    if not follow_table[expr] == set():
        return follow_table[expr]

    if expr == "S":
        follow_table[expr] = {"$"}
        return follow_table[expr]

    for rule in rules:
        right_side = rules[rule]
        for term in right_side:
            term_list = parse_term(term)
            if expr in term_list:
                if term_list[-1] == expr:
                    if term in visited_list[expr]:
                        continue
                    follow_table[expr] = follow_table[expr].union(follow(rule, rules))
                    visited_list[expr].add(term)
                else:
                    terms = iter(term_list)
                    x = None
                    while not x == expr:
                        x = next(terms)
                    follow_item = next(terms)
                    while is_nullable(follow_item, rules):
                        follow_table[expr] = follow_table[expr].union(first(follow_item, rules) - {"ε"})
                        try:
                            follow_item = next(terms)
                        except StopIteration:
                            follow_table[expr] = follow_table[expr].union(follow(rule, rules))
                    follow_table[expr] = follow_table[expr].union(first(follow_item, rules))


    return follow_table[expr]


if __name__ == "__main__":
    production_rules = read_rules("rules.txt")
    print("Production Rules:")
    # Print Production Rules
    for rule in production_rules:
        print(rule)
    # Generate Tables
    rules = parse_rules(production_rules)
    first_table = get_table(production_rules)
    follow_table = get_table(production_rules)
    visited_list = get_table(production_rules)
    # Compute first and follow set
    for rule in rules:
        first(rule, rules)
        follow(rule, rules)
    for i in range(50):
        print("-", end="")
    print()
    # Print first set
    for rule in first_table:
        print(f"FIRST({rule}) = ", first_table[rule])
    for i in range(50):
        print("-", end="")
    print()
    # Print follow set
    for rule in follow_table:
        print(f"FOLLOW({rule}) = ", follow_table[rule])
