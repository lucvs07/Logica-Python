import os
from modulos.circulo import calcular_area_circulo
from modulos.triangulo import calcular_area_triangulo
from modulos.trapezio import calcular_area_trapezio
from modulos.losango import calcular_area_losango
numeros = []

def input_numeros(escolha):
    '''Função para receber os números do usuário'''
    if escolha == 1:
        raio = float(input('Digite o raio do círculo: '))
        while raio < 0:
            raio = float(input('O raio não pode ser negativo. Digite novamente: '))
        return raio
    if escolha == 2:
        base = float(input('Digite a base do triângulo: '))
        while base < 0:
            base = float(input('A base não pode ser negativa. Digite novamente: '))
        altura = float(input('Digite a altura do triângulo: '))
        while altura < 0:
            altura = float(input('A altura não pode ser negativa. Digite novamente: '))
        return base, altura
    if escolha == 3:
        base_maior = float(input('Digite a base maior do trapézio: '))
        while base_maior < 0:
            base_maior = float(input('A base maior não pode ser negativa. Digite novamente: '))
        base_menor = float(input('Digite a base menor do trapézio: '))
        while base_menor < 0:
            base_menor = float(input('A base menor não pode ser negativa. Digite novamente: '))
        while base_maior == base_menor:
            print('As bases não podem ser iguais. Digite novamente.')
            base_maior = float(input('Digite a base maior do trapézio: '))
            base_menor = float(input('Digite a base menor do trapézio: '))
        while base_maior < base_menor:
            print('A base maior deve ser maior que a base menor. Digite novamente.')
            base_maior = float(input('Digite a base maior do trapézio: '))
            base_menor = float(input('Digite a base menor do trapézio: '))
        altura = float(input('Digite a altura do trapézio: '))
        while altura < 0:
            altura = float(input('A altura não pode ser negativa. Digite novamente: '))
        return base_maior, base_menor, altura
    if escolha == 4:
        diagonal_maior = float(input('Digite a diagonal maior do losango: '))
        while diagonal_maior < 0:
            diagonal_maior = float(input('A diagonal maior não pode ser negativa. Digite novamente: '))
        diagonal_menor = float(input('Digite a diagonal menor do losango: '))
        while diagonal_menor < 0:
            diagonal_menor = float(input('A diagonal menor não pode ser negativa. Digite novamente: '))
        while diagonal_maior == diagonal_menor:
            print('As diagonais não podem ser iguais. Digite novamente.')
            diagonal_maior = float(input('Digite a diagonal maior do losango: '))
            diagonal_menor = float(input('Digite a diagonal menor do losango: '))
        while diagonal_maior < diagonal_menor:
            print('A diagonal maior deve ser maior que a diagonal menor. Digite novamente.')
            diagonal_maior = float(input('Digite a diagonal maior do losango: '))
            diagonal_menor = float(input('Digite a diagonal menor do losango: '))
        return diagonal_maior, diagonal_menor
    else:
        print('cu')
    

def resultados(res,tipo):
    dados_do_calculo = {'Tipo':tipo, 'Resultado':res}
    numeros.append(dados_do_calculo)
    print(f'A área do {tipo} é {res}')
    voltar_tela_principal()

def limpar_tela():
    '''Limpa a tela do terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo():
    '''Exibe o título do programa'''
    print("""
          ▁ ▂ ▄ ▅ ▆ ▇ █ C A L C U L A R █ ▇ ▆ ▅ ▄ ▂ ▁
          """)
def exibir_opcoes():
    '''
        Função para exibir as opções que o programa oferece
    '''
    print('1. Calcular Área do Círculo')
    print('2. Calcular Área do Triângulo')
    print('3. Calcular Área do Trapézio')
    print('4. Calcular Área do Losango')
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
        Função para listar os resultados disponíveis no dicionário (numeros)
    '''
    limpar_tela()
    print('▁ ▂ ▄ ▅ ▆ ▇ █ R E S U L T A D O S █ ▇ ▆ ▅ ▄ ▂ ▁\n')
    if len(numeros) > 0:
        print(f"{'Tipo'.ljust(20)}  | Resultado")
        for numero in numeros:
            tipo = numero['Tipo']
            res = numero['Resultado']
            print(f"{tipo.ljust(20)}  | {res}")
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
        - 1. Calcular área do círculo
        - 2. Calcular área do triângulo
        - 3. Calcular área do trapézio
        - 4. Calcular área de um losango
        - 5. Listar resultados
        - 6. Encerrar
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            resultados(
                calcular_area_circulo(input_numeros(opcao_escolhida)),
                tipo='Círculo')
        elif opcao_escolhida == 2:
            resultados(
                calcular_area_triangulo(*input_numeros(opcao_escolhida)),
                tipo='Triângulo')
        elif opcao_escolhida == 3:
            resultados(
                calcular_area_trapezio(*input_numeros(opcao_escolhida)),
                tipo='Trapézio')
        elif opcao_escolhida == 4:
            resultados(
                calcular_area_losango(*input_numeros(opcao_escolhida)),
                tipo='Losango')
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