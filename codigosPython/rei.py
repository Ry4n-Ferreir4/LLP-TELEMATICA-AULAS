def calcular_porcentagens(N, M, pais_maes, presentes):
    geracoes = [0] * N  
    total_presentes = 0  

    for descendente in presentes:
        geracoes[descendente - 1] += 1
        total_presentes += 1

    porcentagens = []

    for i in range(N):
        porcentagem = geracoes[i] * 100 / (2 ** i)  # 2 ^ i representa o número de descendentes daquela geração
        porcentagens.append(porcentagem)

    return porcentagens

N, M = map(int, input().split())
pais_maes = list(map(int, input().split()))
presentes = list(map(int, input().split()))

porcentagens = calcular_porcentagens(N, M, pais_maes, presentes)
print('%.2f' % porcentagens[0], end='')
for i in range(1, N):
    print(' %.2f' % porcentagens[i], end='')
print()
