def imprimir_numeros(quantidade):
    i = 1
    while i <= quantidade :
        print(i)
        i += 1
        
quantidade = int(input('Insira a quantidade de números: '))
imprimir_numeros(quantidade)

def imprimir_numeros2(inicio, fim):
    i = inicio
    while i <= fim :
        print(i)
        i += 1
        
inicio = int(input('Insira o número inicial: '))
fim = int(input('Insira o número final: '))
imprimir_numeros2(inicio, fim)

def contagem_regressiva(contagem, mensagem):
    i = contagem
    while i >= 0 :
        print(f'{i}...')
        i -= 1
    print(f'ღ(¯`◕‿◕´¯) ♫ ♪ ♫ {mensagem} ♫ ♪ ♫ (¯`◕‿◕´¯)ღ')
contagem = int(input('Insira o valor para sua contagem regressiva: '))
mensagem = input('Insira a mensagem para aparecer no final de sua contagem regressiva: ')
contagem_regressiva(contagem, mensagem)

def imprimir_impares(fim):
    i = 1
    while i <= fim :
        if i % 2 != 0 :
            print(i)
        i += 1
fim = int(input('Insira o valor do número final: '))
imprimir_impares(fim)

def imprimir_multiplos(multiplo, quantidade):
    i = 0
    n = 0
    while i <= quantidade :
        if n % multiplo == 0 :
            print(n)
            i += 1
        n += 1

n = int(input('Insira um número inteiro: '))
quantidade = int(input('Insira a quantidade de números a serem imprimidos: '))
imprimir_multiplos(n, quantidade)

def imprimir_tabuada(numero, inicio, fim):
    i = inicio
    print(f'ღ(¯`◕‿◕´¯) ♫ ♪ ♫ Tabuada do Número {numero} ♫ ♪ ♫ (¯`◕‿◕´¯)ღ')
    while i <= fim:
        print(f'{numero} X {i} = {numero * i}')
        i += 1
n = int(input('Insira um número inteiro: '))
inicio = int(input('Insira o começo da tabuada: '))
fim = int(input('Insira o fim da tabuada: '))
imprimir_tabuada(n, inicio, fim)

def juros (capital, taxa):
    i = 1
    taxa = (taxa/100) + 1
    while i <= 24:
        capital = capital * taxa
        print(f'Mês {i} | Ganhos: R${capital}')
        i += 1
capital = float(input('Insira o seu capital inicial: '))
taxa = float(input('Insira a taxa de juros: '))
juros(capital, taxa)

def juros_2 (capital, taxa, deposito):
    i = 1
    taxa = (taxa/100) + 1
    while i <= 24:
        capital = (capital + deposito) * taxa
        print(f'Mês {i} | Ganhos: R${capital}')
        i += 1
capital = float(input('Insira o seu capital inicial: '))
taxa = float(input('Insira a taxa de juros: '))
deposito = float(input('Insira seu depósito mensal: '))
juros_2(capital, taxa, deposito)

def ler_numeros():
    i = 0
    soma = 0
    while True:
        n = int(input('Insira um número inteiro: '))
        if n == 0 :
            break
        soma = soma + n
        i += 1
    media = soma / i
    print(f'Números Digitados: {i} | Soma: {soma} | Média: {media}')
ler_numeros()

def maquina_registradora():
    def calcular_preco(codigo, quantidade):
        if codigo == 1 :
            return 0.50 * quantidade
        elif codigo == 2 :
            return 1 * quantidade
        elif codigo == 3 :
            return 4.00 * quantidade
        elif codigo == 5 :
            return 7.00 * quantidade
        elif codigo == 9 :
            return 8.00 * quantidade
        else :
            return 0
    print(f'ღ(¯`◕‿◕´¯) ♫ ♪ ♫ Máquina Registradora ♫ ♪ ♫ (¯`◕‿◕´¯)ღ')
    print('''
        Produto      | Código | Preço
        Bala         | 1      | R$0.50
        Pirulito     | 2      | R$1.00
        Trident      | 3      | R$4.00
        Chocolate    | 5      | R$7.00
        Coca-Cola    | 9      | R$8.00 
    ''')
    print('Para parar o programa digite 0')
    codigo = 0
    soma = 0
    while True:
        codigo = int(input('Insira o código do produto: '))
        if codigo == 0 :
            break
        quantidade = int(input('Insira a quantidade do produto: '))
        soma = soma + calcular_preco(codigo, quantidade)
    print(f'O total da compra é de R${soma}')


maquina_registradora()    
