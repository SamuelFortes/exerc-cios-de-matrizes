# Função para ler a matriz quadrada fornecida pelo usuário
def ler_matriz(ordem):
    matriz = []  
    print(f"Digite os elementos da matriz {ordem}x{ordem}:")
    
    # Loop para capturar cada linha da matriz
    for i in range(ordem):
        # Coleta uma linha da matriz, converte os elementos para float, e separa-os por espaços
        linha = list(map(float, input(f"Linha {i+1}: ").split()))  
        matriz.append(linha) 
    return matriz

# Função para exibir a matriz de maneira organizada
def exibir_matriz(matriz):
    for linha in matriz:
        print(["{:.0f}".format(elem) for elem in linha])

# Função para escalonar a matriz usando o método de eliminação gaussiana
def escalonar_matriz(matriz, ordem):
    # Percorre a diagonal principal
    for i in range(ordem):
        # Verifica se o elemento da diagonal é zero. Se for, troca de linha com outra linha abaixo
        if matriz[i][i] == 0:
            # Percorre as linhas abaixo da atual
            for j in range(i + 1, ordem):
                if matriz[j][i] != 0:  # Encontra uma linha onde o elemento da coluna não é zero
                    # Troca a linha atual com uma linha abaixo que tenha elemento não zero
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break

        # Elimina os elementos abaixo da diagonal principal
        for j in range(i + 1, ordem):
            # Calcula o fator multiplicador para zerar o elemento na coluna i da linha j
            fator = matriz[j][i] / matriz[i][i]
            # Para cada elemento na linha, aplica a subtração para fazer o escalonamento
            for k in range(ordem):
                matriz[j][k] -= fator * matriz[i][k]  # Subtrai o múltiplo da linha i da linha j


def main():
    ordem = int(input("Digite a ordem da matriz quadrada: "))
    
    matriz = ler_matriz(ordem)
    
    print("Matriz original:")
    exibir_matriz(matriz)

    escalonar_matriz(matriz, ordem)
    
    print("\nMatriz escalonada:")
    exibir_matriz(matriz)

main()
