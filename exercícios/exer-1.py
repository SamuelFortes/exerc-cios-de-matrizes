from random import randint

ordem = int(input("Digite a ordem da sua matriz: "))
linhas = colunas = ordem

matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = randint(0, 50)

print("\nMatriz Normal:")
for linha in matriz:
    print(" ".join(f"{num:4}" for num in linha))

print("\nMatriz Triangular Superior:")
matriz_superior = [linha.copy() for linha in matriz]
for i in range(linhas):
    for j in range(colunas):
        if matriz_superior[i][j] != 0 and i > j:
            matriz_superior[i][j] = 0

for linha in matriz_superior:
    print(" ".join(f"{num:4}" for num in linha))

print("\nMatriz Triangular Inferior:")
matriz_inferior = [linha.copy() for linha in matriz]
for i in range(linhas):
    for j in range(colunas):
        if matriz_inferior[i][j] != 0 and j > i:
            matriz_inferior[i][j] = 0

for linha in matriz_inferior:
    print(" ".join(f"{num:4}" for num in linha))
