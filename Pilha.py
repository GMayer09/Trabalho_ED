class Pilha:
    def __init__(self):
        self.topo = -1
        self.TamMax = 50

    def PilhaVazia(self) -> bool:
        if self.topo == -1:
            return True
        
    def PilhaCheia(self) -> bool:
        if self.topo == self.TamMax:
            return True
    
    def Empilhar(self, valor):
        if not self.PilhaCheia():
            self.topo += 1
            self.Pilha[self.topo] = valor
        else:
            print("Pilha cheia")
    
    def Desempilhar(self):
        if not self.PilhaVazia():
            self.topo -= 1
        else:
            print("Pilha vazia")
    
    def MostrarTopo(self):
        if not self.PilhaVazia():
            print(self.Pilha[self.topo])
        else:
            raise ValueError("Pilha vazia")
    