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
        return ASSIGN(ident, expr, after)

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
    exp = []
    for (word, label) in tokens:
        if label in ["semicolon", "closed_bracket"]:
            exp.append((word, label))

    return parse_expr_zero(exp)

def parse_expr_zero(exp):
    for (i, (word, label)) in enumerate(exp):
        if label == "plus":
            index = i
            break
    else:
        return blocks.EXPR0(parse_expr_one(exp))
    e1 = exp[:index]
    e0 = exp[index + 1:]
    return blocks.EXPR1(parse_expr_one(e1), parse_expr_zero(e0))

def parse_expr_one(exp):
    for (i, (word, label)) in enumerate(exp):
        if label == "multi":
            index = i
            break
    else:
        return blocks.EXPR0(parse_expr_one(exp))
    e1 = exp[:index]
    e0 = exp[index + 1:]
    return blocks.EXPR2(parse_expr_two(e1), parse_expr_one(e0))

def parse_expr_two(exp):
    if exp[0][1] == "minus":
        return blocks.EXPR2("neg", parse_expr_two(exp[1:]))
    else:
        return blocks.EXPR2("e3", None, parse_expr_three(exp))

def parse_expr_three(exp):
    head = exp[0]
    ident = None
    lit = None
    e0 = None
    if exp[1] == "ident":
        ident = exp[0]
    elif exp[1] == "lit":
        lit = exp[0]
    else:
        assert head[1] == "open_bracket"
        assert exp[-1][1] == "closed_bracket"
        e0 = parse_expr_zero(exp[1:-1]) # Get rid of brackets
    return blocks.EXPR3(ident, lit, e0)