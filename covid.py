#%%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##RIAN SOUSA FLORENTINO DAS CHAGAS,RAFAEL FRAZÃO BORGES DA SILVA
# JOAO VITOR FERREIRA DANTAS,SAMUEL LIMA DE ARAUJO##

uri = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv'

covid = pd.read_csv(uri)
covid.columns = ['País', 'Estado', 'Cidade', 'ibgeID', 'totalMortes', 'totalCasos','Morte_por_100Khab','Casos_por_100Khab','Morte_por_TotalCasos',
                '_fonte','data','novosCasos','novasMortes','dataUltimaInfo']

#print(covid.head())
        #0-País 1-Estado 2-Cidade 

tCasos = covid['totalCasos'].sum()
tMortes = covid['totalMortes'].sum()

mediaCasosEstado = tCasos / 27

print("===================")

print("Media de casos por estado: ", int(mediaCasosEstado))
print("Mediana de total de casos: ", np.median(covid['totalCasos']))
print("Estado com mais mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmax(),5]," - ", covid.iloc[covid['totalCasos'].idxmax(),1])
print("Estado com menos mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmin(),5]," - ", covid.iloc[covid['totalCasos'].idxmin(),1])
print("Desvio padrão de total de casos: ", np.std(covid['totalCasos']))
print("Media de mortes: ", np.mean(covid['totalMortes']))
print("Cidade com menos mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmin(),2])

estados5MaisMortes = covid.nlargest(5, 'totalMortes', keep='first')
#estados5MenosMortes = covid.nsmallest(5, 'totalMortes')

estados5MaisCasos = covid.nlargest(5, 'totalCasos', keep='first')



graph1 = plt.bar(estados5MaisMortes['Estado'], estados5MaisMortes['totalMortes'])
print("Estado com 5 mais mortes: ")
plt.show(graph1)
print("Estado com 5 mais casos: ")
graph2 = plt.bar(estados5MaisCasos['Estado'], estados5MaisCasos['totalCasos'])
plt.show(graph2)


# %%
