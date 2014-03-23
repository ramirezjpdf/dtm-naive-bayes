#naive bayes classifier	
class Atributo:
	def __init__(self, atribNome, valores):
		#nome do atributo classe
		self.atribNome = atribNome
		#lista de valore que  podem ser assumidos pelo atributo classe
		self.valores = valores
		
class ProbCondAtribDadaClasse:
	def __init__(self, atribNome, classeValor):
		#valor da classe em que o condicionamento eh feito
		self.classeValor = classeValor
		#nome do atributo para o qual se calcula as probsbilidades condicionais
		self.atribNome = atribNome
		#dicionario chave valor do atributo, valor prob do atributo assumir esse valor dado a classe
		self.probsConds = {}
		
class Classificador:
	def __init__(self, classe):
		#objeto da classe Atributo que representa a classe
		self.classe = classe
		#lista de probabilidades condicionais dos atributos dado o valor de alguma classe
		self.probsConds = []
		#dicionario probabilidades das classes a priori
		self.probsPriori = {}
		
	def getProbCond(self, atribNome, atribValor, classeValor):
		result = [ p.probsConds[atribValor] for p in self.probsConds if p.classeValor == classeValor and p.atribNome == atribNome ]
		return None if not result else result[0]
		
	def calcProbCondClasseDadoAtributos(self, classeValor, atribs):
		prob = self.probsPriori[classeValor]
		for atribNome in atribs.keys():
			prob *= self.getProbCond(atribNome, atribs[atribNome], classeValor)
		return prob
		
	def classifica(self, data):
		probs = {}
		for classeValor in self.classe.valores:
			calcProbCondClasseDadoAtributo(classeNome, data)
		return max(probs, key=probs.get)
		
class Treinador:
	SAMPLE_CORRECTION_PSEUDOCOUNT = 0.0001
	
	def __init__(self, datum, classe, atribs):
		#lista de objetos de uma classe que representa um dado tipo RendimentoEscolar
		self.datum = datum
		#objeto da classe Atributo que representa a classe
		self.classe = classe
		#lista objetos da classe Atributo que representam os atributos
		self.atribs = atribs
		
	def calcProbCond(self, atribNome, atribValor, classeNome, classeValor):
		denominador = len([data for data in self.datum if data.__dict__[classeNome] == classeValor])
		numerador = len([data for data in self.datum if(data.__dict__[classeNome] == classeValor and data.__dict__[atribNome] == atribValor)])
		return numerador / float(denominador)
	
	def calcProbClassePriori(self, classeValor):
		denominador = len(self.datum)
		numerador = len([data for data in self.datum if data.__dict__[self.classe.atribNome] == classeValor])
		return numerador / float(denominador)
	
	def calcProbsPrioriParaTodasClasses(self):
		probsPriori = {}
		for classeValor in self.classe.valores:
			probsPriori[classeValor] = self.calcProbClassePriori(classeValor)
		return probsPriori

	'''dado um valor de uma classe e um nome de atributo,
		devo calcular as probCond de tds os valores desse atributo
		dado o valor da classe'''
	def calcProbCondAtribDadaClasse(self, atributo, classeValor):
		probCondAtribDadaClasse = ProbCondAtribDadaClasse(atributo.atribNome, classeValor)
		for atribValor in atributo.valores:
			probCond = self.calcProbCond(atributo.atribNome, atribValor, self.classe.atribNome, classeValor)
			probCondAtribDadaClasse.probsConds[atribValor] = probCond if probCond > 0.0 else Treinador.SAMPLE_CORRECTION_PSEUDOCOUNT
		return probCondAtribDadaClasse
	
	def calcProbsCondsParaTodosAtribsParaTodasClasses(self):
		probsConds = []
		for classeValor in self.classe.valores:
			#print classeValor
			for atrib in self.atribs:
				#print "\t" + atrib.atribNome
				p = self.calcProbCondAtribDadaClasse(atrib, classeValor)
				probsConds.append(p)
				#print "\t\t" + str(p.probsConds)
		return probsConds
	
	def treina(self):
		classificador = Classificador(self.classe)
		classificador.probsConds = self.calcProbsCondsParaTodosAtribsParaTodasClasses()
		classificador.probsPriori = self.calcProbsPrioriParaTodasClasses()
		return classificador
			
		
