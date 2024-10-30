import os
cpf = []
def cadastrar_cpf():
    limpar_tela()
    print('Você irá cadastrar uma lista de 10 CPF')
    while len(cpf) <= 9:
        cpf_value = int(input(f'Digite o {len(cpf) + 1}º CPF (sem espaços): '))
        cpf.append(cpf_value)
    print(cpf)
    voltar_tela_principal()

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def ordenar_lista():
    limpar_tela()
    print('Lista Ordenada')
    cpf_sorted = quicksort(cpf)
    i = 1
    for n in cpf_sorted :
        print(f'{i}º CPF: {n}')
        i = i + 1
    voltar_tela_principal()

def busca_binaria():
    limpar_tela()
    print('Busca Binária')
    input_cpf = int(input('Insira o cpf a ser buscado (sem espaços): '))
    begin = 0
    end = len(cpf)
    find = False
    while (begin <= end and find == False):
        mid = (begin + end) / 2
        if input_cpf == cpf[mid]:
            find = True
        elif input_cpf != cpf[mid]:
            end = mid - 1
        else :
            begin = mid + 1
        if find == True :
            print(f'O cpf: {input_cpf} foi encontrado na posição {mid}')
        else :
            print('Não foi Localizado')
    voltar_tela_principal()

   

def exibir_opcoes():
    '''
        Função para exibir as opções que o programa oferece
    '''
    print('1. Cadastrar CPF')
    print('2. Ordenar Lista')
    print('3. Busca Binária')
    print('4. Encerrar\n')

def voltar_tela_principal():
    '''
        Função para retornar a tela principal (inicial) do programa
    '''
    input('Pressione enter para voltar ao menu principal...')
    main()
def opcao_invalida():
    '''
        Função para exibir ao usuário que a opção escolhida está inválida
    '''
    print('Opção inválida!\n')
    voltar_tela_principal()

def limpar_tela():
    '''Limpa a tela do terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')
def exibir_titulo():
    '''Exibe o título do programa'''
    print("▀▄▀▄▀▄ C A D A S T R O  D E  C P F ▄▀▄▀▄▀\n")
    
def finalizar_app():
    '''
        Função para limpar o terminal e encerrar o programa
    '''
    limpar_tela()
    print('Encerrando...')

def escolher_opcao():
    '''
        Função para escolher uma opção das disponíveis no programa

        Input:
        - Opção que foi escolhida

        Output:
        - O usuário é direcionado para a opção que foi escolhida
        
        OPÇÕES: 
        - 1. Cadastrar CPF
        - 2. Ordenar Lista
        - 3. Busca Binária
        - 4. Encerrar
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_cpf()
        elif opcao_escolhida == 2:
            ordenar_lista()
        elif opcao_escolhida == 3:
            busca_binaria()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
            
    except: 
        opcao_invalida()


def main():
    limpar_tela()
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()