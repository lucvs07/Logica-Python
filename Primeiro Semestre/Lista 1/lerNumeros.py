# Programa: ler.py
# Propósito: Ler um número inteiro e um número real e exibir na tela.
numeroInteiro = int(input('Digite um número inteiro: '));
print('O número informado foi: ', numeroInteiro);

# Propósito: Ler um número real e exibir na tela.
numeroReal = float(input('Digite um número real: '));
print('O número informado foi: ', numeroReal);

# Propósito: Ler 3 número inseridos e exibir a soma na tela.   
i = 0;
soma = 0;
while i < 3 :
    i += 1;
    n = float(input('Digite um número: '));
    soma = n + soma;
print('A soma dos números informados foi: ', soma);

# Propósito: Ler um número real e exibir na tela o quadrado do número inserido.
numeroReal = float(input('Digite um número real: '));
print('O quadrado do número inserido é ', pow(numeroReal, 2));

# Propósito: Ler um número real e exibir na tela a quinta parte do número inserido.
numeroReal = float(input('Digite um número real: '));
print('A quinta parte do número inserido é ', numeroReal / 5);

# Propósito: Ler 3 número inseridos e exibir a soma dos seus quadrados na tela.   
i = 0;
soma = 0;
while i < 3 :
    i += 1;
    n = float(input('Digite um número: '));
    n = pow(n, 2)
    soma = n + soma;
print('A soma dos quadrados dos números informados foi: ', soma);

# Propósito: Ler 4 notas inseridas e exibir a média na tela.   
i = 0;
soma = 0;
print('Média de 4 notas')
while i < 4 :
    i += 1;
    n = float(input('Digite uma nota: '));
    soma = n + soma;
print('A médida das notas informadas foi: ', soma / 4);

# Programa que lê o valor em real e a cotação do dólar, e realiza a conversão
real = float(input('Digite o valor em real a ser convertido: '));
cota = float(input('Digite o valor da cotação do dólar: '));
dolar = real / cota;
print('O valor convertido é: ', dolar );

# Programa para mostrar o sucessor e o antecessor de um número
n = int(input('Digite um número: '));
print("Seu Antecessor é: ", n-1, "e seu Sucessor é: ", n+1);

# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
n = int(input('Digite um número inteiro: '));
n = (n*3 + 1) + (n*2 - 1);
print(n);

# Leia o tamanho do lado de um quadro e imprima como resultado a sua área
lado = float(input('Insira o tamanho do lado do quadrado: '))
print('A área é ',pow(lado,2));

# Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente
import math;

raio = float(input('Insira o valor do raio do círculo: '));
area = math.pi * pow(raio,2);
print('A área do círculo é: ', area);

# Ler os valores dos catetos (a,b) e calcular e imprimir a hipotenusa
import math;

cateto_a = float(input('Insira o valor do cateto (a): '));
cateto_b = float(input('Insira o valor do cateto (b): '));

hipotenusa = math.sqrt(pow(cateto_a,2) + pow(cateto_b,2))
print ('O valor da hipotenusa é: ', hipotenusa);

# Leia a altura e o raio de um cilindro circular e imprima o volume do cilíndro
import math;
altura_h = float(input('Insira a altura do Cilindro Circular: '));
raio = float(input('Insira o raio do Cilindro Circular: '));
volume = math.pi * pow(raio,2) * altura_h;
print('O volume do cilindro é: ', volume);

#Ler o valor do produto e do desconto e imprimir o valor com desconto
produto = float(input('Insira o valor do produto: '));
desconto = float(input('Insira o valor do desconto: ')) / 100;
produto = produto - (produto * desconto);
print('O valor com desconto é: ', produto);

# Ler os valores do salário e a porcentagem do aumento e imprimir o novo salário
salario = float(input('Insira seu salário: '));
aumento = float(input('Insira a porcentagem de aumento: '))/100;
salario = salario * (1 + aumento);
print('Após o aumento, seu salário é: ', salario);

# Ler o valor de uma premiação e calcular e imprimir os ganhos de cada ganhador
premio = float(input('Insira o valor da premiação: '));
print('O Primeiro ganhador receberá: ', premio * 0.46);
print('O Segundo ganhador receberá: ', premio * 0.32);
print('O Terceiro ganhador receberá: ', premio * 0.28);

# Ler o salário por dia de um encanador e os dias trabalhos, calcular a quantia liquída do salário com 8% de imposto de renda
salario = float(input('Insira o valor que o encanador recebe por dia: '));
dias = int(input('Insira o número de dias trabalhados: '));
salario = (salario * dias) * (1-0.08);
print('A quantia ser paga ao encanador é: ', salario);

