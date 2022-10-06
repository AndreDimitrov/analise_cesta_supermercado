# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 23:20:45 2022

@author: andre
"""

import pandas as pd

dados = pd.read_csv('mercado2.csv', header=None)
dados.head()

transacoes = []
for i in range(0,7501):
    transacoes.append([str(dados.values[i,j]) for j in range(0,20)])
    

from apyori import apriori
regras = apriori(transacoes, min_support=0.003, min_confidence=0.2, min_lift=3.0, min_lenght=2)

"""
Nesse caso, trata-se de uma base de dados de uma semana, dessa forma, para definirmos o support 
teremos que multiplicar a quantidade de um item vendido em um dia por 7 dias da semana:
    4 * 7 = 28

em seguida, dividir esse resultado pelo total de itens 7501:
    28 / 7501 = 0,003732

com esse resultado, podemos utilizar para support


outro detalhe é de nos atentarmos de não utilizar de uma confidence com o valor de 0.8, pois poderemos
gerar uma confiânça muito óbvia.
"""

resultados = list(regras)
resultados

resultados2 = [list(x) for x in resultados]
resultados2

resultadoFormatado = []
for j in range(0,20):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
resultadoFormatado