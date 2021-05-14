import analisa_ficheiro
import json
import pprint




if __name__ == "__main__":
    valores_ficheiro_novo = []
    n=0
    texto = ""
    valores_ficheiro_novo1 = {}


    #acessorio.py

    while n!=1:
        print("Qual o nome do ficheiro?")
        nome = input()
        texto = analisa_ficheiro.pede_nome(nome)

        if texto :
            n = 1
        else:
            n = 0
    print(nome)
    ficheiro_json= analisa_ficheiro.gera_nome(nome)

            
    #calculos.py
    valores_ficheiro_novo1 = analisa_ficheiro.calcula_linhas(texto, valores_ficheiro_novo1)
    valores_ficheiro_novo1 = analisa_ficheiro.calcula_caracteres(texto,valores_ficheiro_novo1)
    valores_ficheiro_novo1 = analisa_ficheiro.maior_palavra(texto,valores_ficheiro_novo1)

    

    valores_ficheiro_novo1 = analisa_ficheiro.calcula_ocorrencia_de_letras(texto,valores_ficheiro_novo1)


    #Escrever valores no ficheiro.json
    with open(ficheiro_json, "w", encoding='utf-8') as json_file:
        json.dump(valores_ficheiro_novo1,json_file,indent=4)
    