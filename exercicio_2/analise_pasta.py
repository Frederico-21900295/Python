import os
import csv
from matplotlib import pyplot as plt


def pede_pasta():
    nome = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ")
    if os.path.isdir(nome) == True:
        print("Existe pasta\n") 
    else:
        print("Pasta nao existe\n")
        return
    faz_calculos(nome)
    return nome


def faz_calculos(nome):
    dictio = {}
    lista = os.listdir(nome)
    
    
    for elemento in lista:
        if os.path.isfile(os.path.join(nome,elemento)):
            if elemento[elemento.find('.')+1:] not in dictio:
                dictio[elemento[elemento.find('.')+1:] ] = {"volume" : os.path.getsize(os.path.join(nome,elemento)) , "quantidades" : 1}
            else:
                dictio[elemento[elemento.find('.')+1:] ]["volume"] += os.path.getsize(os.path.join(nome,elemento))
                dictio[elemento[elemento.find('.')+1:] ]["quantidades"] += 1

    escrever_csv(dictio)
    faz_grafico_queijos(dictio)
    faz_grafico_barras(dictio)
    return


def escrever_csv(dictio):
    with open('resultados.csv', 'w', newline='') as ficheiro:
        campos = ['Extensao', 'Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for elemento in dictio.keys():
            ficheiro.write(f"{elemento},{dictio[elemento]['quantidades']},{dictio[elemento]['volume']   } \n")
    return
    

def faz_grafico_queijos(dictio):
    listachaves =[]
    listavalores =[]
    mycolors = ["black", "hotpink", "b", "#4CAF50"]

    for elemento,value in dictio.items():
        if elemento not in listachaves:
            listachaves.append(elemento)
            listavalores.append(value['quantidades'])
        else:
            continue
    
    plt.pie(listavalores, labels=listachaves, autopct='%1.0f%%', colors = mycolors)
    plt.title("Quantidades de extensoes")
    plt.show()
    
    return


def faz_grafico_barras(dictio):
    listachaves =[]
    listavalores =[]
    mycolors = ["black", "hotpink", "b", "#4CAF50"]

    for elemento,value in dictio.items():
        if elemento not in listachaves:
            listachaves.append(elemento)
            listavalores.append(value['quantidades'])
        else:
            continue
    
    plt.bar(listachaves, listavalores)
    plt.title("Quantidades de extensoes")
    plt.show()
    return






pede_pasta()




