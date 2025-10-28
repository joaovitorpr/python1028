def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

 # ":" slicing, utilizado para pegar todos os itens de uma lista até o seu final
def seletion_sort_melhorzinho(lista):
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:])
        aux = lista[i]
        lista[i] = lista[local_menor]
        lista[local_menor] = aux
    return

def bubble_sort(lista):
    j = 0
    while True:
        trocas = 0
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                trocas += 1
        j += 1
        if trocas == 0:
            return

def Raiz_quadrada(num):
    ini = 0
    fim = num
    chute = (ini + fim)/ 2
    while fim - ini > 0.001:
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
    return chute

def Raiz_binaria_recursiva(num):
    ini = 0
    fim = num
    chute = (ini + fim)/ 2
    if fim - ini > 0.001:
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
    return chute

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def forca_opcao(msg,lista_opcao):
    opcoes = '\n'.join(lista_opcao)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in lista_opcao:
        print('inválido')
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

lista = [5,3,1,8,4,7,6,2]
print(lista)

