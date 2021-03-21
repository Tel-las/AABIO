class SuffixTree:

    def __init__(self):
        self.nodes = {0: (-1, {})}  # root node
        self.num = 0

    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print(k, "->", self.nodes[k][1])
            else:
                print(k, ":", self.nodes[k][0])

    def add_node(self, origin, symbol, leafnum=-1):
        self.num += 1  # Incrementa o número do node
        self.nodes[origin][1][
            symbol] = self.num  # Acede ao dicionário do tuplo do nó e atribui ao nucleótido o nº do node
        self.nodes[self.num] = (leafnum, {})  # Criar o tuplo onde se guardam as próximas posições

    def add_suffix(self, p, sufnum):  # padrão e posição no padrão
        pos = 0
        node = 0
        while pos < len(p):  # Enquanto a posição for inferior ao tamanho do padrão
            # Se a letra na posição pos da seq p não estiver no node/ o [1] vai buscar o dicionário dentro do tuplo
            if p[pos] not in self.nodes[node][1].keys():
                if pos == len(p) - 1:  # Se estiver no último caracter da sequência (se for o dollar)
                    self.add_node(node, p[pos], sufnum)  # Adicona o node final; argumentação leafnum != -1
                else:
                    self.add_node(node, p[pos])  # Adiciona o node
            node = self.nodes[node][1][p[pos]]  # Dizer o nó onde estamos
            pos += 1  # Incrementa a posição

    def suffix_tree_from_seq(self, text):
        t = text + "$"  # Adiciona dollar no final da sequencia
        for i in range(len(t)):  # Para o range da sequencia mais o dolar
            # Passa texto iniciando de uma posição inicial i (iterada no range) e a posição como argumentos a função add_
            self.add_suffix(t[i:], i)

    # Utilizar a suffix tree para encontrar padrões

    def find_pattern(self, pattern):
        node = 0
        for pos in range(len(pattern)):  # Iterar a posição no padrão
            if pattern[pos] in self.nodes[node][1].keys():  # Se a letra estiver nas letras do dicionário
                node = self.nodes[node][1][
                    pattern[pos]]  # Define o node pela posição associada ao nucleótido no dicionário do node 0
            else:
                return None
        return self.get_leafes_below(node)  # Passa o nó para a função get_leafes_below

    def get_leafes_below(self, node):
        res = []  # Abre a lista com as resoluções
        if self.nodes[node][0] >= 0:  # Se o nó for diferente de -1 - é p final da árvore
            res.append(self.nodes[node][0])  # Guarda a posição do node
        else:  # Se o nó for -1 - ou seja é um elemento do ramo
            for k in self.nodes[node][1].keys():  # Iterar as chaves dos dicionários (nucleótidos)
                newnode = self.nodes[node][1][k]  # Abre um novo nó
                leafes = self.get_leafes_below(newnode)  # Recorre a função utilizando o novo nó
                res.extend(leafes)  # Concatenar a lista à resolução
        return res  # Devolve os resultados


    def get_sequence(self, node, nextnodes):
        """
        Resolução Exercício 1_b
        Dar retrieve a todas as sequencias possíveis a partir de um dado node de forma recursiva
        """
        string = ''
        for nextnode in nextnodes:
            for k, v in self.nodes[node][1].items():
                if v == nextnode:
                    string += k # Adicionar o nt à string
            node = nextnode #Avançar para o próximo nó
            nextnodes = self.nodes[node][1].values() #Ir buscar o novo conjunto de values
            res = self.get_sequence(node, nextnodes)
            string += res
        return string


    def matches_prefix(self, prefix):
        """
        Resolução Exercício 1_b
        Fornece os nodes iniciais dos padrões, obtidos a partir do método find_pattern, ao método get_sequence e filtra
        o resultado deste método até obter as substrings pretendidas
        """
        lista_1 = []
        lista_2 = []
        lista_3 = []
        match = self.find_pattern(prefix)
        if match is None:
            return None
        else:
            for node in range(len(match)):
                nextnodes = self.nodes[match[node]][1].values()
                lista_1.append(self.get_sequence(node, nextnodes)) #Lista Raw
                for string in lista_1: #Partir strings pelo sinal '$'
                    lista_2.extend(string.split('$'))
            for string in lista_2: #Lista splitted
                    j = len(prefix)
                    if len(string) >= j and string[0:j] == prefix:
                        lista_3.append(string)
            for string in lista_3: #Lista filtrada pelo tamanho e composição do prefixo
                n = len(string)
                while n >= len(prefix): #Decrementar sequencias completas para obter todas as combinações possíveis
                    lista_3.append(string[:n])
                    n -= 1
                lista_3 = list(dict.fromkeys(lista_3))
            return lista_3

def test():
    seq = "TACTAGHF"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    st.print_tree()
    print(st.find_pattern("TA"))
    print(st.matches_prefix('TA'))

test()




