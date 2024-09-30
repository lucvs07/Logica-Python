import os
from calcular import calcular_imposto as calc

def input_valores():
    '''
        Função para receber os valores finais e o estado do usuário e processar a compra
    '''
    limpar_tela()
    valor_final = float(input('Digite o valor final: R$ '))
    estado = input('Digite a sigla do estado: ').upper()
    calc(valor_final, estado)
    voltar_tela_principal()


def exibir_opcoes():
    '''
        Função para exibir as opções que o programa oferece
    '''
    print('1. Iniciar Venda')
    print('2. Encerrar\n')
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
    print("▀▄▀▄▀▄ H O B B Y  E M  M I N I A T U R A S ▄▀▄▀▄▀\n")
    
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
        - 1. Iniciar Venda
        - 2. Encerrar
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            input_valores()
        elif opcao_escolhida == 2:
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