# LIMPIEZA DE DATOS

# A continuación, se hará una limpieza del archivo .csv generado por el script *test.py*

# Librerías a utilizar:
# %%
import pandas as pd
import datetime
import re

# Se crea una variable por cada archivo .csv
enero = pd.read_csv('./files/enero.csv')
febrero = pd.read_csv('./files/febrero.csv')
marzo = pd.read_csv('./files/marzo.csv')
abril = pd.read_csv('./files/abril.csv')
mayo = pd.read_csv('./files/mayo.csv')
junio = pd.read_csv('./files/junio.csv')
julio = pd.read_csv('./files/julio.csv')
agosto = pd.read_csv('./files/agosto.csv')

# Crear arreglo de datos con cada mes 
data_mensual = [enero, febrero, marzo, abril, mayo, junio, julio, agosto]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto']

cont = 0
# %%
# Recorrer cada csv mensual
for mes in data_mensual:
  
    # Creamos copia de la data con las columnas importantes
    clean_mes = mes[['text', 'hashtags', 'timestamp', 'username']].copy()

    clean_tweets = []

    # Recorremos tweet por tweet
    for line in clean_mes['text']:
        # Quitar caracteres en hex
        line = line.replace(u'\xa0', u' ')
        # Convertir el texto a minúsculas
        line = str(line.lower())

        # Quitar menciones
        line = re.sub('@[^\s]+','', line)
        # Quitar Hastags
        line = re.sub('#[^\s]+', '', line)

        # Quitar control de texto
        regex = re.compile(r'[\n\r\t]')
        line = regex.sub(' ', line)

        # Quitar URLS
        line = re.sub(r'http\S+', '', line)
        line = re.sub(r'pic\S+', '', line)

        # Quitar espacios de más
        line = re.sub(' +', ' ', line)

        # Quitar el resto de expresiones regulares, excepto . ? ! y '
        line = re.sub(r"[^\w.?!\d'\s]", '', line)

        # # Quitar números
        line = re.sub(' \d+', ' ', line)
        # # Quitar espacios extra
        line = line.strip(' \t\n\r')
        # # Reemplazar ! y ? por puntos.
        line = line.replace('!','.').replace('?','.')
        # # Quitar multiples puntos por solo uno
        line = re.sub(r'\.+', ".", line)
        # # Finalmente, quitamos apostrofes
        line = line.replace("'", '')

        clean_tweets.append(line)

    # Reemplazar los tweets sucios por los limpios
    clean_mes['text'] = clean_tweets
    # Crear dataframe del mes
    df = pd.DataFrame(clean_mes)
    # Crear CSV con el nombre del mes
    csv_name = f'./files/clean_{meses[cont]}.csv'
    df.to_csv(csv_name, index=False)

    cont = cont + 1
