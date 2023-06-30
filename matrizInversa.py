def inverter_diagonais(matriz):
    tamanho = len(matriz)
    for i in range(tamanho):
        matriz[i][i], matriz[i][tamanho - 1 - i] = (
            matriz[i][tamanho - 1 - i],
            matriz[i][i],
        )


# Teste
# matriz = [[1, 0], [0, 1]]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matriz = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print("Matriz original:")
for linha in matriz:
    print(*linha)
print("Matriz com as diagonais invertidas:")
inverter_diagonais(matriz)
for linha in matriz:
    print(*linha)
