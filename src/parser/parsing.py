import funktionen as blocks
import itertools

def parse(tokens):
    return parse_stmt(tokens)

'''Wrapper over blocks.FL_STAT'''
def follow_with(stmt):
    return blocks.FL_STAT(stmt)

def parse_stmt(tokens):
    (word, label) = next(tokens)
    if label == "closed_bracket":
        # Create Epsilon-Block
        return blocks.FL_STAT("END")
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
        # Create Input-Block
        return None
    else:
        newtokens = itertools.chain([word], tokens)
        expr = parse_expr(newtokens)
        after = parse_stmt(newtokens)
        return blocks.ASSIGN(ident, expr, follow_with(after))

def parse_decl(tokens):
    ident = next(tokens)
    assert ident[1] == "ident"
    assert next(tokens) == "semicolon"
    after = parse_stmt(tokens)
    # Create Declaration-Block
    return None

STMT = 0
EXPR = 1

def parameterized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

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
    # Create While-Block
    return blocks.WHILE(condition, block, follow_with(after))

@parses(EXPR, STMT)
def parse_if(condition, block, after):
    # Create If-Block
    return blocks.IF_COND(condition, block, follow_with(after))

@parses(EXPR)
def parse_print(value, after):
    # Create Print-Block
    return None

def parse_expr(tokens):
    exp = []
    for (word, label) in tokens:
        if label in ["semicolon", "closed_bracket"]:
            break
        exp.append((word, label))
    return parse_expr_zero(exp)

def parse_expr_m1(exp):
    for (i, (word, label)) in enumerate(exp):
        if label == "equals":
            index = i
            break
    else:
        return blocks.EXPRm1(parse_expr_zero(exp))
    e1 = exp[:index]
    e0 = exp[index + 1:]
    return blocks.EXPRm1(parse_expr_zero(e1), parse_expr_m1(e0))

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
        return blocks.EXPR2(parse_expr_two(exp))
    e1 = exp[:index]
    e0 = exp[index + 1:]
    return blocks.EXPR2(parse_expr_two(e1), parse_expr_one(e0))

def parse_expr_two(exp):
    if exp[0][1] == "minus":
        return blocks.EXPR2(parse_expr_two(exp[1:]))
    else:
        return blocks.EXPR2(None, parse_expr_three(exp))

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