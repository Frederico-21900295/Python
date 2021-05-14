
def main():
    class Automovel:  #defenicao da classe
        def __init__(self,cap_dep,quant_comb,consumo):
            self.cap_dep = cap_dep
            self.quant_comb = quant_comb
            self.consumo = consumo

        def combustivel(self):
            return print(self.quant_comb)

        def autonomia(self):
            return print(int((self.quant_comb * 100)/ self.consumo ))

        def abastece(self,tonomia):
            self.tonomia = tonomia
            if self.quant_comb > self.cap_dep:
                print("Erro")
            else:
                self.tonomia +=  self.quant_comb
                self.tonomia = ((self.tonomia * 100)/ self.consumo)
                print(int(self.tonomia))

        def percorre(self,distancia):
            self.distancia = distancia
            if self.distancia > self.tonomia:
                print("Erro")

            else:
                self.tonomia -= self.distancia
                print(int(self.tonomia))

