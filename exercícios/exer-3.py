# Função para criar uma matriz identidade de tamanho n
def matriz_identidade(n):
    identidade = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        identidade[i][i] = 1
    return identidade

# Função para ler a matriz quadrada do usuário
def ler_matriz(ordem):
    matriz = []
    print(f"Digite os elementos da matriz {ordem}x{ordem}:")
    for i in range(ordem):
        linha = list(map(float, input(f"Linha {i+1}: ").split()))
        matriz.append(linha)
    return matriz

# Função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(["{:.2f}".format(elem) for elem in linha])

def calcular_inversa(matriz, n):
    # Criando uma matriz identidade do mesmo tamanho
    identidade = matriz_identidade(n)
    
    for i in range(n):
        # Verifica se o elemento da diagonal é zero, e faz troca de linhas se necessário
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    identidade[i], identidade[j] = identidade[j], identidade[i]
                    break

        # Normaliza a linha, dividindo todos os elementos pelo elemento da diagonal
        diagonal_element = matriz[i][i]
        for j in range(n):
            matriz[i][j] /= diagonal_element
            identidade[i][j] /= diagonal_element

        # Subtrai a linha atual das outras para zerar os elementos da coluna atual
        for j in range(n):
            if j != i:
                fator = matriz[j][i]
                for k in range(n):
                    matriz[j][k] -= fator * matriz[i][k]
                    identidade[j][k] -= fator * identidade[i][k]

    return identidade


def main():
    ordem = int(input("Digite a ordem da matriz quadrada: "))
    matriz = ler_matriz(ordem)
    
    # Verifica se a matriz tem inversa (determinante diferente de zero)
    try:
        inversa = calcular_inversa(matriz, ordem)
        print("A inversa da matriz é:")
        exibir_matriz(inversa)
    except ZeroDivisionError:
        print("A matriz não é invertível (determinante zero).")

main()
