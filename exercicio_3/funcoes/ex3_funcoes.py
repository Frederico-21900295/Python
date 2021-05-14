import os
import re

def main():
    pede_pasta()


def pede_pasta():
    nome = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ")
    if os.path.isdir(nome) == True:
        print("Existe pasta") 
    else:
        print("Pasta nao existe")
        pede_pasta()
    faz_calculos(nome)
    return nome

def faz_calculos(nome):
    soma = 0
    valor = 0
    lista = os.listdir(nome)

    for elementos in lista:
        if os.path.isfile(os.path.join(nome,elementos)):
            valor = os.path.getsize(os.path.join(nome,elementos))
            soma += valor

        elif os.path.isdir(os.path.join(nome,elementos)):
            pedro = (os.path.join(nome,elementos))
            lista2 =os.listdir(pedro)

            for values in lista2:
                if os.path.isfile(os.path.join(pedro,values)):
                    print(os.path.join(pedro,values))

                    valor = os.path.getsize(os.path.join(pedro,values))
                    soma = soma +valor
                

    print(soma)
    