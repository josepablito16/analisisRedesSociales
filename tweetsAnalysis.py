import datetime
from matplotlib import pyplot as plt
import pandas as pd
from googletrans import Translator
from PerWordAnalisys import perWordAnalisys
translator = Translator()


files = [
    'files\clean_abril.csv',
    'files\clean_agosto.csv',
    'files\clean_enero.csv',
    'files\clean_febrero.csv',
    'files\clean_julio.csv',
    'files\clean_junio.csv',
    'files\clean_marzo.csv',
    'files\clean_mayo.csv'
]
fechas = []
punteos = []
for file in files:
    data = pd.read_csv(file)
    for index in range(len(data['text'])):
        print(data['timestamp'][index])
        texto = data['text'][index]
        fechas.append(data['timestamp'][index]
                      [:data['timestamp'][index].find(" ")])
        punteos.append(perWordAnalisys(
            translator.translate(texto, dest='en').text))

datos = {
    'Fechas': fechas,
    'Punteos': punteos
}
series = pd.DataFrame(datos, columns=['Fechas', 'Punteos'])
series.to_csv('files/timeSerie.csv')

dataPorDia = {}
dataAnalizada = pd.read_csv('files/timeSerie.csv')
for i in range(len(dataAnalizada)):
    try:
        dataPorDia[dataAnalizada['Fechas'][i]] += dataAnalizada['Punteos'][i]
    except:
        dataPorDia[dataAnalizada['Fechas'][i]] = dataAnalizada['Punteos'][i]

punteoPorMeses = [0, 0, 0, 0, 0, 0, 0, 0]
for keys in list(dataPorDia.keys()):
    mes = keys[keys.find('-')+1:]
    mes = mes[:mes.find('-')]
    punteoPorMeses[int(mes)-1] += dataPorDia[keys]

meses = ['Enero', 'Febrero', 'Marzo', 'Abril',
         'Mayo', 'Junio', 'Julio', 'Agosto']

mesesPositivos = [0, 0, 0, 0, 0, 0, 0, 0]
mesesNegativos = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(punteoPorMeses)):
    if(punteoPorMeses[i] > 0):
        mesesPositivos[i] = punteoPorMeses[i]
    else:
        mesesNegativos[i] = punteoPorMeses[i]

fig, ax = plt.subplots()
plt.title('Sentimientos predominantes por mes')
plt.xlabel('Meses')
plt.ylabel('Puntos de sentimientos')
ax.bar(meses, mesesPositivos, color='g')
ax.bar(meses, mesesNegativos, color='r')
plt.show()
