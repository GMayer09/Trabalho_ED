class Pilha:
    def __init__(self):
        self.topo = -1
        self.TamMax = 50
        self.elementos = [0] * self.TamMax
    

    def PilhaVazia(self):
        return self.topo == -1
        
    def PilhaCheia(self):
        return self.topo == self.TamMax - 1
    
    def Empilhar(self, valor):
        if not self.PilhaCheia():
            self.topo += 1
            self.elementos[self.topo] = valor
        else:
            print("Pilha cheia")
    
    def Desempilhar(self):
        if not self.PilhaVazia():
            valor_removido = self.elementos[self.topo]
            self.elementos[self.topo] = None
            self.topo -= 1
        else:
            print("Pilha vazia")
    
    def MostrarTopo(self):
        if not self.PilhaVazia():
            print(self.elementos[self.topo])
        else:
            raise ValueError("Pilha vazia")

if __name__ == "__main__":
    pilha = Pilha()
    pilha.Empilhar(1)
    pilha.MostrarTopo()
    pilha.Empilhar(2)
    pilha.MostrarTopo()
    pilha.Empilhar(3)
    pilha.MostrarTopo()
    pilha.Desempilhar()
    pilha.MostrarTopo()
    pilha.Desempilhar()
    pilha.MostrarTopo()
    pilha.Desempilhar()
    pilha.MostrarTopo()
    pilha.Desempilhar()
    pilha.MostrarTopo()