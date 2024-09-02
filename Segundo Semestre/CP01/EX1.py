import os
# Cálcular a média de 3 variáveis (x, y, z) com 4 opções: Geométrica, Ponderada, Aritmética e Harmônica

# Dicionário para armazenar variáveis e resultados
numeros = []

def input_numeros():
    '''Função para receber os números do usuário'''
    x = float(input('Digite o primeiro número (x): '))
    y = float(input('Digite o segundo número (y): '))
    z = float(input('Digite o terceiro número (z): '))
    return x, y, z

def calcular_media_geometrica(x, y, z):
    '''Calcula a média geométrica de 3 variáveis'''
    res = (x * y * z) ** (1/3)
    dados_do_calculo = {'x':x, 'y': y, 'z': z, 'Tipo':'Geométrica', 'Resultado':res}
    print(dados_do_calculo)
    numeros.append(dados_do_calculo)
    print(f'A média geométrica de {x}, {y} e {z} é {res}')
    voltar_tela_principal()


def calcular_media_ponderada(x, y, z):
    '''Calcula a média ponderada de 3 variáveis'''
    res = (x + 2 * y + 3 * z) / 6
    dados_do_calculo = {'x':x, 'y': y, 'z': z, 'Tipo':'Ponderada', 'Resultado':res}
    print(dados_do_calculo)
    numeros.append(dados_do_calculo)
    print(f'A média ponderada de {x}, {y} e {z} é {res}')
    voltar_tela_principal()

def calcular_media_aritmetica(x, y, z):
    '''Calcula a média aritmética de 3 variáveis'''
    res = (x + y + z) / 3
    dados_do_calculo = {'x':x, 'y': y, 'z': z, 'Tipo':'Aritmética', 'Resultado':res}
    print(dados_do_calculo)
    numeros.append(dados_do_calculo)
    print(f'A média aritmética de {x}, {y} e {z} é {res}')
    voltar_tela_principal()

def calcular_media_harmonica(x, y, z):
    '''Calcula a média harmônica de 3 variáveis'''
    res = 3 / (1/x + 1/y + 1/z)
    dados_do_calculo = {'x':x, 'y': y, 'z': z, 'Tipo':'Harmônica', 'Resultado':res}
    print(dados_do_calculo)
    numeros.append(dados_do_calculo)
    print(f'A média harmônica de {x}, {y} e {z} é {res}')
    voltar_tela_principal()

def limpar_tela():
    '''Limpa a tela do terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo():
    '''Exibe o título do programa'''
    print("""
          🅒🅐🅛🅒🅤🅛🅐🅡
          """)
def exibir_opcoes():
    '''
        Função para exibir as opções que o programa oferece
    '''
    print('1. Calcular Média Geométrica')
    print('2. Calcular Média Ponderada')
    print('3. Calcular Média Aritmética')
    print('4. Calcular Média Harmônica')
    print('5. Listar resultados')
    print('6. Encerrar\n')
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
def finalizar_app():
    '''
        Função para limpar o terminal e encerrar o programa
    '''
    limpar_tela()
    print('Encerrando...')
def listar_resultados():
    '''
        Função para listar os restaurantes disponíveis no dicionário (restaurantes)
    '''
    limpar_tela()
    print('Lista de Resultados\n')
    if len(numeros) > 0:
        print(f"{'x'.ljust(23)} | {'y'.ljust(20)} |{'z'.ljust(20)}  |{'Tipo'.ljust(20)}  | Resultado")
        for numero in numeros:
            x = numero['x']
            y = numero['y']
            z = numero['z']
            tipo = numero['Tipo']
            res = numero['Resultado']
            print(f"{str(x).ljust(23)} | {str(y).ljust(20)} | {str(z).ljust(20)} | {tipo.ljust(20)} | {res}")
    else:
        print('Nenhum resultado encontrado.')
    print('')
    voltar_tela_principal()
def escolher_opcao():
    '''
        Função para escolher uma opção das disponíveis no programa

        Input:
        - Opção que foi escolhida

        Output:
        - O usuário é direcionado para a opção que foi escolhida
        
        OPÇÕES: 
        - 1. Calcular Média Geométrica
        - 2. Calcular Média Ponderada
        - 3. Calcular Média Aritmética
        - 4. Calcular Média Harmônica
        - 5. Listar resultados
        - 6. Encerrar
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            calcular_media_geometrica(*input_numeros())
        elif opcao_escolhida == 2:
            calcular_media_ponderada(*input_numeros())
        elif opcao_escolhida == 3:
            calcular_media_aritmetica(*input_numeros())
        elif opcao_escolhida == 4:
            calcular_media_harmonica(*input_numeros())
        elif opcao_escolhida == 5:
            listar_resultados()
        elif opcao_escolhida == 6:
            finalizar_app()
        else:
            opcao_invalida()
            
    except: 
        opcao_invalida()
def main():
    '''Função principal'''
    limpar_tela()
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()