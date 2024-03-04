# programa para converter uma letra maiúscula em letra minúscula. Usando a tabela ASCII
letra = input('Insira uma letra: ');
letra = ord(letra);
if letra in range (65,91) :
    letra = letra + 32;
    print('A letra convertida em minúscula: ', chr(letra));
elif letra in range(97, 123):
    letra = letra - 32;
    print('A letra convertida em maiúscula: ', chr(letra));
else :
    print ('O caractere inserido é inválido');