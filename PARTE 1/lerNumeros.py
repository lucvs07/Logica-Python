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