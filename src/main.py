def lex(source):
    tokens = []
    trace = ""
    for c in source:
        if c.isspace():
            continue

        if not (c.isalpha() or c.isdigit())
            def match(matches, clazz):
                global trace
                if trace in matches:
                    tokens.append((trace, clazz))
                    return True
                return False

        matches = [
            (["(", ")", "{", "}"], "bracket"),
            (["+", "-", "*", "/", "<="], "bin_op"),
            (["-"], "un_op"),
            (["input", "while", "print", "if"], "keyword"),
            (["int", ";"], "misc")
        ]

        trace += c

def match_brackets(word):
    brackets = ["(", ")", "{", "}"]
    if

def match_operators(word):
    operators = ["+", "-", "*", "/", "<="]
    if word in operators:
        return (word, "operator")

def match_keywords(word):
    keywords = ["input", "while", "print", "if"]
    if word in keywords:
        return (word, "keyword")