import requests  # Importar a biblioteca requests para fazer requisições HTTP
import unicodedata  # Importar a biblioteca unicodedata para manipulação de strings Unicode

# Função para obter a lista de cidades da API do IBGE
def lista_Cidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"  # URL da API do IBGE para obter os dados dos distritos
    resposta = requests.get(url)  # Fazer uma requisição GET para a API do IBGE
    if resposta.status_code == 200:  # Verificar se a resposta da requisição foi bem-sucedida
        return resposta.json()  # Se a resposta foi bem-sucedida, retornar os dados em formato JSON
    else:
        return []  # Se a resposta não foi bem-sucedida, retornar uma lista vazia

# Função para normalizar os nomes das cidades
def nomes(cidades):
    nomes_cidades = []  # Lista para armazenar os nomes normalizados das cidades
    for cidade in cidades:  # Iterar sobre cada cidade na lista de cidades
        nome = cidade['nome']  # Obter o nome da cidade
        # Normalizar o nome removendo acentos e caracteres especiais
        nome_normalizado = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
        nomes_cidades.append(nome_normalizado)  # Adicionar o nome normalizado à lista de nomes de cidades
    return nomes_cidades  # Retornar a lista de nomes de cidades normalizados

# Função de ordenação Quick Sort
def quick_sort(lista):
    quickSortOrdena(lista, 0, len(lista)-1 ) # Chamada à função auxiliar de ordenação Quick Sort

# Função auxiliar para ordenação Quick Sort
def quickSortOrdena(lista, esq, dir):
    if esq < dir: # Verificar se o índice da esquerda é menor que o índice da direita
        indice = particao( lista, esq, dir) # Encontrar o índice do pivô após particionamento
        quickSortOrdena(lista, esq, indice-1) # Chamada recursiva para ordenar a sublista à esquerda do pivô
        quickSortOrdena(lista, indice+1, dir) # Chamada recursiva para ordenar a sublista à direita do pivô

# Função auxiliar para particionamento no Quick Sort
def particao(lista, esq, dir):
    indice_pivo = (esq+dir)//2 # Calcula o índice do pivô como o meio da lista
    pivo = lista[indice_pivo ]['nome'] # Selecionar o valor do pivô
    i = esq # Inicializar índices para percorrer a lista
    j = dir
    while i <= j: # Loop para particionar a lista
        while i <= dir and lista[i]['nome '] <= pivo: # Encontrar elemento maior do que o pivô à esquerda
            i += 1
        while j >= esq and lista[j]['nome'] > pivo: # Encontrar elemento menor do que o pivô à direita
            j -= 1
        if i < j: # Se os índices não se cruzam, trocar os elementos
            lista[i], lista[j] = lista[j], lista[i]
    lista[indice_pivo], lista[j] = lista[j], lista[indice_pivo] # Posicionar o pivô no local correto
    return j # Retornar o índice do pivô após particionamento

# Função de ordenação Merge Sort
def intercala(inicio, meio, fim, lista):
    w_lista = [] # Lista temporária para armazenar a lista intercalada
    i = inicio # Inicializar índices para percorrer as sublistas
    j = meio
    while i < meio and j < fim:  # Intercalar as sublistas enquanto houver elementos em ambos
        if lista[i] < lista[j]:
            w_lista.append(lista[i ])
            i += 1
        else:
            w_lista.append(lista[j])
            j += 1
    while j < fim: # Adicionar os elementos restantes da primeira sublista
        w_lista.append(lista[j])
        j += 1
    while i < meio: # Adicionar os elementos restantes da segunda sublista
        w_lista.append(lista[i])
        i += 1
    for k in range(inicio, fim): # Atualizar a lista original com os elementos intercalados
        lista[k] = w_lista[k - inicio]

# Função auxiliar para ordenação Merge Sort
def merge_sort(inicio, fim, lista):
    if inicio < fim - 1:
        meio = (inicio + fim) // 2
        merge_sort(inicio, meio, lista) # Chamada recursiva para ordenar a sublista esquerda
        merge_sort(meio, fim, lista) # Chamada recursiva para ordenar a sublista direita
        intercala(inicio, meio, fim, lista) # Intercalar as sublistas ordenadas

# Função de ordenação Bubble Sort
def bubble_sort(lista):
    n = len( lista) # Obter o tamanho da lista
    comparações = 0 # Inicializar o contador de comparações
    for i in range(n): # Loop externo para percorrer toda a lista
        for j in range(0, i-1): # Loop interno para percorrer a lista e comparar os elementos adjacentes
            comparações += 1 # Incrementar o contador de comparações a cada comparação
            if lista[j] > lista[j+1]: # Trocar os elementos se estiverem fora de ordem
                lista[j], lista[j +1] = lista[j+1], lista[j]
    print("Número de comparações no Bubble Sort:", comparações) # Imprimir o número total de comparações
    return lista

# Função de ordenação Selection Sort
def selection_sort(lista):
    n = len(lista) # Obtenha o tamanho da lista
    comparações = 0 # Inicializar o contador de comparações
    for i in range(n): # Loop externo para percorrer toda a lista
        min_index = i # Inicializar o índice do menor elemento como o atual
        for j in range(i+1, n): # Encontrar o índice do menor elemento restante
            comparações += 1 # Incrementar o contador de comparações a cada comparação
           
