def calcular_imposto(valor, estado):
    
    estados_validos = {'AM': 17,
                'MG': 15,
                'RJ': 6,
                'SP': 8,
                'MS': 12}
    # array com a sigla de todos os estados brasileiros
    estados=['SP', 'RJ', 'MG', 'AM', 'MS', 'MT', 'GO', 'PR', 'SC', 'RS', 'ES', 'BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE', 'PI', 'MA', 'PA', 'TO', 'RO', 'AC', 'RR', 'AP', 'DF']
    if estado not in estados:
        print('Estado Inválido')
    elif estado not in estados_validos:
        print(f'Não são comercializados produtos para o estado de {estado}')
    else:
        valor = valor * (1 + estados_validos[estado] / 100)
        print("▀▄▀▄▀▄ R E C I B O ▄▀▄▀▄▀")
        print(f'Para o estado de {estado} o imposto é de {estados_validos[estado]}%')
        print(f'O valor da venda com imposto é: R$ {valor}' )

