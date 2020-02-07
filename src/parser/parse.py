import funktionen as blocks
import itertools

def parse_stmt(tokens):
    (word, label) = next(tokens)
    if lable == "closed_bracket":
        return Epsilon-Block
    elif label == "ident":
        return parse_assign(word, tokens)
    elif label == "int":
        return parse_decl(tokens)
    return eval("parse_" + label + "(tokens)")

# Consumed identifier, head is =
def parse_assign(ident, tokens):
    assert next(tokens)[1] == "assign"
    word = next(tokens)
    if word[1] == "input":
        for (a, b) in zip(tokens, "();"):
            assert a == b
        after = parse_stmt(tokens)
        return built input-block
    else:
        newtokens = itertools.chain([word], tokens)
        expr = parse_expr(newtokens)
        after = parse_stmt(newtokens)
        return built assign-block

def parse_decl(tokens):
    ident = next(tokens)
    assert ident[1] == "ident"
    assert next(tokens) == "semicolon"
    after = parse_stmt(tokens)
    return built decl-block

STMT = 0
EXPR = 1

@parameterized
def parses(fn, *nodes):
    def parse_func(tokens):
        parsed = []
        for node in nodes:
            assert next(tokens)[1] == "open_bracket"
            p = None
            if node == STMT:
                p = parse_stmt(tokens)
            elif node == EXPR:
                p = parse_expr(tokens)
            parsed.append(p)
        parsed.append(parse_stmt(tokens))
        return fn(*parsed)
    return parse_func

@parses(EXPR, STMT)
def parse_while(condition, block, after):
    return while-block

@parses(EXPR, STMT)
def parse_if(condition, block, after):
    return if-block

@parses(EXPR)
def parse_print(value, after):
    return print-block

def parse_expr(tokens):
    exp = lalb
    for (word, label) in tokens:
        if label in ["semicolon", "closed_bracket"]:

    return parse_expr_one(tokens)

def parse_expr_one(tokens):
    (word, label) = next(tokens)
