import copy

env = {}
s = 0

watcher_s = 0

class IF_COND:

	# expr: Bedingung unter der der if-Block ausgeführt wird
	# if_stat: Programmcode der ausgeführt wird wenn expr == True
	# fl_stat: Der immer auf den if-Block folgende Code
	def __init__(self, expr, if_stat, fl_stat):
		self.expr = expr
		self.if_stat = if_stat
		self.fl_stat = fl_stat

	def ausgabe(self, v):
		return v * " " + "IF\n" + self.expr.ausgabe(v + 1) + "\n" + self.if_stat.ausgabe(
			v + 2) + "\n" + self.fl_stat.ausgabe(v)


class WHILE:

	# expr: Bedingung unter der der while-Block ausgeführt wird
	# wh_stat: Programmcode der ausgeführt wird wenn expr == True
	# fl_stat: Der immer auf den if-Block folgende Code
	def __init__(self, expr, wh_stat, fl_stat):
		self.expr = expr
		self.wh_stat = wh_stat
		self.fl_stat = fl_stat

	def ausgabe(self, v):
		return v * " " + "WHILE\n" + self.expr.ausgabe(v + 1) + "\n" + self.wh_stat.ausgabe(
			v + 1) + "\n" + self.fl_stat.ausgabe(v)


class ASSIGN:

	# id: Name der Variable
	# expr: Wert der Variable (bisher nur integer)
	# fl_stat: Die folgenden Statements
	def __init__(self, id, expr, fl_stat):
		self.id = id
		self.expr = expr
		self.fl_stat = fl_stat

	def ausgabe(self, v):
		return v * " " + "ASSIGN\n" + self.id + "\n" + self.expr.ausgabe(v + 1) + "\n" +\
			   self.fl_stat.ausgabe(v)

	def generiere_asm(self):
		global s

		asm = self.expr.generiere_asm()

		# Speicher Offset von $sp zu der Variable
		env[self.id] = s
		# Verschiebe Offset um 4 Byte
		s -= 4

		asm += self.fl_stat.generiere_asm()

		return asm

class FL_STAT:

	def __init__(self, fl_stat):
		self.fl_stat = fl_stat # Das hier ist ein String, soll aber nicht

	def ausgabe(self, v):
		if self.fl_stat == "END":
			return self.fl_stat
		else:
			return self.fl_stat.ausgabe(v)

	def generiere_asm(self):
		if self.fl_stat == "END":
			return "\n"
		else:
			return self.fl_stat.generiere_asm()

class START:

	def __init__(self, fl_stat):
		self.fl_stat = fl_stat

	def ausgabe(self):
		print(self.fl_stat.ausgabe(0))


class EXPRm1:
	def __init__(self, e0, comparandm1=None):
		self.e0 = e0
		self.comparandm1 = comparandm1

	def ausgabe(self, v):
		ausgabe = v * " "
		if self.comparandm1 != None:
			ausgabe = "==\n" + self.comparandm1.ausgabe(v)
		return self.e0.ausgabe(v + 1) + ausgabe

	def generiere_asm(self):
		return self.e0.generiere_asm()

