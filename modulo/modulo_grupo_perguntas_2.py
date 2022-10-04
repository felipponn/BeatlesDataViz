import pandas as pd
import collections

# Quais são as palavras mais comuns nos títulos dos álbuns?

def palavras_comuns_albuns(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            albuns = dataframe.index.get_level_values(1) # Seleciona todos os albuns do dataframe
            lista_albuns = list(dict.fromkeys(albuns)) # Organiza-os em uma lista (cada album é uma string)
            lista_palavras = []
            for album in lista_albuns: # Transforma cada string de album em uma lista de palavras
                titulo = album.split()
                for palavra in titulo: # Adiciona cada palavra dos títulos dos albuns em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(3) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

# Quais são as palavras mais comuns nos títulos das músicas?

def palavras_comuns_musicas(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            musicas = dataframe.index.get_level_values(1) # Seleciona todos as músicas do dataframe
            lista_musicas = list(dict.fromkeys(musicas)) # Organiza as músicas em uma lista (cada música é uma string)
            lista_palavras = []
            for musica in lista_musicas: # Transforma cada string de música em uma lista de palavras
                titulo = musica.split()
                for palavra in titulo: # Adiciona cada palavra dos títulos das músicas em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(3) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

# Quais são as palavras mais comuns nas letras das músicas, por álbum?

def palavras_comuns_letras_albuns(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            letras = dataframe["lyrics"].groupby(["album"]) # Seleciona todas as letras das músicas, agrupadas por álbum
            lista_letras = list(dict.fromkeys(letras)) # Organiza as letras em uma lista (cada letra é uma string)
            lista_palavras = []
            for letra in lista_letras: # Transforma cada string de letra em uma lista de palavras
                palavras = letra.split()
                for palavra in palavras: # Adiciona cada palavra das letras das músicas em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(3) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

# Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?

def palavras_comuns_letras_disco(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            letras = dataframe["lyrics"] # Seleciona todas as letras das músicas de toda a discografia
            lista_letras = list(dict.fromkeys(letras)) # Organiza as letras em uma lista (cada letra é uma string)
            lista_palavras = []
            for letra in lista_letras: # Transforma cada string de letra em uma lista de palavras
                palavras = letra.split()
                for palavra in palavras: # Adiciona cada palavra das letras das músicas em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(3) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

# O título de um álbum é tema recorrente nas letras?

def titulo_album_letras(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            albuns = dataframe.index.get_level_values(1) # Seleciona todos os albuns do dataframe
            serie_albuns = pd.Series(albuns) # Cria uma série de álbuns 
            array_albuns = serie_albuns.unique() # Elimina as repetições de álbuns
            letras = dataframe["lyrics"] # Seleciona todas as letras do dataframe
            serie_letras = pd.Series(letras) # Cria uma série de letras 
            array_letras = serie_letras.unique() # Elimina as repetições de letras
            dicio_relacao = {}
            for album in array_albuns: # Verifica se os álbuns da série têm relação com as letras da série
                dicio_relacao[album] = 0
                for letra in array_letras:
                    relacionamento = letra.count(album)
                    dicio_relacao[album] += relacionamento # Adiciona a relação álbum/letra em um dicionário
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return dicio_relacao

###############################################################################

# O título de uma música é tema recorrente nas letras?

def titulo_musica_letras(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            musicas = dataframe.index.get_level_values(1) # Seleciona todos as músicas do dataframe
            serie_musicas = pd.Series(musicas) # Cria uma série de músicas
            array_musicas = serie_musicas.unique() # Elimina as repetições de músicas
            letras = dataframe["lyrics"] # Seleciona todas as letras do dataframe
            serie_letras = pd.Series(letras) # Cria uma série de letras
            array_letras = serie_letras.unique() # Elimina as repetições de letras
            dicio_relacao = {} 
            for musica in array_musicas: # Verifica se as músicas da série têm relação com as letras da série
                dicio_relacao[musica] = 0
                for letra in array_letras:
                    relacionamento = letra.count(musica)
                    dicio_relacao[musica] += relacionamento # Adiciona a relação música/letra em um dicionário
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return dicio_relacao