# Trabalho Estrutura de Dados - Franklin Cesar Flores
# Raul Alencar (145090) e Guilherme Mayer (140656)

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
            try:
                tokens = dividir_por_delimitador(linha_limpa, '.')
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

        if char.isdigit():
            current_token += char
            i += 1
            continue

        if char == '.':
            if current_token != "":
                tokens.append(current_token)
                current_token = ""
            i += 1
            continue

        if char in "+-*/":
            if current_token != "":
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
            i += 1
            continue

        raise ValueError(f"Caractere inválido: {char}")

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
    operadores = {"+", "-", "*", "/"}

    for token in tokens:
        token_limpo = remover_espacos_e_newlines(token)

        if ehNumero(token_limpo):
            pilha.Empilhar(int(token_limpo))
            continue

        if token_limpo in operadores:
            if pilha.topo < 1:
                raise ValueError("Erro: faltando operando na expressão.")

            b = pilha.Desempilhar()
            a = pilha.Desempilhar()

            match token_limpo:
                case '+':
                    pilha.Empilhar(a + b)
                case '-':
                    pilha.Empilhar(a - b)
                case '*':
                    pilha.Empilhar(a * b)
                case '/':
                    if b == 0:
                        raise ValueError("Divisão por zero.")
                    pilha.Empilhar(a // b)

            continue

        raise ValueError(f"Token inválido: {token_limpo}")

    if pilha.PilhaVazia():
        raise ValueError("Erro: expressão vazia ou inválida.")

    resultado_final = pilha.Desempilhar()

    if not pilha.PilhaVazia():
        raise ValueError("Erro: faltando operador na expressão.")

    return resultado_final

    
if __name__ == "__main__":
    main()