class EXPR0:

	# EXPR0 nimmt Instanz von Typ EXPR1 (e1)
	# summand0: optionaler Summand von Typ (e0)
	def __init__(self, e1, summand0=None):
		self.e1 = e1
		self.summand0 = summand0

	def ausgabe(self, v):
		ausgabe = v * " "
		if self.summand0 != None:
			ausgabe = "+\n"+self.summand0.ausgabe(v + 1)
		return self.e1.ausgabe(v + 1)+ausgabe

	def generiere_asm(self):
		global s
		global watcher_s
		#--Erinnerung:--#
		# Stack-Pointer wird in ASSIGN.generiere_asm() dekrementiert

		# Speicher den Wert von dem linken Summant in $t0
		asm = self.e1.generiere_asm()

		# Speicher den Wert von $t0 in den Stack an 0($sp)
		asm += "sw $t0 "+str(s)+"($sp)\n"


		# Wenn ein rechter Summant vorhanden ist dann mache das:
		if self.summand0 != None:
			# Der Offset wird geupdatet um den nächsten RAM Eintrag weiter unten im Stack zu speichern
			s -= 4
			# Speicher den Wert des rechten Summanten in $t0
			asm += self.summand0.generiere_asm()

			# Der Offset wird geupdatet um wieder wie normal auf den oberen Eintrag im Stack zuzugreifen
			s += 4
			# Speicher den Wert in 0($sp) in $t1
			asm += "lw $t1 "+str(s)+"($sp)\n"

			# Addiere den Wert in $t0 udn in $t1 in $t0
			asm += "add $t0 $t0 $t1\n"

			# Speicher den Wert von $t0 in 0($sp)
			asm += "sw $t0 "+str(s)+"($sp)"

		return asm


class EXPR1:

	# EXPR1 nimmt Instanz von Typ EXPR2 (e2)
	# factor1: optionaler Faktor von Typ EXPR1 (factor1)
	def __init__(self, e2, factor1=None):
		self.e2 = e2
		self.factor1 = factor1

	def ausgabe(self, v):
		ausgabe = v * " "
		if self.factor1 != None:
			ausgabe = "*\n"+self.factor1.ausgabe(v + 1)
		return self.e2.ausgabe(v + 1)+ausgabe

	def generiere_asm(self):
		global s
		global watcher_s
		#--Erinnerung:--#
		# Stack-Pointer wird in ASSIGN.generiere_asm() dekrementiert

		# Speicher den Wert von dem linken Faktor in $t0
		asm = self.e2.generiere_asm()

		# Speicher den Wert von $t0 in den Stack an 0($sp)
		asm += "sw $t0 "+str(s)+"($sp)\n"
	

		# Wenn ein rechter Faktor vorhanden ist dann mache das:
		if self.factor1 != None:
			# Der Offset wird geupdatet um den nächsten RAM Eintrag weiter unten im Stack zu speichern
			s -= 4

			# Speicher den Wert des rechten Faktor in $t0
			asm += self.factor1.generiere_asm()

			# Der Offset wird geupdatet um wieder wie normal auf den oberen Eintrag im Stack zuzugreifen
			s += 4
			# Speicher den Wert in 0($sp) in $t1
			asm += "lw $t1 "+str(s)+"($sp)\n"

			# Addiere den Wert in $t0 udn in $t1 in $t0
			asm += "mul $t0 $t0 $t1\n"

			# # Speicher den Wert von $t0 in 0($sp)
			# asm += "sw $t0 "+str(s)+"($sp)\n"
		
		return asm


class EXPR2:

	# EXPR2 nimmt entweder einen negative Instanz von Typ EXPR2 (negated2)
	# oder nimmt Instanz von Typ EXPR3 (e3)
	# Keine Rechnung
	def __init__(self, negated2=None, e3=None):
		self.negated2 = negated2
		self.e3 = e3
	
	def ausgabe(self, v):
		if self.negated2 != None:
			ausgabe = "\n-" +self.negated2.ausgabe(v + 1)
		else:
			ausgabe = self.e3.ausgabe(v + 1)
		return v * " " + ausgabe

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

	def ausgabe(self, v):
		if self.ident != None:
			ausgabe = self.ident
		elif self.lit != None:
			ausgabe = self.lit
		else:
			ausgabe = "(\n" + self.e0.ausgabe(v + 1) + "\n" + v * " " + ")"
		return v * " " + ausgabe
	
	def generiere_asm(self):
		asm = ""
		if self.ident != None:
			# 
			voffset = env[self.ident]
			asm = "lw $t0 "+str(voffset)+"($sp)\n"
			#asm = "li $t0 5\n"
		elif self.lit != None:
			asm = "li $t0 "+self.lit+"\n"
		else:
			asm = self.e0.generiere_asm()
		return asm
