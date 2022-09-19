import os

filename = "code.txt"


def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()

    return list(content)


buffer = read_file(filename)

keywords = ["import", "def", "print"]

operators = {
    "=" : "<assignop>",
    "+" : "<addop>",
    "-" : "<subop>",
    "*" : "<multop>",
    "/" : "<divop>",
    "==": "<eqop>",
    ">" : "<gtop>",
    "<" : "<ltop>",
    ">=": "<gteop>",
    "<=": "<lteop>",
}

identifiers = ["keywords", "operators"]

# print(buffer)

current_lexeme = []

# for i in range(len(buffer)):
#     current_lexeme.append(buffer[i])
#     if "".join(current_lexeme) in keywords:
#         if "".join([*current_lexeme, buffer[i+1]]) not in keywords:
#             print("Keyword")
#             current_lexeme = []
