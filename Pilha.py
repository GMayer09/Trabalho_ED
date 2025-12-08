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
            return valor_removido
        else:
            print("Pilha vazia")
    
    def MostrarTopo(self):
        if not self.PilhaVazia():
            return self.elementos[self.topo]
        else:
            raise ValueError("Pilha vazia")

def main():
    if len(sys.argv) != 2:
        print("Uso: python Pilha.py arquivo.txt")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    linhas = lerArquivo(nome_arquivo)

    i = 0
    while i < len(linhas):
        linha = linhas[i]
        linha_limpa = remover_espacos_e_newlines(linha)

        if linha_limpa != "":
            tokens = dividir_por_delimitador(linha_limpa, '.')
            try:
                resultado = notacaoPolonesa(tokens)
                print("Resultado da linha", i + 1, ":", resultado)
            except Exception as e:
                print("Erro na linha", i + 1, ":", e)

        i += 1


def remover_espacos_e_newlines(s: str) -> str:
    inicio = 0
    fim = len(s)
    
    while inicio < fim and (s[inicio] == ' ' or s[inicio] == '\n' or s[inicio] == '\r'):
        inicio += 1
    
    while fim > inicio and (s[fim - 1] == ' ' or s[fim - 1] == '\n' or s[fim - 1] == '\r'):
        fim -= 1
        
    return s[inicio:fim]

def dividir_por_delimitador(s: str, delimitador: str) -> list[str]:
    tokens = []
    current_token = ""

    i = 0
    while i < len(s):
        char = s[i]

        if char == delimitador:
            if current_token != "":
                tokens.append(current_token)
                current_token = ""
            i += 1
            continue

        # Se o caractere atual é dígito E o token atual é operador,
        # comece um novo token automaticamente
        if char.isdigit() and (current_token in ["+", "-", "*", "/"]):
            tokens.append(current_token)
            current_token = ""

        current_token += char
        i += 1

    if current_token != "":
        tokens.append(current_token)

    return tokens

def lerArquivo(nome: str) -> str:
    try:
        with open(nome) as arquivo:
            return arquivo.readlines()
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

def ehNumero(s: str) -> bool:
    if s == "":
        return False
    
    if s[0] == "-":
        if len(s) == 1:
            return False
        s = s[1:]
    
    for c in s:
        if c < '0' or c > '9':
            return False
    
    return True


def notacaoPolonesa(tokens: list[str]):
    pilha = Pilha()
    for token in tokens:
        token_limpo = remover_espacos_e_newlines(token)

        match token_limpo:
            case t if ehNumero(t):
                pilha.Empilhar(int(t))
            case '+':
                pilha.Empilhar(pilha.Desempilhar() + pilha.Desempilhar())
            case '-':
                b = pilha.Desempilhar()
                a = pilha.Desempilhar()
                pilha.Empilhar(a - b)
            case '*':
                pilha.Empilhar(pilha.Desempilhar() * pilha.Desempilhar())
            case '/':
                b = pilha.Desempilhar()
                a = pilha.Desempilhar()
                pilha.Empilhar(a / b)
            case _:
                print(f"Token inválido: {token_limpo}")

    if pilha.PilhaVazia():
        raise ValueError("Expressão vazia ou não resultou em valor final.")

    resultado_final = pilha.MostrarTopo()
    pilha.Desempilhar()

    if not pilha.PilhaVazia():
        sobrando = pilha.topo + 1
        raise ValueError("Expressão incompleta: sobraram {} valor(es) na pilha.".format(sobrando))

    return resultado_final

    
if __name__ == "__main__":
    main()