import itertools
import sys
import pathlib
funktionen_path = pathlib.Path(__file__).parent.parent.absolute() / 'ast_to_asm'
sys.path.append(str(funktionen_path))
import funktionen as blocks

def parse(tokens):
    return parse_stmt(tokens)

'''Wrapper over blocks.FL_STAT'''
def follow_with(stmt):
    return blocks.FL_STAT(stmt)

def parse_stmt(tokens):
    try:
        (word, label) = next(tokens)
    except:
        # Create Epsilon-Block
        return blocks.FL_STAT("END")
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

tokens = None

def parse_expr(ts):
    global tokens
    tokens = ts
    em1 = parse_expr_m1()
    assert next(tokens)[1] in ["semicolon", "closed_bracket"]
    return em1

def parse_expr_m1():
    global tokens
    e0 = parse_expr_zero()
    token = next(tokens)
    if token[1] == "equals":
        return blocks.EXPRm1(e0, parse_expr_m1())
    backtrack(token)
    return blocks.EXPRm1(e0)

def parse_expr_zero():
    global tokens
    e1 = parse_expr_one()
    token = next(tokens)
    if token[1] == "plus":
        return blocks.EXPR0(e1, parse_expr_zero())
    backtrack(token)
    return blocks.EXPR0(e1)

def parse_expr_one():
    global tokens
    e2 = parse_expr_two()
    token = next(tokens)
    if token[1] == "multi":
        return blocks.EXPR1(e2, parse_expr_one())
    backtrack(token)
    return blocks.EXPR1(e2)

def parse_expr_two():
    global tokens
    token = next(tokens)
    if token[1] == "minus":
        return blocks.EXPR2(parse_expr_two())
    backtrack(token)
    return blocks.EXPR2(None, parse_expr_three())

def parse_expr_three():
    global tokens
    token = next(tokens)
    if token[1] == "ident":
        return blocks.EXPR3(token[0])
    elif token[1] == "lit":
        return blocks.EXPR3(None, token[0])
    assert token[1] == "open_bracket"
    em1 = parse_expr_m1()
    assert next(tokens)[1] == "closed_bracket"
    return blocks.EXPR3(None, None, em1)

def backtrack(*ts):
    global tokens
    tokens = itertools.chain(ts, tokens)