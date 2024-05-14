# 14
def resolver_crime():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    respostas = []
    i = 0
    while i < len(perguntas)  :
        resposta = input(f'{perguntas[i]} ')
        if resposta == 'sim':
            resposta = 1
        else :
            resposta = 0
        respostas.append(resposta)
        i+=1
    nota = sum(respostas)
    if nota == 2 :
        print('Pessoa classificado como suspeita')
    elif nota == 3 or nota == 4:
        print('Pessoa Classificada como Cúmplice')
    elif nota == 5 :
        print('Pessoa classificada como Assassina')
    else :
        print('Inocente')

# 15
def valores():
    valores = []
    while True:
        n = float(input('Insira um valor: '))
        if n != -1:
            valores.append(n)
        else:
            break
    print(f'Foram inseridos {len(valores)} valores')
    print(valores)
    valores.reverse()
    menor_7 = []
    for valor in valores:
        if valor < 7 :
            menor_7.append(valor)
        print(valor)
    print(f'a soma dos valores inseridos é: {sum(valores)}')
    print(f'a média dos valores inseridos é: {sum(valores)/len(valores)}')
    print(f'A quantidade de valores abaixo de sete é: {len(menor_7)}')
    print('Programa encerrado')
valores()