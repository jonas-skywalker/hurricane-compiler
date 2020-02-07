import funktionen as fn

# Programm geht von unten nach oben durch

# b = fn.ASSIGN("y", fn.EXPR("4"), fn.FL_STAT("END"))
# w = fn.WHILE(fn.EXPR("3 < 4"), fn.FL_STAT("END"), fn.FL_STAT(b))
# a = fn.ASSIGN("x", fn.EXPR("5 + 4"), fn.FL_STAT(w))
# ia = fn.ASSIGN("c", fn.EXPR("3"), fn.FL_STAT("END"))
# i = fn.IF_COND(fn.EXPR("3 < 3"), fn.FL_STAT("END"), fn.FL_STAT(a))
# s = fn.START(i)
# s.ausgabe()

# datei = open("src/ast_to_asm/out.py", "w")
# datei.write(s.generiere_python())

a = fn.ASSIGN("x", fn.EXPR("3 - 4"), fn.FL_STAT("END"))

# print(a.expr.generiere_asm(fn.s, r"$t0", r"$t1"))
print(fn.s)
print(a.generiere_asm(fn.s, fn.env, r"$t0", r"$t1"))

print(fn.env)