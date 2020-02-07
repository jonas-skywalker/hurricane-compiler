def parse_file(filename):
    c_code = get_source(filename)
    print(c_code)


def get_source(filename):
    with open(filename, "r") as infile:
        c_code = infile.read().replace('\n', '')
    #c_code = c_code.replace(" ", "")
    return c_code


if __name__ == '__main__':
    filename = "src/test.txt"
    parse_file(filename)

matches = [
    (["(", ")", "{", "}"], "bracket"),
    (["+", "-", "*", "/", "<="], "bin_op"),
    (["-"], "un_op"),
    (["input", "while", "print", "if"], "keyword"),
    (["int", ";", "="], "misc")
]

def lex(source):
    tokens = []
    trace = ""
    for c in source:
        if c.isspace():
            continue

        if not (c.isalpha() or c.isdigit()):
            def match(matches, clazz):
                global trace
                if trace in matches:
                    tokens.append((trace, clazz))
                    return True
                return False
            for m in matches:
                if match(*m):
                    continue
            else:
                if trace.isdigit():
                    tokens.append((trace, "literal"))
                    trace = ""
                    continue
                if trace.isalpha():
                    tokens.append((trace, "ident"))
                    trace = ""
                    continue


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
