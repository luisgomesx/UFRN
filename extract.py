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
print(len(temp))

print(len(temp))

def remove_repetidos(lista):
    l = ['annot', 'he', 'ine', 'ain.cpp.51.']
    for i in lista:
        if i in l:
            lista.remove(i)
    return lista

temp2 = remove_repetidos(temp)

print(temp2)
print(len(temp2))

'''
tempo em milisegundos de um dia 86400000
GERANDO ERRO ABAIXO!!!!!!!!!!!
tempos com ('he', 'ine', 'annot') dentro dos dados
'''

tempos = list()
for i in temp:
    x = datetime.strptime(i, '%d.%b.%Y.%H.%M.%S')
    print(x)
    #tempos.extend(i)

#print(tempos)
    #x = x.timestamp()*1000
    #tempos.extend(x)

#tempos_milisegundos = tempos.timestamp()*1000

#print(tempos)


'''
test = datetime.strptime('29.Nov.2017.00.00.00', '%d.%b.%Y.%H.%M.%S')
milisec = test.timestamp()*1000
print(milisec)

test2 = datetime.strptime('30.Nov.2017.00.00.00', '%d.%b.%Y.%H.%M.%S')
milisec2 = test2.timestamp()*1000
print(milisec2)

print(milisec2 - milisec)
'''