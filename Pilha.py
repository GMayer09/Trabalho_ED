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
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.') 
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.') 
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    
    linhas_do_arquivo = lerArquivo(nome_arquivo) 
    
    dados_brutos = ""
    for linha in linhas_do_arquivo:
        dados_brutos += linha
    
    dados_formatados = remover_espacos_e_newlines(dados_brutos)
    
    tokens = dividir_por_delimitador(dados_formatados, '.')

    if not tokens:
        print("O arquivo está vazio ou não contém tokens válidos.")
        return

    try:
        resultado = notacaoPolonesa(tokens)
        print(f"Resultado final da expressão: {resultado}")
    except Exception as e:
        print(f"\nErro durante o cálculo da expressão: {e}")

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
    
    for char in s:
        if char == delimitador:
            if current_token:
                tokens.append(current_token)
            current_token = ""
        else:
            current_token += char
    
    if current_token:
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

        match token:
            case t if t.ehNumero():
                pilha.Empilhar(int(t))
            case '+':
                pilha.Empilhar(pilha.Desempilhar() + pilha.Desempilhar())
            case '-':
                pilha.Empilhar(pilha.Desempilhar() - pilha.Desempilhar())
            case '*':
                pilha.Empilhar(pilha.Desempilhar() * pilha.Desempilhar())
            case '/':
                pilha.Empilhar(pilha.Desempilhar() / pilha.Desempilhar())
            case _:
                print(f"Token inválido: {token}")
    try:
        resultado_final = pilha.MostrarTopo()
        pilha.Desempilhar()
        if not pilha.PilhaVazia():
            print("AVISO: A pilha final tem mais de um elemento. Expressão incompleta.")
        return resultado_final
    except (ValueError, IndexError):
        return "Erro: Expressão não resultou em valor final."

    
if __name__ == "__main__":
    main()