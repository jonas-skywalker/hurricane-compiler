import sys
import pathlib
p = pathlib.Path(__file__).parent.absolute() / 'parser'
sys.path.append(str(p))
import lexer
import parsing

def get_source(filename):
    with open(filename, "r") as infile:
        c_code = infile.read()
    return c_code

def construct_ast(filename):
    c_code = get_source(filename)
    ts = lexer.token_stream(c_code)
    ast = parsing.parse(ts)
    return ast

def compile(filename):
    ast = construct_ast(filename)
    print(ast.ausgabe(0))

if __name__ == '__main__':
    filename = "test.hc"
    compile(filename)
