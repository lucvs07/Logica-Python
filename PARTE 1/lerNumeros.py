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