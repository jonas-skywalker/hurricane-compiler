import funktionen as fn

# Programm geht von unten nach oben durch

ex0 = fn.ASSIGN("x", fn.EXPR0(
		fn.EXPR1(
			fn.EXPR2(
				e3=fn.EXPR3(lit="4")
				),
		factor1=fn.EXPR1(
			fn.EXPR2(
				e3=fn.EXPR3(lit="4")
				)
			)
		)
	), fn.FL_STAT("END"))

print(ex0.generiere_asm())
print(fn.env)

ex1 = fn.ASSIGN("y", fn.EXPR0(
		fn.EXPR1(
			fn.EXPR2(
				e3=fn.EXPR3(lit="5")
				),
		factor1=fn.EXPR1(
			fn.EXPR2(
				e3=fn.EXPR3(lit="5")
				)
			)
		)
	), fn.FL_STAT("END"))

print(ex1.generiere_asm())
print(fn.env)

ex2 = fn.ASSIGN("z", fn.EXPR0(
		fn.EXPR1(
			fn.EXPR2(
				e3=fn.EXPR3(ident="x")
			)
		),
		summand0=fn.EXPR0(
			fn.EXPR1(
				fn.EXPR2(
					e3=fn.EXPR3(ident="y")
				)
			)
		)
	), fn.FL_STAT("END"))


print(ex2.generiere_asm())
print(fn.env)