# Exercício 1
minha_altura = 1.78
sua_altura = float(input('Insira sua altura: '));
if sua_altura > minha_altura :
    print (f' Saudações ');
else :
    print('Tchau')

# Exercício 2
meu_peso = 70;
seu_peso = float(input('Insira seu peso: '));
if seu_peso != meu_peso :
    print(' Saudações ');
else :
    print('Tchau');

# Exercício 3
n = int(input('Insira um valor inteiro: '));
if n % 2 == 0 :
    quadrado = pow(n,2);
    print(f'{n} ao quadrado é igual a: {quadrado}');
else :
    print('Número Inválido')

# Exercício 4
velocidade = float(input('Insira sua velocidade em km/h: '));
if velocidade > 80 :
    multa = (velocidade - 80) * 5
    print(f'Sua velocidade {velocidade} está acima do permitido. Será necessário pagar uma multa de {multa}');
else :
    print('Você está dentro da velocidade permitida');

# Exercício 5
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais número: '))

def print_maior(n):
    print(f'O maior número é {n}');

def print_menor(n):
    print(f'O menor número é {n}');

if n1 > n2 and n1 > n3 :
    print_maior(n1)
    if n2 > n3 :
        print_menor(n3)
    else :
        print_menor(n2)
elif n2 > n1 and n2 > n3 :
    print_maior(n2)
    if n1 > n3 :
        print_menor(n3)
    else :
        print_menor(n1)
elif n3 > n1 and n3 > n2 :
    print_maior(n3)
    if n1 > n2 :
        print_menor(n2)
    else :
        print_menor(n1)
else :
    print (' Os números são iguais.')

# Exercício 6
salario = float(input('Insira seu salário: '));
if salario > 1250 :
    salario = salario * 1.1
    print(f'Seu salário aumentou para {salario}');
else :
    salario = salario * 1.15
    print(f'Seu salário aumentou para {salario}');
