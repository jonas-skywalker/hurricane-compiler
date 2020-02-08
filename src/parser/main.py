import lexer as lx
import parsing as ps

def construct_ast(filename):
    with open(filename) as file:
        source = file.read()
    ts = lx.token_stream(source)
    ast = ps.parse(ts)
    return ast

pr = construct_ast("addition.hc")
print(pr.ausgabe(0))
asm = pr.generiere_asm()

with open("addition.asm", "w") as datei:
    datei.write(asm)
