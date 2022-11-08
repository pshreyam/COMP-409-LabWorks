def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def remove_left_recursion(rules):
    # Divide the rules
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))

        alpha_terms = []
        beta_terms = []

        for term in right_side:
            if term.startswith(A):
                alpha_term = term.replace(A, "")
                alpha_terms.append(alpha_term)
            else:
                beta_terms.append(term)
        # Use the rule
        # A → Aα1| Aα2|…| Aαn| β1 | β2 | …| βm
        # we replace the A-production by
        # A → β1A'| β2A'|…|βmA'
        # A' → α1A'| α2A'|…| αnA'|ε

        if len(alpha_terms) > 0:
            beta_right_side = " | ".join([f"{beta}{A}'" for beta in beta_terms]).strip()
            rules.append(f"{A} -> {beta_right_side}")
            alpha_right_side = " | ".join([f"{alpha}{A}'" for alpha in alpha_terms]).strip() + " | ε"
            rules.append(f"{A}' -> {alpha_right_side}")
            rules.remove(rule)

    return rules


if __name__ == "__main__":
    production_rules = read_rules("rules.txt")
    print("Production Rules:")
    for rule in production_rules:
        print(rule)
    new_rules = remove_left_recursion(production_rules[:])
    print("After removing left recursion:")
    for rule in new_rules:
        print(rule)
