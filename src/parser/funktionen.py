class IF_COND:

    # expr: Bedingung unter der der if-Block ausgeführt wird
    # if_stat: Programmcode der ausgeführt wird wenn expr == True
    # fl_stat: Der immer auf den if-Block folgende Code
    def __init__(self, expr, if_stat, fl_stat):
        self.expr = expr
        self.if_stat = if_stat
        self.fl_stat = fl_stat

    def ausgabe(self, v):
        return (v) * " " + "IF\n" + self.expr.ausgabe(v + 1) + "\n" + self.if_stat.ausgabe(
            v + 2) + "\n" + self.fl_stat.ausgabe(v + 1)


class ASSIGN:

    # id: Name der Variable
    # expr: Wert der Variable (bisher nur integer)
    # fl_stat: Die folgenden Statements
    def __init__(self, id, expr, fl_stat):
        self.id = id
        self.expr = expr
        self.fl_stat = fl_stat

    def ausgabe(self, v):
        return (v) * " " + "ASSIGN\n" + (v + 1) * " " + self.id + "\n" + self.expr.ausgabe(
            v + 2) + "\n" + self.fl_stat.ausgabe(v + 1)


class WHILE:

    # expr: Bedingung unter der der while-Block ausgeführt wird
    # wh_stat: Programmcode der ausgeführt wird wenn expr == True
    # fl_stat: Der immer auf den if-Block folgende Code
    def __init__(self, expr, wh_stat, fl_stat):
        self.expr = expr
        self.wh_stat = wh_stat
        self.fl_stat = fl_stat

    def ausgabe(self, v):
        return (v) * " " + "WHILE\n" + self.expr.ausgabe(v + 1) + "\n" + self.wh_stat.ausgabe(
            v + 2) + "\n" + self.fl_stat.ausgabe(v + 1)


class FL_STAT:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat

    def ausgabe(self, v):
        if self.fl_stat == "END":
            return (v) * " " + self.fl_stat
        else:
            return self.fl_stat.ausgabe(v)


class START:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat

    def ausgabe(self):
        print(self.fl_stat.ausgabe(0))


class EXPR0:
    def __init__(self, e1, summand0=None):
        self.e1 = e1
        self.summand0 = summand0


class EXPR1:
    def __init__(self, e2, factor1=None):
        self.e2 = e2
        self.factor1 = factor1


class EXPR2:
    '''self.type = "neg" | "e3" '''

    def __init__(self, type, negated2=None, e3=None):
        self.type = type
        self.negated2 = negated2
        self.e3 = e3


class EXPR3:
    '''type = "ident" | "lit" | "e0" '''

    def __init__(self, type, ident=None, lit=None, e0=None):
        self.type = type
        self.ident = ident
        self.lit = lit
        self.e0 = e0
    
    def generate_asm(self):
        return self.e0