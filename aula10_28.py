# Função para encontrar o índice do menor valor em uma lista
def indice_menor(lista):
    indice = 0  # Assume-se que o primeiro elemento seja o menor inicialmente
    for i in range(len(lista)):  # Itera sobre todos os índices da lista
        if lista[i] < lista[indice]:  # Se o elemento atual for menor que o elemento no índice 'indice'
            indice = i  # Atualiza o índice para o novo menor valor
    return indice  # Retorna o índice do menor valor

# Algoritmo de ordenação Selection Sort
def selection_sort(lista):
    ordenada = []  # Lista onde os elementos ordenados serão armazenados
    while lista:  # Enquanto a lista original não estiver vazia
        local_menor = indice_menor(lista)  # Encontra o índice do menor valor
        menor = lista.pop(local_menor)  # Remove o menor valor da lista original
        ordenada.append(menor)  # Adiciona o menor valor na lista ordenada
    return ordenada  # Retorna a lista ordenada

# Algoritmo de ordenação Selection Sort com otimização
def seletion_sort_melhorzinho(lista):
    for i in range(len(lista)):  # Itera sobre a lista
        local_menor = indice_menor(lista[i:])  # Encontra o menor valor a partir do índice i
        aux = lista[i]  # Salva o valor atual para troca posterior
        lista[i] = lista[local_menor]  # Coloca o menor valor no índice i
        lista[local_menor] = aux  # Coloca o valor que estava em i no local do menor
    return  # Função não retorna nada, mas modifica a lista in-place

# Algoritmo de ordenação Bubble Sort
def bubble_sort(lista):
    j = 0  # Contador de iterações
    while True:  # Laço infinito até que não haja mais trocas
        trocas = 0  # Contador de trocas realizadas nesta iteração
        for i in range(len(lista) - 1 - j):  # Itera pela lista, ignorando a última parte já ordenada
            if lista[i] > lista[i + 1]:  # Se o valor atual for maior que o próximo
                # Troca os valores
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                trocas += 1  # Aumenta o contador de trocas
        j += 1  # Aumenta a contagem de iterações
        if trocas == 0:  # Se nenhuma troca foi feita, a lista já está ordenada
            return  # Sai da função

# Função para calcular a raiz quadrada de um número utilizando o método de bisseção
def Raiz_quadrada(num):
    ini = 0  # Limite inferior
    fim = num  # Limite superior
    chute = (ini + fim) / 2  # Calcula o chute inicial como a média entre ini e fim
    while fim - ini > 0.001:  # Continua até que a diferença entre ini e fim seja suficientemente pequena
        if chute**2 > num:  # Se o chute for maior que o número
            fim = chute  # Diminui o limite superior
        else:
            ini = chute  # Aumenta o limite inferior
    return chute  # Retorna o valor aproximado da raiz quadrada

# Função recursiva para calcular a raiz quadrada utilizando o método de bisseção
def Raiz_binaria_recursiva(num, ini, fim):
    if fim == num:  # Caso base, onde os limites ainda não foram definidos
        ini = 0
        fim = num
    chute = (ini + fim) / 2  # Calcula o chute como a média entre ini e fim
    if fim - ini > 0.001:  # Se a diferença entre os limites ainda for grande o suficiente
        if chute**2 > num:  # Se o chute for maior que o número
            fim = chute  # Diminui o limite superior
        else:
            ini = chute  # Aumenta o limite inferior
        chute = Raiz_binaria_recursiva(num, ini, fim)  # Chama a função recursivamente
    return chute  # Retorna o valor aproximado da raiz quadrada

# Função para garantir que o usuário digite um número válido
def verifica_numero(msg):
    num = input(msg)  # Solicita a entrada do usuário
    while not num.isnumeric():  # Enquanto a entrada não for um número válido
        num = input(msg)  # Solicita novamente
    return int(num)  # Retorna o número convertido para inteiro

# Função para garantir que o usuário escolha uma opção válida de uma lista de opções
def forca_opcao(msg, lista_opcao):
    opcoes = '\n'.join(lista_opcao)  # Formata as opções para exibição
    escolha = input(f'{msg}\n{opcoes}\n->')  # Solicita a escolha do usuário
    while escolha not in lista_opcao:  # Enquanto a escolha não estiver nas opções válidas
        print('inválido')  # Informa que a opção é inválida
        escolha = input(f'{msg}\n{opcoes}\n->')  # Solicita novamente
    return escolha  # Retorna a opção escolhida

# Exemplo de uso de funções acima
lista = [5, 3, 1, 8, 4, 7, 10, 6, 2, 9]  # Lista inicial
print(lista)

# Teste da função Raiz_binaria_recursiva
print(Raiz_binaria_recursiva(25, 0, 25))

# Algoritmo Quicksort
def quicksort(lista):
    if len(lista) < 2:  # Se a lista tiver menos que 2 elementos, já está ordenada
        return lista
    pivo = lista[0]  # O primeiro elemento é o pivô
    menores = [elem for elem in lista if elem < pivo]  # Lista com elementos menores que o pivô
    maiores = [elem for elem in lista if elem > pivo]  # Lista com elementos maiores que o pivô
    menores_ordenados = quicksort(menores)  # Chamada recursiva para ordenar os menores
    maiores_ordenados = quicksort(maiores)  # Chamada recursiva para ordenar os maiores
    return menores_ordenados + [pivo] + maiores_ordenados  # Junta as listas ordenadas

# Teste da função Quicksort
lista = [5, 3, 8, 1, 7, 6, 2, 10, 4, 9]  # Lista inicial
lista = quicksort(lista)  # Ordena a lista
print(lista)  # Imprime a lista ordenada
