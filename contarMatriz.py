def contar_submatriz(A, B):
    cont = 0
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])

    for i in range(linhas_A - linhas_B + 1):
        for j in range(colunas_A - colunas_B + 1):
            achou = True
            for k in range(linhas_B):
                for l in range(colunas_B):
                    if A[i + k][j + l] != B[k][l]:
                        achou = False
                        break
                if not achou:
                    break
            if achou:
                cont += 1

    return cont


# Teste
A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

B = [[3, 4], [4, 5]]

ocorrencias = contar_submatriz(A, B)
print(ocorrencias)
