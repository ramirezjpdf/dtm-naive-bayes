#naive bayes classifier

import csv
import sys

NOME_CLASSE_RENDIMENTO_ESCOLAR = "regiao"
VALORES_CLASSE_RENDIMENTO_ESCOLAR = ["norte", "nordeste", "sudeste", "sul", "centroOeste"]

VALORES_ATTR_ANO = ["A", "B", "C", "D", "E"]

def converterCsvParaRendimentoEscolar(csvpath):
	rendimentosEscolares = []
	with open(csvpath, "rb") as csvfo:
		reader = csv.reader(csvfo, delimiter=";")
		#escapa a linha de header
		reader.next()
		rendimentosEscolares = [RendimentoEscolar(*row) for row in reader]
	return rendimentosEscolares

def criaTreinadorParaRendimentoEscolar(csvpath):
	classe = Atributo(atribNome=NOME_CLASSE_RENDIMENTO_ESCOLAR, valores=VALORES_CLASSE_RENDIMENTO_ESCOLAR)
	atribs = [Atributo("localizacao", ["urbana", "rural"]), Atributo("rede", ["Estadual", "Federal", "Municipal", "Particular"]),
			  Atributo("primeiroAno", VALORES_ATTR_ANO), Atributo("segundoAno", VALORES_ATTR_ANO), 
			  Atributo("terceiroAno",VALORES_ATTR_ANO), Atributo("quartoAno",VALORES_ATTR_ANO),
			  Atributo("quintoAno",VALORES_ATTR_ANO), Atributo("sextoAno",VALORES_ATTR_ANO),
			  Atributo("setimoAno",VALORES_ATTR_ANO), Atributo("oitavoAno",VALORES_ATTR_ANO),
			  Atributo("nonoAno",VALORES_ATTR_ANO)]
	datum = converterCsvParaRendimentoEscolar(csvpath)
	return Treinador(datum, classe, atribs)

class RendimentoEscolar:
	def __init__(self, regiao,localizacao,rede,primeiroAno,segundoAno,terceiroAno,quartoAno,quintoAno,sextoAno,setimoAno,oitavoAno,nonoAno):
		self.regiao = regiao
		self.localizacao = localizacao
		self.rede = rede
		self.primeiroAno = primeiroAno
		self.segundoAno = segundoAno
		self.terceiroAno = terceiroAno
		self.quartoAno = quartoAno
		self.quintoAno = quintoAno
		self.sextoAno = sextoAno
		self.setimoAno = setimoAno
		self.oitavoAno = oitavoAno
		self.nonoAno = nonoAno
	
	
	def __str__(self):
		return (str(self.regiao) + ", " +
			   str(self.localizacao) + ", " +
			   str(self.rede) + ", " +
			   str(self.primeiroAno) + ", " +
			   str(self.segundoAno) + ", " +
			   str(self.terceiroAno) + ", " +
			   str(self.quartoAno) + ", " +
			   str(self.quintoAno) + ", " +
			   str(self.sextoAno) + ", " +
			   str(self.setimoAno) + ", " +
			   str(self.oitavoAno) + ", " +
			   str(self.nonoAno))
			   
	def __repr__(self):
		return self.__str__()
	
class Atributo:
	def __init__(self, atribNome, valores):
		#nome do atributo classe
		self.atribNome = atribNome
		#lista de valore que  podem ser assumidos pelo atributo classe
		self.valores = valores
		
class ProbCondAtribDadaClasse:
	def __init__(self, atribNome, classeValor):
		self.atribNome = atribNome
		self.classeValor = classeValor
		self.probsConds = {}
		
class Classificador:
	def __init__(self, classe):
		#objeto da classe Atributo que representa a classe
		self.classe = classe
		#lista de probabilidades condicionais dos atributos dado o valor de alguma classe
		self.probsConds = []
		#dicionario probabilidades das classes a priori
		self.probsPriori = {}
		
	

class Treinador:
	SAMPLE_CORRECTION_PSEUDOCOUNT = 0.001
	
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
		print denominador
		numerador = len([data for data in self.datum if data.__dict__[self.classe.atribNome] == classeValor])
		print numerador
		return numerador / float(denominador)
	
	def calcProbsPrioriParaTodasClasses(self):
		probsPriori = {}
		for classeValor in classe.valores:
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
		classficador.probsPriori = self.calcProbsPrioriParaTodasClasses()
		return classificador
		
if __name__ == "__main__":
	l = converterCsvRendimentoEscolar(sys.argv[1])
	print l
	
			
		