import ler_arquivo_entrada
import heapq
'utf-8'

# @Autor José Maria Reis dos Santos

# Cursando segundo semestre de Banco de Dados Fatec São José Dos Campos

# • Descrição do problema escolhido (em detalhes)

'''
Objetivo: O projeto desenvolvido foi pensado em situações 
em que se precisa realizar um trabalho de cálculo de 
metragem de cabo/fibra opta para realizar uma conexão de rede.
O servidor Provedor de internet ficaria em um ponto específico da
cidade e passando as informações correta para arquivo de entrada.txt
sistema calcula o menor custo para realizar e também qual seria as rotas  melhores de passagem.  
O algoritmo utilizado foi:
• Árvore geradora mínima
'''
# • Descrição breve do funcionamento do algoritmo base do projeto

'''
O Algoritmo (Arvore Geradora Mínima) escolhido funciona da seguinte maneira, quando o mesmo recebe as informações 
de um grafo conectado, valorado e não direcionado, escolhendo uma raiz e a partir dessa começa analisar qual o menor custo para conectar todos 
os pontos (vértices) através das arestas que já tem seus pesos já determinado. No final da análise é encontrada a Arvore Geradora Mínima. 
'''
# • Identificação das variáveis de entrada e saída chaves do algoritmo

'''
As principais variáveis de entrada são:
n = sendo o número de vértices
m = sendo número de arestas
n_arestas = lista de arestas
raiz = ponto onde inicia a analise, isso ocorre de forma aleatória pelo import  random.
a, b, c = conexão do ponto (a) para (b) e seu custo (c) 

Principais variáveis de saída são:

custo_total = custo gerado no fim da analise
arv_ger_min = lista com minha Arvore Geradora Mínima expressa de forma numérica
arquivo = Gera meu resultado de saída e grava no arquivo saida.txt
'''

# • Documentação do padrão definido para o arquivo de entrada
'''
O arquivo de entrada deve ser fornecido de forma numérica,
sendo os dados de um grafo conectado, valorado e não direcionado,
esses dados são as conexões de cada vértices através de uma arresta, que são lidos
dessa forma:
a primeira linha da lista numérica fornecida de  conter quantidades  vértices (n) e quantidades arestas(m).
Nas próximas linhas (a) sendo o primeiro ponto,(b) o segundo e (c) o custo, (a e b) são vértices, toda vez que o 
algoritmos escolhe uma raiz para analisar ele analisa dessa forma, conexão de (a) para(b) e seu custo(c).


IMPORTANTE
O arquivo passado deve seguir rigorosamente esse padrão, lembrando que se for necessário testar 
com outro exemplo fora desse projeto seguir esse modelo.

primeira linha 9 números de vértices 14 números de arrestas
as seguintes linhas são minhas conexões de um ponto para outro
e seu custo, como se trata de uma lista começa analisando do  ponto (0) para ponto (1) e seu custo (4) e assim sucessivamente
exemplo do arquivo de entrada:


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
# • Documentação do padrão definido para o arquivo de saída
'''
meu arquivo de saida é gerado na primeira vez que executa o projeto,
as proximas execuções apenas sobrescrevera o resultado de saída
'''


def iniciar():

    valor =1
    if valor == 1:

        n,m,heap,n_valores = ler_arquivo_entrada.ler_arquivo1()

        a, b, c, n_valores,raiz= ler_arquivo_entrada.ler_arquivo2()

        for (x, c) in n_valores[raiz]:
            heapq.heappush(heap, (c, raiz, x))

        n_arestas = 0  # As conexões de um ponto a outro
        custo_total = 0  # Custo total inicia em zero
        marcados = [raiz]  # Marcador é de onde começa a analise do Grafo
        arv_ger_min = []  # Arvore geradora minima iniciando vazia

        while n_arestas < n - 1:
            while True:
                (c, a, b) = heapq.heappop(heap)
                if b not in marcados:
                    break
            marcados.append(b)

            custo_total += c
            arv_ger_min.append((a, b))
            n_arestas += 1

            for (x, c) in n_valores[b]:
                if x not in marcados:
                    heapq.heappush(heap, (c, b, x))

    else:
        pass

    arquivo = ler_arquivo_entrada.criar_aquivo_de_saida()
    arquivo =(arquivo)  # Abrindo meu Arquivo Saída.txt
    arquivo.write(' Os pontos de conexões onde vão gerar um menor custo: ')  # Gravado uma frase no arquivo
    arquivo.write(str(arv_ger_min))  # Gravando minha Arvore Geradora Minima
    arquivo.write("\n")
    arquivo.write(' Custo total em metros:  ')  # Gravado uma frase no arquivo
    arquivo.write(str([custo_total]))  # Gravando meu Custo Total no arquivo
    arquivo.close()

if (__name__ == "__main__"):
    iniciar()












