import sys
sys.path.append(r"C:\Users\Joao&Duda\Desktop\JP\2014-1\datamining\NaiveBayesClass\naivebayesrepo")
from rendimentoEscolar import *

csvpath = r"C:\Users\Joao&Duda\Desktop\JP\2014-1\datamining\NaiveBayesClass\naivebayesrepo\2007(treinamento).csv"
t = criaTreinadorParaRendimentoEscolar(csvpath)
c = t.treina()
for p in c.probsConds:
	print "dada a classe " + p.classeValor
	print "as probs condicionais do atributo " + p.atribNome + " sao"
	print p.probsConds
	s = 0.0
	for k in p.probsConds.keys():
		s += p.probsConds[k]
	print "soma = " + str(s)

print c.getProbCond("nonoAno", "C", "centroOeste")

v = dict(zip(['localizacao','rede','primeiroAno','segundoAno','terceiroAno','quartoAno','quintoAno','sextoAno','setimoAno','oitavoAno','nonoAno'], ['rural','Estadual','B','D','C','C','B','B','B','B','A']))
prob = c.calcProbCondClasseDadoAtributos("norte", v)

print prob

r = c.classifica(v)
print r