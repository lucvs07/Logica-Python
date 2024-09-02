#1- Faça um programa que receba dois números e mostre qual deles é o maior
n = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))

if n > n2 :
    print(f'O número {n} é maior que {n2}');
elif n2 > n :
    print(f'O número {n2} é maior que {n}');
else :
    print('Os números são iguais');

#2- Leia um número, se for positivo : calcule a raiz quadrada do número. Se o número for negativo : mostre uma mensagem dizendo que o número é inválido
import math;
n = float(input('Insira um número: '));
if n < 0 :
    print(f'O número {n} é inválido');
else :
    raiz = math.sqrt(n);
    print(f' A raiz quadradada de {n} é igual a: {raiz}');

#3- Leia um número real, se for positivo: imprima a raiz quadrada. Se o número for negativo imprima o número ao quadrado
import math;
n = float(input('Insira um número: '));
if n < 0 :
    quadrado = pow(n,2);
    print(f'{n} ao quadrado é igual a: {quadrado}')
else :
    raiz = math.sqrt(n);
    print(f' A raiz quadradada de {n} é igual a: {raiz}');

#4- Faça um programa que leia um número e caso seja positivo mostre : O número digitado ao quadrado e a raiz quadrada do número digitado
import math
n = float(input('Insira um número: '));
if n < 0 :
    print(f'O número {n} é inválido');
else :
    quadrado = pow(n,2);
    raiz = math.sqrt(n);
    print(f'{n} ao quadrado é igual a: {quadrado}');
    print(f'A raiz quadrada de {n} é igual a: {raiz}');

#5- Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar
n = int(input('Insira um número inteiro: '));
if n % 2 == 0 :
    print (f'{n} é um número par');
else :
    print(f'{n} é um número ímpar');

#6 e 7- Escreva um programa que dado dois número inteiros, mostre na tela o maior deles, assim como a diferença entre ambos
n = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n > n2 :
    sub = n - n2
    print(f'O número {n} é maior que {n2} e a diferença existente entre eles é : {sub}');
elif n2 > n :
    sub = n2 - n
    print(f'O número {n2} é maior que {n} e a difrença existente entre eles é: {sub}');
else :
    print('Os números são iguais');

#8- Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.#
nota = float(input('Insira a nota de 0 a 10: '));
if nota < 0 :
    print(f'a nota {nota} inserida é inválida');
elif nota >= 0 :
    nota2 = float(input('Insira a outra nota de 0 a 10: '));
    if nota2 < 0 :
        print(f'A nota {nota2} inserida é inválida');
    else:
        media = (nota + nota2) / 2
        print (f'A média das notas é {media}');

#9- Leia o salário e o valor da prestação, se o valorda prestação for 20% maior que o salário : imprima 'Empréstimo Não Concedido, caso não : imprima 'Empréstimo Concedido'
salario = float(input('Insira seu Salário: '));
emprestimo = float(input('Insira o valor da prestação do empréstimo: '))
if emprestimo > salario * 1.02 :
    print('Empréstimo Não Concedido');
else :
    print('Empréstimo Concedido')

#10- Receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal
sexo = input('Insira seu genêro Feminino (F) ou Masculino (M): ');
altura = float(input('Insira sua altura: '))
def peso_ideal(altura, sexo):
    if sexo == 'F':
        return (62.1 * altura) - 44.7
    elif sexo == 'M' :
        return (72.7 * altura) - 58
    else :
        print('Genêro inserido inválido');
print(f'O peso ideal é igual a: {peso_ideal(altura, sexo)}');

# 11 - Ler um número inteiro e calcular a soma de seus algarismos
n = int(input('Insira um número inteiro: '))
soma = 0
# Enquanto n for maior que 0, a variável soma irá receber o resto da divisão de n por 10 e n irá receber a divisão inteira de n por 10
while n > 0 :
    soma += n % 10
    n = n // 10
print(f'A soma dos algarismos do número é igual a: {soma}')

#12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo, calcular o logaritmo deste número.
# Inserindo a biblioteca math
import math
n = int(input("Insira um número inteiro: "))
log = 0
if n < 0 :
    print(f'O número : {n}, é inválido');
elif n >= 0 :
    log = math.log(n);
    print(f'O logaritmo natural do número {n} é igual a {log}');
else :
    print('Erro Desconhecido !')

