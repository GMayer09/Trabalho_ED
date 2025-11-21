from sys import argv
import sys

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

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.') 
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.') 
        sys.exit(1)

    pilha = Pilha()
    opcao: str = ""
    try:
        print("Iniciando programa!")
        while opcao != "s":
            print("\n--- Menu ---")
            print("e - Empilhar")
            print("d - Desempilhar")
            print("m - Mostrar topo")
            print("s - Sair")
            opcao = input("Escolha uma opção: ").lower()
            match opcao:
                case "e":
                    valor = int(input("Digite o valor a ser empilhado: "))
                    pilha.Empilhar(valor)
                case "d":
                    pilha.Desempilhar()
                case "m":
                    pilha.MostrarTopo()
                case "s":
                    break
    except ValueError as e:
        print("\nErro de valor: {e}")
    except Exception as e:
        print("\nErro inesperado: {e}")
    finally:
        print("Programa finalizado!")

def lerArquivo(nome: str) -> str:
    try:
        with open(nome) as arquivo:
            return arquivo.readlines()
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)
    
if __name__ == "__main__":
    main()