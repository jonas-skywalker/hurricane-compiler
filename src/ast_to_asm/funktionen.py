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
		return (v) * " " + "IF\n" + self.expr.ausgabe(v + 1) + "\n" + self.if_stat.ausgabe(
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


class ASSIGN:

	# id: Name der Variable
	# expr: Wert der Variable (bisher nur integer)
	# fl_stat: Die folgenden Statements
	def __init__(self, id, expr, fl_stat):
		self.id = id
		self.expr = expr
		self.fl_stat = fl_stat

	def ausgabe(self, v):
		return (v) * " " + "ASSIGN\n" + (v + 1) * " " + self.id + "\n" + self.expr.ausgabe() + "\n" + self.fl_stat.ausgabe(v + 1)

	def generiere_asm(self, r0, r1):
		global s

		asm = self.expr.generiere_asm()#r0, r1)

		# Speicher Offset von $sp zu der Variable
		env[self.id] = s
		# Verschiebe Offset um 4 Byte
		s -= 4

		return asm

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


class EXPRm1:
	def __init__(self, e0, comparandm1=None):
		self.e0 = e0
		self.comparandm1 = comparandm1

class EXPR0:

	# EXPR0 nimmt Instanz von Typ EXPR1 (e1)
	# summand0: optionaler Summand von Typ (e0)
	def __init__(self, e1, summand0=None):
		self.e1 = e1
		self.summand0 = summand0

	def ausgabe(self):
		ausgabe = ""
		if self.summand0 != None:
			ausgabe = "+"+self.summand0.ausgabe()
		return self.e1.ausgabe()+ausgabe

	def generiere_asm(self):
		global s
		# Schreibe die Zahl n $to
		# Wenn eine Variable aufgerufen wird dann wird der lw-Befehl verwendet,
		# sonst wird eine Zahl in den Register geladen
		asm = "li $t1 0\n"
		asm += self.e1.generiere_asm()+"\n"
		asm += "sw $t0 "+str(s)+"($sp)\n"
		asm += "subi $sp $sp 4\n"
		s -= 4
		if self.summand0 != None:
			asm += self.summand0.generiere_asm()+"\n"
		asm += "lw $t1 "+str(s)+"($sp)\n"
		asm += "add $t0 $t0 $t1"
		return asm


class EXPR1:

	# EXPR1 nimmt Instanz von Typ EXPR2 (e2)
	# factor1: optionaler Faktor
	def __init__(self, e2, factor1=None):
		self.e2 = e2
		self.factor1 = factor1

	def ausgabe(self):
		ausgabe = ""
		if self.factor1 != None:
			ausgabe = "*"+self.factor1.ausgabe()
		return self.e2.ausgabe()+ausgabe

	def generiere_asm(self):
		asm = self.e2.generiere_asm()
		if self.factor1 != None:
			asm += " mul "+self.factor1.ausgabe()
		return asm


class EXPR2:

	# EXPR2 nimmt entweder einen negative Instanz von Typ EXPR2 (negated2)
	# oder nimmt Instanz von Typ EXPR3 (e3)
	# Keine Rechnung
	def __init__(self, negated2=None, e3=None):
		self.negated2 = negated2
		self.e3 = e3
	
	def ausgabe(self):
		if self.negated2 != None:
			ausgabe = self.negated2.ausgabe()
		else:
			ausgabe = self.e3.ausgabe()
		return ausgabe

	def generiere_asm(self):
		if self.negated2 != None:
			asm = self.negated2.generiere_asm()
		else:
			asm = self.e3.generiere_asm()
		return asm


class EXPR3:

	# Entweder Variablenname (ident), Zahl (lit) oder eingeklammerte Instanz von Typ EXPR0 (e0)
	def __init__(self, ident=None, lit=None, e0=None):
		self.ident = ident
		self.lit = lit
		self.e0 = e0

	def ausgabe(self):
		ausgabe = ""
		if self.ident != None:
			ausgabe = self.ident
		elif self.lit != None:
			ausgabe = self.lit
		else:
			ausgabe = self.e0.ausgabe()
		return ausgabe
	
	def generiere_asm(self):
		asm = ""
		if self.ident != None:
			# Offset der Variable von Null
			offset_der_variable = env[self.ident]
			# Offset vom jetzigen Stackpointer
			o = offset_der_variable - s
			asm += "lw $t0 "+str(o)+"($sp)"
		elif self.lit != None:
			asm = "li $t0 "+self.lit
		else:
			asm = self.e0.generiere_asm()
		return asm
