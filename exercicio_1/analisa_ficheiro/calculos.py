import re
import string


def calcula_linhas(texto,valores_ficheiro_novo1):
    numerodelinhas = len(texto.splitlines())
    valores_ficheiro_novo1.update({'Numero de linhas' : numerodelinhas})
    return valores_ficheiro_novo1

def calcula_caracteres(texto,valores_ficheiro_novo1):
    n = 0
    numerodelinhas =[]
    for caracters in texto:
        if caracters == '/n':
            n = n +1
        else:
            n = n +1
    
    valores_ficheiro_novo1.update({'Numero de caracteres' : n})
    return valores_ficheiro_novo1

def maior_palavra(texto,valores_ficheiro_novo1):

    palavras =[]
    spot = ""
    palavras =  re.findall(r"[\w']+", texto)
    
    for palavra in palavras:
        valor = len(palavra)
        valor1 = len(spot)

        if valor > valor1:
            spot = palavra
        else:
            continue
    
    valores_ficheiro_novo1.update({'A maior palavra no ficheiro .txt' : spot})
    return valores_ficheiro_novo1

def calcula_ocorrencia_de_letras(texto,valores_ficheiro_novo1):
    dict = {}
    texto = texto.lower()

    for letters in texto:
        keys = dict.keys()
        if letters in keys:
            dict[letters] += 1
        
        elif (letters == '\n' or letters == ' ' or letters == '!' or letters == ',' or letters == '.'  or letters == '?'):
            continue
        else:
            dict[letters] = 1

    valores_ficheiro_novo1.update({'A quantidade de vezes que cada letra ocorre' : [dict] })
    
    return valores_ficheiro_novo1
        




for elemento in tupple_lista:
        keys = dictio.keys()

        print(type(tupple_lista))
        
        if elemento in keys:
            keys[elemento] += 1

        else:
            keys[elemento] = 1

