import sys
naiveBayesPath = sys.argv[1]
csvpathTreino = sys.argv[2]
csvpathClassifica = sys.argv[3]
resultadoPath = sys.argv[4]

sys.path.append(naiveBayesPath)
from rendimentoEscolar import *

classificador = criaTreinadorParaRendimentoEscolar(csvpathTreino).treina()
rendimEscolaresClassificar = converterCsvParaRendimentosEscolares(csvpathClassifica)

for rendimEscolar in rendimEscolaresClassificar:
	data = rendimEscolar.__dict__
	del data["regiao"]
	classe = classificador.classifica(data)
	rendimEscolar.regiao = classe

redimentosEscolaresParaCsv(rendimEscolaresClassificar, resultadoPath)