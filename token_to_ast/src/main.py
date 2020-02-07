import funktionen as fn


b = fn.ASSIGN("y", fn.EXPR("4"), fn.FL_STAT("END"))
a = fn.ASSIGN("x", fn.EXPR("5"), fn.FL_STAT(b))
ia = fn.ASSIGN("c", fn.EXPR("3"), fn.FL_STAT("END"))
i = fn.IF_COND(fn.EXPR("3<3"), fn.FL_STAT("END"), fn.FL_STAT(a))
s = fn.START(i)
s.ausgabe()
