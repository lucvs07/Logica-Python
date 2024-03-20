# Exercício 1
print(' Meu nome é Lucas ');

# Exercício 2
a = 3;
b = 5;
print(' Resultado: ',(2*a)*(3*b));

# Exercício 3
i = 0
soma = 0
while i < 3 :
    n = float(input('Insira um número: '));
    soma = soma + n;
    i+= 1;
print ('O resultado da soma é: ', soma)

# Exercício 4
i = 0
soma = 0
while i < 2 :
    n = float(input('Insira um número: '));
    soma = soma + n;
    i+= 1;
print ('O resultado da soma é: ', soma);

# Exercício 5
metros = float(input('Insira o valor em metros: '));
milimetros = metros * 1000;
print(f'O valor {metros} em metros é {milimetros} em milímetros.');

# Exercício 6
dias = float(input('Insira a quantidade de dias: '));
dias = dias * 24;

horas = float(input('Insira a quantidade de horas: '));
horas = (dias + horas) * 60;

minutos = float(input('Insira a quantidade de minutos: '));
minutos = (horas + minutos) * 60;

segundos = float(input('Insira a quantidade de segundos: '));
segundos = segundos + minutos;

print(f'O total em segundos é {segundos}');

# Exercício 7
salario = float(input('Insira o valor do seu salário: '));
aumento = float(input('Insira a porcentagem do aumento: '))/100;
aumento = salario * aumento;
salario = salario + aumento;
print(f'Seu salário teve um aumento de {aumento}, e novo valor de seu salário é: {salario}');

# Exercício 8
valor = float(input('Insira o valor da mercadoria: '));
desconto = float(input('Insira a porcentagem do desconto: '))/100;
desconto = valor * desconto;
valor = valor - desconto;
print(f'O valor do desconto é: {desconto}. O valor a ser pago é: {valor}');

# Exercício 9
distancia = float(input('Insira a distância da viagem em quilômetros(KM): '));
velocidade = float(input('Insira a velocidade média em KM/H: '));
tempo = distancia / velocidade;
print(f'A duração da viagem será de: {tempo}')

# Exercícios 10
celcius = float(input('Insira a temperatura em graus Celsius: '));
f = ((9 * celcius)/5) + 32;
print(f' A temperatura {celcius}° C é {f}°');

# Exercício 11
km = float(input('Insira a quantidade de quilômetros(km) percorridos: '));
dias = float(input('Insira a quantidade de dias que o carro ficou alugado: '));
valor_aluguel = float(input('Insira o valor da diária: '));
valor_km = float(input('Insira o valor do preço por KM rodado: '));

valor_aluguel = valor_aluguel * dias;
valor_km = valor_km * km;
valor = valor_km + valor_aluguel

print(f'O valor total a ser pago é: {valor}');

# Exercício 12
x = int(input('Insira o valor de x: '));
y = int(input('Insira o valor de y: '));
z = ((pow(x,2)+pow(y,2)) / pow((x-y),2));
print (f'O valor de z é: {z}');

# Exercício 13
salario = float(input('Insira o valor do salário: '));
reajuste = float(input('Insira o valor do reajuste em porcentagem: ')) / 100 + 1;
salario = salario * reajuste;
print (f'O valor após o reajuste é: {salario}');