import csv
import sys
from naiveBayes import *

NOME_CLASSE_RENDIMENTO_ESCOLAR = "regiao"
VALORES_CLASSE_RENDIMENTO_ESCOLAR = ["norte", "nordeste", "sudeste", "sul", "centroOeste"]

VALORES_ATTR_ANO = ["A", "B", "C", "D", "E"]

def converterCsvParaRendimentosEscolares(csvpath):
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
	datum = converterCsvParaRendimentosEscolares(csvpath)
	return Treinador(datum, classe, atribs)
	
def redimentosEscolaresParaCsv(rendimentosEscolares, csvpath):
	with open(csvpath, "wb") as csvfo:
		writer = csv.writer(csvfo, delimiter=";")
		writer.writerow(["regiao", "localizacao", "rede", "primeiroAno", "segundoAno", "terceiroAno",
						 "quartoAno", "quintoAno", "sextoAno", "setimoAno", "oitavoAno", "nonoAno"])
		for rendimentoEscolar in rendimentosEscolares:
			writer.writerow([rendimentoEscolar.regiao, rendimentoEscolar.localizacao, rendimentoEscolar.rede, rendimentoEscolar.primeiroAno,
							 rendimentoEscolar.segundoAno, rendimentoEscolar.terceiroAno, rendimentoEscolar.quartoAno,
							 rendimentoEscolar.quintoAno, rendimentoEscolar.sextoAno, rendimentoEscolar.setimoAno,
							 rendimentoEscolar.oitavoAno, rendimentoEscolar.nonoAno])

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

if __name__ == "__main__":
	l = converterCsvRendimentoEscolar(sys.argv[1])
	print l