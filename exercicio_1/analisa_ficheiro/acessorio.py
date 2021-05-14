import os

def pede_nome(nome):
    texto = []
    

    filesize = os.path.exists(nome)

    if filesize == 0 : 
        return
        
    else:
        with open(nome, "r", encoding='utf-8') as f:
            texto = f.read()
            return texto





        
def gera_nome(nome):
    ficheiro = nome.split('.')[0]
    ficheiro = (ficheiro + '.json')
    with open(ficheiro, "w", encoding='utf-8') as f:
        return ficheiro
        
        

    

