''' Exercício 1 - Escreva um programa que pergunte a distância que 
um passageiro deseja percorrer em km. Calcule o preço 
da passagem, cobrando R$ 0,50 por km para viagens de 
até 200 km e R$ 0,45 para viagens mais longas.'''

def calcularPreco(distancia) :
    '''
    Função para calcular o gasto em uma viagem

    Inputs:
    - Distancia

    Outputs:
    -Valor gasto
    '''
    if distancia > 200 :
        return distancia * 0.45
    else :
        return distancia * 0.50;

distancia = float(input('Insira a distância total da viagem: '));

print(f'O valor total é de: {calcularPreco(distancia)}');

''' Exercício 2 - Considerando que uma determinada escola possui 
média 7 e que não há exame, efetuar a leitura de 3 
notas de um aluno, calcular a média aritmética simples e 
apresentar se o aluno está reprovado ou aprovado'''

def calcularNota (nota):
    '''
        Função para calcular a média de uma nota e retornar se o aluno está reprovado ou aprovado

        Inputs:
        - Soma das Notas

        Outputs:
        - Reprovado ou Aprovado
    '''
    media = soma / 3;
    if media >= 7 :
        return 'Aprovado'
    else :
        return 'Reprovado'

i = 0
soma = 0
while i < 3 :
    i+= 1;
    nota = float(input(f'Insira a nota({i}): '));
    soma = soma + nota;

print(calcularNota(soma));
