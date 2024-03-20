'''
Exercício 1 :

Escreva um programa que leia dois números e que 
pergunte qual operação você deseja realizar. Você deve 
poder calcular soma, subtração, multiplicação e divisão. 
Exiba o resultado da operação solicitada

'''
def calcular(operacao, n1, n2):
    '''
    Função para calcular uma operação entre dois números

    Inputs:
    - Operação Escolhida
    - Número 1
    - Número 2

    Outputs:
    - Resultado da operação escolhida entre os dois números
    '''
    if operacao == 'S':
        return f'O resultado da soma entre {n1} e {n2} é {n1+n2}';
    elif operacao == 'Sub' :
        return f'O resultado da subtração entre {n1} e {n2} é {n1-n2}';
    elif operacao == 'M' :
        return f'O resultado da multiplicação entre {n1} e {n2} é {n1*n2}';
    elif operacao == 'D' :
        return f'O resultado da divisão entre {n1} e {n2} é {n1/n2}';
    else :
        return f'A operação {operacao} é inválida';

operacao = input('Selecione a operação entre Soma (S), Substração(Sub), Multiplicação(M) ou Divisão(D): ');
n1 = float(input('Insira um número: '));
n2 = float(input('Insira o outro número: '));
print(calcular(operacao, n1, n2));

'''
Exercício 2 :

Escreva um programa para aprovar o empréstimo 
bancário para compra de uma casa. O programa deve 
perguntar o valor da casa a comprar, o salário e a 
quantidade de anos a pagar. O valor da prestação 
mensal não pode ser superior a 30% do salário. Calcule 
o valor da prestação como sendo o valor da casa a 
comprar dividido pelo número de meses a pagar
'''

valor_casa = float(input('Insira o valor da casa a ser comprada: '))
salario = float(input('Insira seu salário: '))
tempo = float(input('Em quantos anos deseja pagar a casa: ')) * 12;
prestacao = valor_casa / tempo

if prestacao > 1.3 * salario :
    print(f'Empréstimo Reprovado ! O valor da prestação {prestacao} é superior a 30% do seu salário {salario}');
else :
    print(f'Empréstimo Aprovado! O valor de sua prestação é de {prestacao}');

'''
Exercício 3

Escreva um programa que calcule o preço a pagar 
pelo fornecimento de energia elétrica. Pergunte a 
quantidade de kWh consumida e o tipo de instalação: R 
para residências, I para indústrias e C para comércios. 
Calcule o preço a pagar de acordo com a tabela

Residencial (R) :
- Até 500 kWh -> R$0.40
- Acima de 500 kWh -> R$ 0.65

Comercial (C): 
- Até 1000 kWh -> R$0.55
- Acima de 1000 kWh -> R$ 0.60

Industrial (I):
- Até 5000 kWh -> R$0.55
- Acima de 5000 kWh -> R$0.60
'''

def calcular_conta (operacao, energia):
    '''
    Função que calcula o valor a ser pago da conta de energia elétrica por uma instalação

    Inputs :
    - Tipo da Instalação -> Residencial(R), Comercial(C) ou Industrial(I)
    - Energia em kWh

    Outputs:
    - Valor a ser pago pela instalação
    '''
    if operacao == 'R':
        if energia <= 500 :
            return f'O preço a pagar em sua residência é de R${energia * 0.40}'
        elif energia > 500 :
            return f'O preço a pagar em sua residência é de R${energia * 0.65}'
        else :
            return f'Valor de {energia} kWh é inválido'
    elif operacao == 'C' :
        if energia <= 1000 :
            return f'O preço comercial a ser pago é de R${energia*0.55}'
        elif energia > 1000 :
            return f'O preço comercial a ser pago é de R${energia*0.60}'
        else :
            return f'O valor de {energia} kWh é inválido'
    elif operacao == 'I' :
        if energia <= 5000 :
            return f'O preço industrial a ser pago é de R${energia*0.55}'
        elif energia > 5000 :
            return f'O preço industrial a ser pago é de R${energia*0.60}'
        else :
            return f'O valor de {energia} kWh é inválido'
    else :
        return f'A operação {operacao} é inválida'
    
operacao = input('Selecione o tipo de Instalação entre Residencial(R), Comercial(C) ou Industrial (I): ');
energia = float(input('Insira a quantidade de energia elétrica em kWh: '));
print(calcular_conta(operacao, energia));

'''
Exercício 4

Faça um programa que leia 2 notas de um aluno, 
calcule a média e imprima aprovado ou reprovado (para 
ser aprovado a média deve ser no mínimo 6)
'''

def calcularNota (nota):
    '''
    Função para calcular a média de uma nota e retornar se o aluno está reprovado ou aprovado

    Inputs:
    - Soma das Notas

    Outputs:
    - Reprovado ou Aprovado
    '''
    media = soma / 2;
    if media >= 6 :
        return 'Aprovado'
    else :
        return 'Reprovado'

i = 0
soma = 0
while i < 2 :
    i+= 1;
    nota = float(input(f'Insira a nota({i}): '));
    soma = soma + nota;

print(calcularNota(soma));

'''
Exercício 5
Refaça o exercício 4, identificando o conceito 
aprovado (média superior ou igual a 6), exame (média 
maior ou igual a 4 e menor que 6) ou reprovado (média 
inferior a 4)
'''

def calcularNota (nota):
    '''
    Função para calcular a média de uma nota e retornar se o aluno está reprovado ou aprovado

    Inputs:
    - Soma das Notas

    Outputs:
    - Reprovado , Aprovado ou Exame
    '''
    media = soma / 2;
    if media >= 6 :
        return f'Você foi aprovado com a média de {media}'
    elif media >= 4 and media < 6 :
        return f'Você ficou de exame com a média de {media}'
    else :
        return f'Você foi reprovado com a média de {media}'

i = 0
soma = 0
while i < 2 :
    i+= 1;
    nota = float(input(f'Insira a nota({i}): '));
    soma = soma + nota;

print(calcularNota(soma));

'''
Exercício 6
Ler três valores para os lados de um triângulo, considerando 
lados como: A, B e C. Verificar se os lados fornecidos formam 
realmente um triângulo, e se for esta condição verdadeira, 
deverá ser indicado qual tipo de triângulo foi formado: 
isósceles, escaleno ou equilátero. Faça o algoritmo, diagrama 
em blocos e a codificação em C, prestando atenção na 
utilização dos operadores lógicos

Dados:
Um polígono de 3 lados é um triângulo quando: A < B + C; 
B < A + C; C < A + B
Triângulo Isósceles: possui dois lados iguais e um diferente.
Triângulo Escaleno: possui todos os lados diferentes.
Triângulo Equilátero: possui todos os lados iguais

'''

print('Verificador de Triângulos')
lado_a = float(input('Insira o lado A do triângulo: '));
lado_b = float(input('Insira o lado B do triângulo: '));
lado_c = float(input('Insira o lado C do triângulo: '));

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b :
    if lado_a == lado_b == lado_c :
        print('É um triângulo Equilátero')
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c :
        print('É um triângulo Isósceles');
    else :
        print('É um Triângulo Escaleno');
else :
    print('Não é um triângulo')