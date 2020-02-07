import funktionen as fn

# Programm geht von unten nach oben durch

ex0_0 = fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(lit="2"))), fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(lit="3")))))
a = fn.ASSIGN("x", ex0_0, fn.FL_STAT("END"))

ex0_1 = fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(lit="2"))), fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(lit="3")))))
b = fn.ASSIGN("y", ex0_1, fn.FL_STAT("END"))

ex_0_2 = fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(ident="y"))), fn.EXPR0(fn.EXPR1(fn.EXPR2(fn.EXPR3(ident="x")))))
c = fn.ASSIGN("z", ex_0_2, fn.FL_STAT("END"))

print(a.generiere_asm("$t0", "$t1"))
print(fn.s)
print(fn.env)
print()

print(b.generiere_asm("$t0", "$t1"))
print(fn.s)
print(fn.env)
print()

print(c.generiere_asm("$t0", "$t1"))
print(fn.s)
print(fn.env)
print()
