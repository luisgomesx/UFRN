'''
sobre tempo em python
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
import pandas as pd
from datetime import datetime

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
#print(dados_requisicao_data_hora_tratado)

#substituição dos ":" e "/" por "."
tempo = [w.replace(':', '.').replace('/', '.') for w in dados_requisicao_data_hora_tratado]
#print(tempo)
#print(len(tempo))

#remoção de itens da lista que não fazem refência a tempo
tempo_format = list()
for i in tempo:
    try:
        x = datetime.strptime(i, '%d.%b.%Y.%H.%M.%S')
        #print(tempo)
    except:
        tempo.remove(i)
        tempo_format.append(x)
#print(tempo_format)
#print(len(tempo_format))

#convertendo em milisegundos para poder realizar algum procedimento matemático
milisegundos = list()
for i in tempo_format:
    milisegundos.append(i.timestamp())

#organizando
milisegundos.sort()
#print(milisegundos)
#print(len(milisegundos))

#de 0_29 e 30_59

referencia = milisegundos[:30]
#print(referencia)
#print(len(referencia))
a_ser_comparado = milisegundos[30:60]
#print(a_ser_comparado)
#print(len(a_ser_comparado))

'''
test = datetime.strptime('29.Nov.2017.00.00.00', '%d.%b.%Y.%H.%M.%S')
milisec = test.timestamp()*1000
print(milisec)

test2 = datetime.strptime('30.Nov.2017.00.00.00', '%d.%b.%Y.%H.%M.%S')
milisec2 = test2.timestamp()*1000
print(milisec2)

print(milisec2 - milisec)

tempo em milisegundos de um dia 86400000
'''