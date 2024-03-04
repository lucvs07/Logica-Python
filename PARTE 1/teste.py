# Programa que le um número inteiro positivo de três digitos e gera outro número formado pelos dígitos invertidos
numero = int(input('Insira um número intereio de 3 digítos (100 a 999): '));
if numero in range (100, 1000):
    digitos = str(numero);
    digitos[0] = digitos[2];
    digitos[2] = digitos[0];
    numero ="".join(digitos);
    print(numero);
else : 
    print('Numero Inválido');