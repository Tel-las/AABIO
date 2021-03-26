class SuffixTree:

    def __init__(self):
        self.nodes = { 0:(-1,{}) } # root node
        self.num = 0

    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print (k, "->", self.nodes[k][1])
            else:
                print (k, ":", self.nodes[k][0])

    def add_node(self, origin, symbol, leafnum = -1):
        self.num += 1 #Incrementa o número do node
        self.nodes[origin][1][symbol] = self.num #Acede ao dicionário do tuplo do nó e atribui ao nucleótido o nº do node
        self.nodes[self.num] = (leafnum,{}) #Criar o tuplo onde se guardam as próximas posições

    def add_suffix(self, p, sufnum): #padrão e posição no padrão
        pos = 0
        node = 0
        while pos < len(p): #Enquanto a posição for inferior ao tamanho do padrão
            if p[pos] not in self.nodes[node][1].keys(): #Se a letra na posição pos da seq p não estiver no node/ o [1] vai buscar o dicionário dentro do tuplo
                if pos == len(p)-1: #Se estiver no último caracter da sequência (se for o dollar)
                    self.add_node(node, p[pos], sufnum) #Adicona o node final; argumentação leafnum != -1
                else:
                    self.add_node(node, p[pos]) #Adiciona o node
            node = self.nodes[node][1][p[pos]] #Dizer o nó onde estamos
            pos += 1 #Incrementa a posição

    def suffix_tree_from_seq(self, text):
        t = text+"$" #Adiciona dollar no final da sequencia
        for i in range(len(t)): #Para o range da sequencia mais o dolar
        # Passa texto iniciando de uma posição inicial i (iterada no range) e a posição como argumentos a função add_
            self.add_suffix(t[i:], i)

#Utilizar a suffix tree para encontrar padrões

    def find_pattern(self, pattern):
        node = 0
        for pos in range(len(pattern)): #Iterar a posição no padrão
            if pattern[pos] in self.nodes[node][1].keys(): #Se a letra estiver nas letras do dicionário
                node = self.nodes[node][1][pattern[pos]] #Define o node pela posição associada ao nucleótido no dicionário do node 0
            else: return None
        return self.get_leafes_below(node) #Passa o nó para a função get_leafes_below


    def get_leafes_below(self, node):
        res = [] #Abre a lista com as resoluções
        if self.nodes[node][0] >=0: #Se o nó for diferente de -1 - é p final da árvore
            res.append(self.nodes[node][0]) #Guarda a posição do node
        else: #Se o nó for -1 - ou seja é um elemento do ramo
            for k in self.nodes[node][1].keys(): #Iterar as chaves dos dicionários (nucleótidos)
                newnode = self.nodes[node][1][k] #Abre um novo nó
                leafes = self.get_leafes_below(newnode) #Recorre a função utilizando o novo nó
                res.extend(leafes) #Concatenar a lista à resolução
        return res #Devolve os resultados


    def nodes_below(self, identificador):
        """
        Resolução Exercício 1_a
        """
        if identificador in self.nodes.keys(): # Verificar se o identificador corresponde a um nó da árvore
            res = list(self.nodes[identificador][1].values()) #Adicionar a uma lista os valores do dicionário do nó associado ao identificador
            for i in res: #Iterar número dos nós guardados lista
                res.extend(list(self.nodes[i][1].values())) #Acrescenta os valores obtidos das listas filhas na lista mãe
            return res #Devolve a lista final
        else: return None

def test():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    st.print_tree()
    print(st.nodes_below(7))

test()