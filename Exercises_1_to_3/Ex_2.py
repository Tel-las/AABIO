# -*- coding: utf-8 -*-

class SuffixTree_2:

    def __init__(self):
        self.nodes = {0: (-1, {})}  # root node
        self.num = 0
        self.seq1 = ''
        self.seq2 = ''

    def unpack(self, k):
    """
    This function filters the -1 of the branches and unpacks the tuple of the leaves
    """
        if self.nodes[k][0] == -1:
            m = self.nodes[k][0]
            n = ''
        else:
            m, n = self.nodes[k][0]
        return m, n


    def print_tree(self):
    """
    This function was altered to accomodate the new tuple keys and to unpack them for processing
    """
        for k in self.nodes.keys():
            m, n = self.unpack(k)

            if m < 0: #If different than -1
                print(k, "->", self.nodes[k][1]) #Print branch
            else:
                print(k, ":", m, n) #Print leaf

    def add_node(self, origin, symbol, leafnum=-1):
        self.num += 1  # Incrementa o número do node
        self.nodes[origin][1][
            symbol] = self.num  # Acede ao dicionário do tuplo do nó e atribui ao nucleótido o nº do node
        self.nodes[self.num] = (leafnum, {})  # Criar o tuplo onde se guardam as próximas posições

    def add_suffix(self, p, sufnum):  # padrão e posição no padrão
        pos = 0
        node = 0
        while pos < len(p):  # Enquanto a posição for inferior ao tamanho do padrão
            if p[pos] not in self.nodes[node][1].keys():  # Se a letra na posição pos da seq p não estiver no node/ o [1] vai buscar o dicionário dentro do tuplo
                if pos == len(p) - 1:  # Se estiver no último caracter da sequência
                    self.add_node(node, p[pos], sufnum)  # Adiconar o node final; argumentação leafnum != -1
                else:
                    self.add_node(node, p[pos])  # Adiciona o node
            node = self.nodes[node][1][p[pos]]  # Dizer o nó onde estamos
            pos += 1  # Incrementa a posição

    def suffix_tree_from_seq(self, seq1, seq2):
        seq1 = seq1 + "$"
        seq2 = seq2 + "#" #New seq with new termination "#" is added
        self.seq1 = seq1
        self.seq2 = seq2
        for i in range(len(seq1)):  # Para o range da sequencia mais o sufixo
            # Passa texto iniciando de uma posição inicial i (iterada no range) e a posição como argumentos a função add_suffix
            self.add_suffix(seq1[i:], (0, i)) # i foi substituido por tuplo, em que o 0 corresponde a uma árvore
        for i in range(len(seq2)):  # Para o range da sequencia mais o sufixo
            # Passa texto iniciando de uma posição inicial i (iterada no range) e a posição como argumentos a função add_suffix
            self.add_suffix(seq2[i:], (1, i))# i foi substituido por tuplo, em que o 0 corresponde à OUTRA árvore

    # Utilizar a suffix tree para encontrar padrões

    def find_pattern(self, pattern):
        node = 0
        for pos in range(len(pattern)):  # Iterar a posição no padrão
            if pattern[pos] in self.nodes[node][1].keys():  # Se a letra estiver nas letras do dicionário
                node = self.nodes[node][1][pattern[pos]]  # Define o node pela posição associada ao nucleótido no dicionário do node 0
            else:
                return None
        return self.get_leafes_below(node)  # Passa o nó para a função get_leafes_below

    def get_leafes_below(self, node):
        res_1 = []
        res_2 = []# Abre a lista com as resoluções
        m, n = self.unpack(node)
        if m >= 0:  # Se o nó for diferente de -1 - é p final da árvore
            if m == 1:
                res_1.append(n)
            else: res_2.append(n)# Guarda a posição do node
        else:  # Se o nó for -1 - ou seja é um elemento do ramo
            for k in self.nodes[node][1].keys():  # Iterar as chaves dos dicionários (nucleótidos)
                newnode = self.nodes[node][1][k]  # Abre um novo nó
                lista_1, lista_2 = self.get_leafes_below(newnode)  # Recorre a função utilizando o novo nó
                res_1.extend(lista_1)
                res_2.extend(lista_2) #Concatenar a lista à resolução
        return (res_1, res_2)  #Devolve os resultados

    def largestCommonSubstring(self):
        seq1 = self.seq1
        seq2 = self.seq2
        match = ''
        for i in range(0,len(seq1)):
            for j in range(0,len(seq2)):
                k = 1
# now applying while condition until we find a substring match and length of substring is less than length of seq1 and seq2
                while i+k <= len(seq1) and j+k <= len(seq2) and seq1[i:i+k] == seq2[j:j+k]:
                    if len(match) <= len(seq1[i:i+k]):
                       match = seq1[i:i+k]
                    k = k+1
        return match

def test():
    seq1 = "TATCACAAAA" #Input the first sequence
    seq2 = "TATGCACAAAA" #Input the second sequence
    st = SuffixTree_2()
    st.suffix_tree_from_seq(seq1, seq2)
    st.print_tree()
    print(st.find_pattern("CA"))
    print(st.largestCommonSubstring())



test()
print()
#test2()




