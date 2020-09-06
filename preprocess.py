# LIMPIEZA DE DATOS

# A continuación, se hará una limpieza del archivo .csv generado por el script *test.py*

# Librerías a utilizar:
import pandas as pd
import datetime
import re

# Se crea una variable por cada archivo .csv
enero = pd.read_csv('./enero.csv')
febrero = pd.read_csv('./febrero.csv')
marzo = pd.read_csv('./marzo.csv')
abril = pd.read_csv('./abril.csv')
mayo = pd.read_csv('./mayo.csv')
junio = pd.read_csv('./junio.csv')
julio = pd.read_csv('./julio.csv')
agosto = pd.read_csv('./agosto.csv')

# Crear variable con toda la data junta
data = pd.concat([enero, febrero, marzo, abril, mayo, junio, julio, agosto])

# Crear copia del documento, usando solo las columnas útiles
clean_df = data[['text', 'hashtags', 'timestamp', 'username']].copy()


# LIMPIEZA DE CADA TEXTO EN LOS TWEETS

# Creamos arreglo de tweets
clean_tweets = []

# Recorremos cada tweet individualmente
for line in clean_df['text']:
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

# CREAR CSV CON TWEETS LIMPIOS
# Primero, se cambian las columnas por aquellas que esten limpias.
clean_df['text'] = clean_tweets

# Luego, crear CSV limpio
df = pd.DataFrame(clean_df)
df.to_csv('./files/CleanData.csv', index=False)
