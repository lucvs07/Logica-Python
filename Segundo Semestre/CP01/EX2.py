'''
Elabore um programa completo em Python que possua uma função. Essa função deve receber como parâmetros: uma lista de 20 nomes, um índice inicial e um índice final. É mandatário que o índice final seja maior ou igual ao índice inicial, e que ambos, tanto o inicial quanto o final, estejam definidos entre 0 e 19, inteiros. 

A função deverá ser capaz de ordenar os nomes que estão entre o menor índice e o maior índice em ordem alfabética. Depois, deve retornar o resultado ao corpo principal.

De volta à função principal, a lista de nomes deve ser impressa (somente essa faixa determinada).
'''
def ordenar_nomes(nomes, inicio, fim):
    '''
    função para ordenar os nomes entre o índice inicial e o índice final em ordem alfabética
    '''
    if inicio < 0 or inicio > 19 or fim < 0 or fim > 19 or fim < inicio:
        return 'Índices inválidos!'
    nomes[inicio:fim] = sorted(nomes[inicio:fim])
    return nomes[inicio:fim]

def receber_nomes():
    nomes = []
    print('Inserir 20 nomes')
    i = 0
    while i < 20 :
        n = input(f'Insira o {i+1}° nome: ')
        i = i + 1
        nomes.append(n)
    return nomes

def main():
    '''
    função principal
    '''
    nomes = receber_nomes()
    inicio = int(input('Digite o índice inicial: '))
    fim = int(input('Digite o índice final: '))
    print(ordenar_nomes(nomes, inicio, fim))
if __name__ == '__main__':
    main()