# 13 - Faça um algoritmo que calcule a média ponderada de 3 notas, mostre a média final do aluno e indique se o aluno for aprovado. Aprovação : média maior que 60 pontos
i = 0
notas = []
pesos = []
while i != 3 :
    i = i+1
    nota = int(input(f'Insira a nota {i} (ex:100): '))
    notas.append(nota)

n = 0
while n != 3 :
    n = n+1
    peso = int(input(f'Insira o peso da nota {n}: '))
    pesos.append(peso)
soma_pesos = sum(pesos);

pos = 0
soma_notas = 0
while pos < len(notas):
    soma_notas = soma_notas + (notas[pos]*pesos[pos])
    pos = pos + 1

media = soma_notas / soma_pesos

if media > 60 :
    print(f'O aluno foi aprovado com média: {round(media)}')
else :
    print(f'O aluno foi reprovado com média: {round(media)}')

#14
n1 = float(input("Insira a nota do trabalho de laboratório: "))*2
n2 = float(input("Insira a nota da avaliação semestral: "))*3
n3 = float(input("Insira a nota do Exame Final: "))*5
media = (n1+n2+n3)/10
if media > 0 and media < 2.9 :
    print(f'O aluno está reprovado ! Média: {media}')
elif media > 3 and media < 4.9 :
    print(f'O aluno está de recuperação ! Média: {media}')
elif media > 4.9 :
    print(f'O aluno está Aprovado! Média: {media}')
else :
    print("Erro desconhecido !")

# 15
n = int(input("Insira um número inteiro: "))

match n :
    case 1 :
        print(f'Domingo({n})')
    case 2 :
        print(f'Segunda-Feira({n})')
    case 3 :
        print(f'Terça-Feira({n})')
    case 4:
        print(f'Quarta-Feira({n})')
    case 5 :
        print(f'Quinta-Feira({n})')
    case 6 :
        print(f'Sexta-Feira({n})')
    case 7 :
        print(f'Sábado({n})')
    case _:
        print(f'Opção({n}) Inválida !')

# 16
n = int(input("Insira um número inteiro: "))

match n :
    case 1 :
        print(f'Janeiro({n})')
    case 2 :
        print(f'Fevereiro({n})')
    case 3 :
        print(f'Março({n})')
    case 4:
        print(f'Abril({n})')
    case 5 :
        print(f'Maio({n})')
    case 6 :
        print(f'Junho({n})')
    case 7 :
        print(f'Julho({n})')
    case 8 :
        print(f'Agosto({n})')
    case 9 :
        print(f'Setembro({n})')
    case 10 :
        print(f'Outubro({n})')
    case 11 :
        print(f'Novembro({n})')
    case 12 :
        print(f'Dezembro({n})')
    case _:
        print(f'Opção({n}) Inválida !')

# 17
base_maior = float(input('Insira o valor da base maior do trapézio: '))
base_menor = float(input('Insira o valor da base menor do trapézio: '))
altura = float(input('Insira o valor da altura do trapézio: '))
area = (base_menor+base_maior) * altura / 2
if base_maior > 0 and base_menor > 0 and altura > 0 :
    print(f'A área do trapézio é de {area}')
else :
    print(f'Valores Inseridos são inválidos !')

# 19
n = int(input('Insira um número inteiro: '))
if n % 3 == 0 and n % 5 == 0 :
    print(f'o número {n} é divísivel por 3 e 5')
elif n % 3 == 0 :
    print(f'O número {n} é divísivel por 3')
elif n % 5 == 0 :
    print(f'O número {n} é divísivel por 5')
else :
    print(f'O número {n} não é divísvel por 3 e nem por 5')

#22
idade = int(input('Insira sua idade: '))
trabalho = int(input('Insira seu tempo de serviço: '))

if idade >= 65 :
    print(f'Válido para aposentar ! Sua idade {idade} e tempo de serviço {trabalho}')
elif trabalho >= 30 :
    print(f'Válido para aposentar ! Sua idade {idade} e tempo de serviço {trabalho}')
elif idade >= 60 and trabalho >= 25 :
    print(f'Válido para aposentar ! sua idade {idade} e tempo de serviço {trabalho}')
else :
    print(f'Sua Situação é inválida para aposentadoria. Sua idade {idade} e tempo de serviço {trabalho}')

#23
ano = int(input('Insira o ano: '))
if (ano % 400 == 0 or ano % 4 == 0) and ano % 100 != 0 :
    print(f'O ano {ano} é um ano bissexto')
else :
    print(f'O ano {ano} não é um ano bissexto') 