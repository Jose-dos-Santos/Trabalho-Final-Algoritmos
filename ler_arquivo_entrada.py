import heapq
import random
import os

def ler_arquivo1():
    heap = []
    with open('entrada_dados.txt', encoding='utf-8') as fp:  # Abrindo o Arquivo de entrada, o metodo with se encarrega de abrir e fechar o arquivo
        for i, line in enumerate(fp):
            if i == 0:
                v1, v2 = line.split()
                v1 = int(v1)
                v2 = int(v2)

            break

    n_valores = [[] * v1 for i in range(v1)]
    return v1, v2, heap, n_valores


def ler_arquivo2():
    n, m, heap, n_valores = ler_arquivo1()

    for j in range(m):
        with open('entrada_dados.txt') as fp:  # Abrindo o Arquivo de entrada
            for i, line in enumerate(fp):
                if i >= 1 and i <= j:  # Lendo a partir da linha um ate a ultima linha
                    a, b, c = line.split()
                    a = int(a)  # Representa um dos pontos de conexão (Nó) ponto A
                    b = int(b)  # Representa outro ponto de conexão (Nó) ponto B
                    c = int(c)  # Representa o Custo de um ponto a outro C
                    n_valores[a].append((b, c))
                    n_valores[b].append((a, c))
                    raiz = random.randint(0, n - 1)

    return a, b, c, n_valores, raiz


def criar_aquivo_de_saida():


    arquivo = open('saida.txt', 'w', encoding='utf-8')  # Criando meu Arquivo Saída.txt

    return arquivo

def arquivo_vazio(path):
    return os.stat(path).st_size==0

# Algumas entrada para realizar testes, caso queira testar copiar para o arquivo entrada123.txt


'''
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2  5 4
2 8 2
3 4 9
3 5 14
4 5 10    
5 6 2
6 7 1
6 8 6
7 8 7
'''


'''
7 11
0 1 1 
0 4 2
0 3 4
1 3 2 
1 2 4
2 3 1
2 6 2
3 4 2
3 5 2
4 5 3
5 6 3
'''
