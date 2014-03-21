#naive bayes classifier

import csv
import sys

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
	
	
class Treinador:
	def __init__(self, datum):
		self.datum = datum
		
	def calcProbCond(self, attrNome, attrValor, classeNome, classeValor):
		denominador = len([data for data in self.datum if data.__dict__[classeNome] == classeValor])
		numerador = len([data for data in self.datum if(data.__dict__[classeNome] == classeValor and data.__dict__[attrNome] == attrValor)])
		
		return numerador / float(denominador)
	

def converterCsvRendimentoEscolar(csvpath):
	rendimentosEscolares = []
	with open(csvpath, "rb") as csvfo:
		reader = csv.reader(csvfo, delimiter=",")
		reader.next() #escapa a linha de header
		rendimentosEscolares = [RendimentoEscolar(*row) for row in reader]
	return rendimentosEscolares
	
if __name__ == "__main__":
	l = converterCsvRendimentoEscolar(sys.argv[1])
	print l
	
			
		