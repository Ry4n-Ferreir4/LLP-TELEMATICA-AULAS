def calcular_porcentagens(N, M, pais_maes, presentes):
    geracoes = [0] * N  # lista para contar quantos descendentes de cada geração estão presentes
    total_presentes = 0  # contador para o número total de descendentes presentes na festa

    # Contagem dos descendentes presentes
    for descendente in presentes:
        geracoes[descendente - 1] += 1
        total_presentes += 1

    porcentagens = [geracoes[i] * 100 / (2 ** i) for i in range(N)]  # cálculo das porcentagens por geração

    return porcentagens

# Leitura da entrada
N, M = map(int, input().split())
pais_maes = list(map(int, input().split()))
presentes = list(map(int, input().split()))

# Cálculo e impressão das porcentagens
porcentagens = calcular_porcentagens(N, M, pais_maes, presentes)
print(' '.join(['%.2f' % p for p in porcentagens]))
