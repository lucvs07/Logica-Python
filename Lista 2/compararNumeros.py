#Faça um programa que receba dois números e mostre qual deles é o maior
n = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))

if n > n2 :
    print(f'O número {n} é maior que {n2}');
elif n2 > n :
    print(f'O número {n2} é maior que {n}');
else :
    print('Os números são iguais');

#Leia um número, se for positivo : calcule a raiz quadrada do número. Se o número for negativo : mostre uma mensagem dizendo que o número é inválido
import math;
n = float(input('Insira um número: '));
if n < 0 :
    print(f'O número {n} é inválido');
else :
    raiz = math.sqrt(n);
    print(f' A raiz quadradada de {n} é igual a: {raiz}');

#Leia um número real, se for positivo: imprima a raiz quadrada. Se o número for negativo imprima o número ao quadrado
import math;
n = float(input('Insira um número: '));
if n < 0 :
    quadrado = pow(n,2);
    print(f'{n} ao quadrado é igual a: {quadrado}')
else :
    raiz = math.sqrt(n);
    print(f' A raiz quadradada de {n} é igual a: {raiz}');

#Faça um programa que leia um número e caso seja positivo mostre : O número digitado ao quadrado e a raiz quadrada do número digitado
import math
n = float(input('Insira um número: '));
if n < 0 :
    print(f'O número {n} é inválido');
else :
    quadrado = pow(n,2);
    raiz = math.sqrt(n);
    print(f'{n} ao quadrado é igual a: {quadrado}');
    print(f'A raiz quadrada de {n} é igual a: {raiz}');

#Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar
n = int(input('Insira um número inteiro: '));
if n % 2 == 0 :
    print (f'{n} é um número par');
else :
    print(f'{n} é um número ímpar');

#Escreva um programa que dado dois número inteiros, mostre na tela o maior deles, assim como a diferença entre ambos
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

#Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.#
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

# Leia o salário e o valor da prestação, se o valorda prestação for 20% maior que o salário : imprima 'Empréstimo Não Concedido, caso não : imprima 'Empréstimo Concedido'
salario = float(input('Insira seu Salário: '));
emprestimo = float(input('Insira o valor da prestação do empréstimo: '))
if emprestimo > salario * 1.02 :
    print('Empréstimo Não Concedido');
else :
    print('Empréstimo Concedido')

