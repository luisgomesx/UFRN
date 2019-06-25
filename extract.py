'''
sobre tempo em python
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
import pandas as pd

#importação do dataset
dataset = pd.read_csv('dataset/weblog.csv')
#separando os dados das colunas, index e valores
colunas = dataset.columns
index = dataset.index
dados = dataset.values
#capturando apena o que tá na coluna 'Time'
requisicao_data_hora = dataset['Time']

#print(dataset.head())
#print(colunas)
#print(index)
#print(dados)
#print(requisicao_data_hora)

#capturando apenas os dados da coluna time
dados_requisicao_data_hora = requisicao_data_hora.values

#print(dados_requisicao_data_hora)
#print(len(dados_requisicao_data_hora))

'''Tratamento dos dados da coluna'''
#Removendo o '[' que veio no dataset
dados_requisicao_data_hora_tratado = [ i[1:] for i in dados_requisicao_data_hora ]
print(dados_requisicao_data_hora_tratado)

#convertendo em milisegundos para poder realizar algum procedimento matemático
from datetime import datetime

temp = [w.replace(':', '.').replace('/', '.') for w in dados_requisicao_data_hora_tratado]
print(temp)

'''GERANDO ERRO !!!!!!!!!!!'''
tempo_milisegundos = []
for i in temp:
    tempo_milisegundos += datetime.strptime(i, '%d.%b.%Y.%H.%M.%S')

print(tempo_milisegundos)
