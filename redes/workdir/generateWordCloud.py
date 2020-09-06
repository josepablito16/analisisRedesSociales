#import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generateWordCloud(texts):    
    comment_words = ''
    stopwords = ['a', 'aca', 'ahi', 'ajena', 'ajeno', 'ajenas','ajenos', 'al', 'algo', 'alguna', 'alguno', 'algunos', 'algunas', 'alla' , 'alli', 'ambos', 'ante', 'antes', 'aquel', 'aquella', 'aquello','aquellas','aquellos',    
    'aqui', 'arriba', 'asi', 'atras', 'aun', 'aunque', 'bajo', 'bastante', 'bien', 'cabe', 'cada', 'casi', 'cierta', 'cierto', 'ciertas'
    'ciertos', 'como', 'con', 'conmigo', 'conseguimos', 'conseguir', 'consigo', 'consigue', 'consiguen', 'consigues', 'contigo', 'contra', 
    'cual', 'cuales', 'cualquier', 'cualquiera', 'cualquieras', 'cuan', 'cuando', 'cuanto', 'cuantos', 'cuantas', 'cuanta', 'de', 'dejar', 
    'del', 'demas', 'demasiada', 'demasiadas', 'demasiados', 'demasiado' , 'dentro', 'desde', 'donde', 
    'dos', 'el', 'el', 'ella', 'ellas', 'ellos', 'ello', 'empleais', 'emplean', 'emplear', 'empleas', 'empleo', 'en', 'encima', 'entonces', 'entre', 
    'era', 'eras', 'eramos', 'eran', 'eres', 'es', 'esa', 'ese', 'eso', 'esas', 'esos', 'estas', 'esta','estaba', 'estado', 'estais'
    , 'estamos', 'estan', 'estar', 'twitter', 'google','chrome',
    'este', 'estos', 'esto', 'estoy', 'etc', 'fin', 'fue', 'fueron', 'fui', 'fuimos', 'gueno', 'ha', 'hace', 'haces', 'haceis', 'hacemos', 'hacen', 
    'hacer', 'hacia', 'hago', 'hasta', 'incluso', 'intenta', 'intentas', 'intentais', 'intentamos', 'intentan', 'intentar', 'intento', 'ir', 
    'jamas', 'juntos', 'junto','lo', 'la', 'los','las' 'largo', 'mas', 'me', 'menos', 'mi','mis', 'mia', 'mias', 'mientras', 'mio', 'mios',
    'misma','mismo','mismas','mismos', 'modo', 'mucha', 'muchas', 
    'muchisima', 'muchisimos', 'muchisimo', 'muchisimos', 'mucho','muchos', 'muy', 'nada', 'ni', 
    'ninguna','ninguno','ningunas','ningunos', 'no', 'nos', 'nosotros','nosotras', 'nuestra','nuestros','nuestro','nuestras', 'nunca', 'os', 'otro', 'otra', 'otros', 'otras', 
    'para', 'parecer', 'pero', 'poco','poca','pocos','pocas', 'podeis', 'podemos', 'poder', 'podria','podrias', 'podriais', 'podriamos', 'podrian', 'por', 'por que', 
    'porque', 'primero', 'puede', 'pueden', 'puedo', 'pues', 'que', 'que', 'querer', 'quien','quienes', 'quienesquiera', 'quienquiera', 'quiza', 'quizas', 
    'sabe','sabes','saben', 'sabeis', 'sabemos', 'saber', 'se', 'segun', 'ser', 'si', 'si', 'siempre', 'siendo', 'sin', 'sino', 'so', 'sobre', 
    'sois', 'solamente', 'solo', 'solo', 'somos', 'soy', 'sr', 'sra', 'sres', 'sta', 
    'su','sus', 'suya','suyo','suyos','suyas', 'tales','tal', 'tambien', 'tampoco', 
    'tan', 'tanta','tanto','tantas', 'tantos','tanta', 'tantos', 'tantas', 'tanto', 'te', 'teneis', 'tenemos', 'tener', 'tengo', 'ti', 'tiempo', 'tiene', 'tienen', 
    'toda','todo','todas','todos', 'tomar', 'trabaja', 'trabajo', 
    'trabajais', 'trabajamos', 'trabajan', 'trabajar', 'trabajas', 'tras', 'tu', 'tu', 'tus', 'tuya','tuyo','tuyas','tuyos', 'ultimo', 'ultimo', 'un','una','unos','uno','unas', 
    'usa', 'usas','usais', 'usamos', 'usan', 'usar', 'uso', 'usted','ustedes', 'van','va', 'vais', 'valor', 'vamos', 'varias','varios', 'vaya', 'verdadera', 
    'vosotras','vosotros', 'voy', 'vuestra', 'vuestro', 'vuestras', 'vuestros', 'y', 'ya', 'yo']
    for text in texts:
        tokens = text.split() 
        comment_words += " ".join(tokens)+" "

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words)

    return wordcloud

""" add to generate graph
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show() 
"""