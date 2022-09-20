from prettytable import PrettyTable


class Lexer(object):
    def __init__(self, filename):
        self.contents = self.read_file(filename)
        self.keywords = [
            "def",
            "if",
            "return",
            "True",
            "False",
        ]
        self.operators = [
            "=",
            "+",
            "-",
            "*",
            "/",
            "==",
            ">",
            "<",
            ">=",
            "<=",
        ]
        self.tokens = []

    def read_file(self, filename):
        with open(filename, "r") as f:
            content = f.read()
        return list(content)

    def is_integer(self, lexeme):
        try:
            if all([x in range(0, 10)
                   for x in map(lambda a: int(a), list(lexeme))]):
                return True
            return False
        except BaseException:
            return False

    def tokenize(self):
        line_number = 1
        current_lexeme = ""
        for index, character in enumerate(self.contents):
            if character == " " or character == "\n":
                if character == "\n":
                    line_number += 1
                current_lexeme = ""
            elif character in ":(),":
                # print(f">> {character}")
                self.tokens.append(
                    Token(
                        character,
                        "SPECIAL_SYMBOL",
                        line_number))
                current_lexeme = ""
            elif character in self.operators:
                current_lexeme += character
                if current_lexeme + \
                        self.contents[index + 1] not in self.operators:
                    # print(f">> {current_lexeme}")
                    self.tokens.append(
                        Token(current_lexeme, "OPERATOR", line_number))
                    current_lexeme = ""
            else:
                current_lexeme += character
                if current_lexeme in self.keywords:
                    self.tokens.append(
                        Token(current_lexeme, "KEYWORD", line_number))
                    # print(">>", current_lexeme)
                else:
                    if index <= len(self.contents) - 2:
                        if self.contents[index + 1] in list("(), :\n="):
                            if not current_lexeme in " \n":
                                if self.is_integer(current_lexeme):
                                    self.tokens.append(
                                        Token(current_lexeme, "INTEGER", line_number))
                                    # print(">>", current_lexeme)
                                else:
                                    self.tokens.append(
                                        Token(current_lexeme, "IDENTIFIER", line_number))
                                    # print(">>", current_lexeme)


class Token(object):
    def __init__(self, lexeme, token_type, line_number):
        self.lexeme = lexeme
        self.token_type = token_type
        self.line_number = line_number

    def __repr__(self):
        return f"<{self.token_type}\t\t'{self.lexeme}'\t\tLine:{self.line_number}>"


if __name__ == "__main__":
    lexer = Lexer("code.txt")
    lexer.tokenize()

    # Symbol Table
    table = PrettyTable()
    table.field_names = ["S.N.", "Lexeme", "Token Type", "Line Number"]

    for index, token in enumerate(lexer.tokens):
        # if token.token_type == "IDENTIFIER":
        table.add_row([index + 1, token.lexeme, token.token_type, token.line_number])

    print(table)
