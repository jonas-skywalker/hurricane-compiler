# SUPERDUPER WICHTIGEN GLOBALEN VARIABLEN
AUTOBOTS = r"""
________  ___  ___  _________  ________  ________  ________  _________  ________
|\   __  \|\  \|\  \|\___   ___\\   __  \|\   __  \|\   __  \|\___   ___\\   ____\
\ \  \|\  \ \  \\\  \|___ \  \_\ \  \|\  \ \  \|\ /\ \  \|\  \|___ \  \_\ \  \___|_
 \ \   __  \ \  \\\  \   \ \  \ \ \  \\\  \ \   __  \ \  \\\  \   \ \  \ \ \_____  \
  \ \  \ \  \ \  \\\  \   \ \  \ \ \  \\\  \ \  \|\  \ \  \\\  \   \ \  \ \|____|\  \
   \ \__\ \__\ \_______\   \ \__\ \ \_______\ \_______\ \_______\   \ \__\  ____\_\  \
    \|__|\|__|\|_______|    \|__|  \|_______|\|_______|\|_______|    \|__| |\_________\
                                                                           \|_________|
"""

ASSEMBLE = r"""
________  ________   ________  _______   _____ ______   ________  ___       _______
|\   __  \|\   ____\ |\   ____\|\  ___ \ |\   _ \  _   \|\   __  \|\  \     |\  ___ \
\ \  \|\  \ \  \___|_\ \  \___|\ \   __/|\ \  \\\__\ \  \ \  \|\ /\ \  \    \ \   __/|
 \ \   __  \ \_____  \\ \_____  \ \  \_|/_\ \  \\|__| \  \ \   __  \ \  \    \ \  \_|/__
  \ \  \ \  \|____|\  \\|____|\  \ \  \_|\ \ \  \    \ \  \ \  \|\  \ \  \____\ \  \_|\ \
   \ \__\ \__\____\_\  \ ____\_\  \ \_______\ \__\    \ \__\ \_______\ \_______\ \_______\
    \|__|\|__|\_________\\_________\|_______|\|__|     \|__|\|_______|\|_______|\|_______|
             \|_________\|_________|
"""

# Weniger wichtige globale Variablen
env = {}
s = 0

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

    def generiere_python(self, v):
        return (v)*" " + "if " + self.expr.generiere_python(v) + ":\n" + self.if_stat.generiere_python(v+4) + "\n" + self.fl_stat.generiere_python(v)

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
    
    def generiere_python(self, v):
        return (v)*" " + "while " + self.expr.generiere_python(v) + ":\n" + self.wh_stat.generiere_python(v+4) + "\n" + self.fl_stat.generiere_python(v)

class ASSIGN:

    # id: Name der Variable
    # expr: Wert der Variable (bisher nur integer)
    # fl_stat: Die folgenden Statements
    def __init__(self, id, expr, fl_stat):
        self.id = id
        self.expr = expr
        self.fl_stat = fl_stat

    def ausgabe(self, v):
        return (v)*" " + "ASSIGN\n" + (v+1)*" " + self.id + "\n" + self.expr.ausgabe(v+2)+ "\n" + self.fl_stat.ausgabe(v+1)

    def generiere_python(self, v):
        return (v)*" " + self.id + "=" + self.expr.generiere_python(v) + "\n" + self.fl_stat.generiere_python(v)

    def generiere_asm(self, s, env):
        # Speicher Variable
        env[self.id] = s
        # Verschiebe Offset
        s -= 4

class EXPR:

    # expr: String
    def __init__(self, arg):
        arg = arg.split()
        self.lhand = str(arg[0])
        if len(arg) != 3:
            self.op = ""
            self.rhand = ""
        else:
            self.op = str(arg[1])
            self.rhand = str(arg[2])
        
    def ausgabe(self, v):
        return (v)*" " + self.lhand + self.op + self.rhand
    
    def generiere_python(self, v):
        return (v)*" " + self.lhand + self.op + self.rhand
    
    # Addiert zwei Zahlen, sonst nichts
    def generiere_asm(self, s, r0, r1):
        # Speicher erste Zahl im Stack:
        anweisung = "li "+r0+" "+self.lhand+"\n"
        # Addiere zwei Zahlen
        anweisung += self.generate_op()+" "+r1+" "+r0+" "+self.rhand+"\n"
        # Schreibe in den Stack
        anweisung += "sw "+r1+" "+str(s)+"($sp)"+"\n"
        return anweisung
    
    def generate_op():
        if self.op == "+":
            return "add"
        if self.op == "-":
            return "sub"

class FL_STAT:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat

    
    def ausgabe(self, v):
        if self.fl_stat == "END":
            return (v)*" " + self.fl_stat
        else:
            return self.fl_stat.ausgabe(v)
    
    def generiere_python(self, v):
        if self.fl_stat == "END":
            return (v)*" " + "pass"
        else:
            return self.fl_stat.generiere_python(v)

class START:

    def __init__(self, fl_stat):
        self.fl_stat = fl_stat
    
    def ausgabe(self):
        print(self.fl_stat.ausgabe(0))
    
    def generiere_python(self):
        return self.fl_stat.generiere_python(0)


def optimus_prime(start):
    pass

