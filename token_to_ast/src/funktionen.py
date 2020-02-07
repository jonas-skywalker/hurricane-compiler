class IF_COND:

    # expr: Bedingung unter der der if-Block ausgeführt wird
    # if_stat: Programmcode der ausgeführt wird wenn expr == True
    # fl_stat: Der immer auf den if-Block folgende Code
    def __init__(self, expr, if_stat, fl_stat):
        self.expr = expr
        self.if_stat = if_stat
        self.fl_stat = fl_stat
    
    def ausgabe(self, v):
        return (v)*" " + "IF\n" + self.expr.ausgabe(v+1) + "\n" + self.if_stat.ausgabe(v+2) + "\n" + self.fl_stat.ausgabe(v+1)

class ASSIGN:

    def __init__(self, id, expr, fl_stat):
        self.id = id
        self.expr = expr
        self.fl_stat = fl_stat
    
    def ausgabe(self, v):
        return (v)*" " + "ASSIGN\n" + (v+1)*" " + self.id + "\n" + self.expr.ausgabe(v+2)+ "\n" + self.fl_stat.ausgabe(v+1)
    
class EXPR:

    def __init__(self, expr):
        self.expr = expr
    
    def ausgabe(self, v):
        return (v)*" " + self.expr

class FL_STAT:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat

    
    def ausgabe(self, v):
        if self.fl_stat == "END":
            return (v)*" " + self.fl_stat
        else:
            return self.fl_stat.ausgabe(v)

class START:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat
    
    def ausgabe(self):
        print(self.fl_stat.ausgabe(0))