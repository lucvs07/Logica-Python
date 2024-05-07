#1. Escreva um programa para ler 7 notas e calcular a média aritmética. 
def calcular_media():
    notas = []
    i = 1
    print('''
          ---- Calculadora de Média Aritmética das Notas -----
          
          Quando desejar não inserir mais notas digite (-1)
          ''')
    while True:
        n = float(input('Insira uma nota: '))
        if n >= 0:
            print(f'Nota {i}: {n}')
            notas.append(n)
            i+=1
        if n < 0 :
            break
    media = sum(notas)/len(notas)
    print(f'A média de {len(notas)} notas é {media}')

#2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras
def listas():
    lista1 = [3, 2, 5, 10]
    lista2 = [-1, 4, 6, 7, -12]
    lista3 = []
    lista3.extend(lista1)
    lista3.extend(lista2)
    print(lista3)
    lista3.sort()
    print(lista3)

#3 Modifique o exemplo anterior de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while
def encontrar_numero():
    arr = [0, 3, 6, 9, 12]
    while True :
        n = int(input('Insira o número inteiro'))
        if n in arr :
            print(f'O número {n} foi encontrado na lista')
            break
        else:
            print(f'O número {n} não foi encontrado na lista. Tente Novamente')
encontrar_numero()