# Ler o valor da hora de trabalho (em reais) e o número de horas trabalhadas, calcular e imprimir o valor a ser pago com o acréscimo de 10%
salario = float(input('Insira o valor da hora de trabalho: '));
horas = float(input('Insira o número de horas trabalhadas: '));
salario = (salario * horas) * (1 + 0.10);
print('A quantia a ser paga é: ', salario);

# Calcular o salário de um funcionário com gratificação e imposto de renda a ser pago
salario = float(input('Insira seu Salário: '));
gratificao = float(input('Insira a porcentagem de sua gratificação: '))/100;
imposto = float(input('Insira a porcentagem do desconto do imposto de renda: '))/100;
salario = (salario * (1+gratificao)) - (salario*imposto);
print('O seu sálario é de: ',salario);

# Programa para ajudar vendedores
valor = float(input('Insira o valor total: '));
tipo = input('Parcelado(P) ou À Vista (V): ');
if tipo == 'V' :
    valor = valor * 0.9
    print ('O valor a ser pago é: ', valor);
    print ('A comissão do vendedor é de: ', valor * 0.05)
elif tipo == 'P' :
    parcelas = int(input('Insira a quantidade de parcelas: '));
    print ('Valor a ser pago nas parcelas: ', valor/parcelas);
    print ('A comissão do vendedor é de: ', valor * 0.05);
else :
    print ('Operação Inválida');

# Programa que recebe a altura de um degrau e altura que deseja alcançar, calcule e imprima a quantiade de degraus a serem subidos para alcançar o objetivo
altura_degraus = float(input('Insira a altura do degrau: '));
altura_objetivo = float(input('Insira a altura que deseja alcançar: '));
degraus = altura_objetivo / altura_degraus;
print ('Para alcançar seu objetivo é necessário subir: ', degraus , ' degraus');

# Programa que le um número inteiro positivo de três digitos e gera outro número formado pelos dígitos invertidos
numero = int(input('Insira um número intereio de 3 digítos (100 a 999): '));
# Verifica se o número é válido
while numero < 100 or numero > 999:
    numero = int(input('Número inválido! Insira um número intereio de 3 digítos (100 a 999): '));
# Transforma o número em string
numero = str(numero);
# Inverte o número
numero = numero[::-1];
print('Número invertido: ', numero);

# Leia um número inteiro de 4 digitos ( de 1000 a 9999) e imprima 1 dígito por linha.
numero = int(input('Digite um número inteiro de 4 digitos: '));
i = 0
if numero in range(1000, 10000):
    numero = str(numero);
    while i < 4:
        print(numero[i]);
        i += 1;
else:
    print('Número inválido');

# Escreva um programa que leais as coordenas x e y de pontos no R² e calcule sua distância da origem (0,0).
import math;
X_a = float(input('Digite a coordenada Xa: '));
y_a = float(input('Digite a coordenada Ya: '));
X_b = float(input('Digite a coordenada Xb: '));
y_b = float(input('Digite a coordenada Yb: '));
distancia = math.sqrt(pow(X_b - X_a, 2) + pow(y_b - y_a, 2));
print('A distância da origem é: ', distancia);

# Crie um programa que leia quanto dinheiro três amigos investiram em uma loteria e o valor do prêmio. O programa deve calcular e imprimir quanto cada um irá receber do prêmio com base no valor investido.
amigo_1 = float(input('Digite quanto o primeiro amigo investiu: '));
amigo_2 = float(input('Digite quanto o segundo amigo investiu: '));
amigo_3 = float(input('Digite quanto o terceiro amigo investiu: '));
total = amigo_1 + amigo_2 + amigo_3;

premio = float(input('Digite o valor do prêmio: '));
amigo_1 = (amigo_1 / total) * premio;
amigo_2 = (amigo_2 / total) * premio;
amigo_3 = (amigo_3 / total) * premio;

print('O valor total investido foi: ', total);
print('O primeiro amigo receberá: ', amigo_1);
print('O segundo amigo receberá: ', amigo_2);
print('O terceiro amigo receberá: ', amigo_3);

# Faça um programa para ler as dimensões de um terreno (comprimento e largura) e o preço do metro da tela. O programa deve calcular e imprimir o valor total para cercar o terreno com tela.
comprimento = float(input('Insira o Comprimento do Terreno em metros: '));
largura = float(input('Insira a Largura do Terreno em metros: '));
valor = float(input('Insira o Preço do metro da Tela: '));
if comprimento == largura:
    valor = valor * (comprimento * 4);
else:
    valor = valor * (comprimento * 2 + largura * 2);

print('O valor total é: R$', valor);