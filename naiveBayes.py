#naive bayes classifier

import csv
import sys

NOME_CLASSE_RENDIMENTO_ESCOLAR = "regiao"
VALORES_CLASSE_RENDIMENTO_ESCOLAR = ["norte", "nordeste", "sudeste", "sul", "centroOeste"]

VALORES_ATTR_ANO = ["A", "B", "C", "D", "E"]

def converterCsvParaRendimentoEscolar(csvpath):
	rendimentosEscolares = []
	with open(csvpath, "rb") as csvfo:
		reader = csv.reader(csvfo, delimiter=",")
		reader.next() #escapa a linha de header
		rendimentosEscolares = [RendimentoEscolar(*row) for row in reader]
	return rendimentosEscolares

def criaTreinadorParaRendimentoEscolar(csvpath):
	classe = Atributo(attrNome=NOME_CLASSE, valores=VALORES_CLASSE_RENDIMENTO_ESCOLAR)
	atribs = [Atributo("localizacao", ["urbana", "rural"]), Atributo("rede", ["Estadual", "Federal", "Municipal", "Particular"]),
			  Atributo("1Ano", VALORES_ATTR_ANO), Atributo("2Ano", VALORES_ATTR_ANO), 
			  Atributo("3Ano",VALORES_ATTR_ANO), Atributo("4Ano",VALORES_ATTR_ANO),
			  Atributo("5Ano",VALORES_ATTR_ANO), Atributo("6Ano",VALORES_ATTR_ANO),
			  Atributo("7Ano",VALORES_ATTR_ANO), Atributo("8Ano",VALORES_ATTR_ANO),
			  Atributo("9Ano",VALORES_ATTR_ANO)]
	datum = converterCsvRendimentoEscolar(csvpath)
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
	def __init__(self, attrNome, valores):
		#nome do atributo classe
		self.attrNome = attrNome
		#lista de valore que  podem ser assumidos pelo atributo classe
		self.valores = valores
		
class Treinador:
	def __init__(self, datum, classe, atribs):
		#lista de objetos de uma classe que representa um dado tipo RendimentoEscolar
		self.datum = datum
		#objeto da classe Atributo
		self.classe = classe
		#lista objetos da classe Atributo
		self.atribs = atribs
		
	def calcProbCond(self, attrNome, attrValor, classeNome, classeValor):
		denominador = len([data for data in self.datum if data.__dict__[classeNome] == classeValor])
		numerador = len([data for data in self.datum if(data.__dict__[classeNome] == classeValor and data.__dict__[attrNome] == attrValor)])
		
		return numerador / float(denominador)
	
	def calcProbClassePriori(self, classeNome):
		denominador = len(self.datum)
		numerador = len([data for data in datum if data.__dict__[self.classe.attrNome] == classeNome])
		return numerador / float(denominador)

	'''dado um valor de uma classe e um nome de atributo,
		devo calcular as probCond de tds os valores desse atributo
		dado o valor da classe'''
	
if __name__ == "__main__":
	l = converterCsvRendimentoEscolar(sys.argv[1])
	print l
	
			
		