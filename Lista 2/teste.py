# Ler um número inteiro e calcular a soma de seus algarismos
n = int(input('Insira um número inteiro: '))
n = str(n)
i = 0
soma = 0
while len(n) + 1 > i :
    soma = soma + int(n[i]);
    i = i + 1
print (f'A soma dos algarismos é {soma}');