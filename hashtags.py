# %%
import os
import operator
import pandas as pd
from ast import literal_eval
import matplotlib.pyplot as plt
from itertools import islice

# Se crea una variable por cada archivo .csv
enero = pd.read_csv('./files/clean_enero.csv')
febrero = pd.read_csv('./files/clean_febrero.csv')
marzo = pd.read_csv('./files/clean_marzo.csv')
abril = pd.read_csv('./files/clean_abril.csv')
mayo = pd.read_csv('./files/clean_mayo.csv')
junio = pd.read_csv('./files/clean_junio.csv')
julio = pd.read_csv('./files/clean_julio.csv')
agosto = pd.read_csv('./files/clean_agosto.csv')

data = [enero, febrero, marzo, abril, mayo, junio, julio, agosto]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto']
sum_hashtags = []
# %%
for mes in data:

    hashtag_dict = {}

    for array in mes['hashtags']:
        array = literal_eval(array)
        if array:
            for hashtag in array:
                hashtag = hashtag.lower()
                if hashtag in hashtag_dict: hashtag_dict[hashtag] += 1
                else: hashtag_dict[hashtag] = 1
    
    sorted_dict = dict(sorted(hashtag_dict.items(), key=operator.itemgetter(1),reverse=True))
    sum_hashtags.append(sorted_dict)

# %%
path = os.getcwd() + '/images'

try:
    os.mkdir(path)
except OSError:
    print ('Unable to create /images directory')
else:
    print ('Successfully created /images the directory')
    pass


# %%
cont = 0
for mes in sum_hashtags:

    sub_dict = {k: mes[k] for k in list(mes)[:10]}

    # plt.tight_layout()

    plt.figure(figsize=(10,10))
    plt.rcParams['xtick.labelsize'] = 'small'
    plt.bar(range(len(sub_dict)), list(sub_dict.values()), align='center')
    plt.xticks(range(len(sub_dict)), list(sub_dict.keys()), rotation=45)
    plt.ylabel('Cantidad de usos')
    plt.title(f'Hashtags más usados en {meses[cont]}')

    filename = 'hashtags_{}.png'.format(meses[cont])
    dirname = os.path.dirname(__file__)
    images_dir = os.path.join(dirname, 'images/')

    plt.savefig(images_dir + filename)

    cont += 1
