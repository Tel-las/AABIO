# -*- coding: utf-8 -*-

class Trie:
    
    def __init__(self):
        self.nodes = { 0:{} } # dictionary
        self.num = 0

#Construir a trie

    def print_trie(self): #Imprimir nós e posições
        for k in self.nodes.keys():
            print (k, "->" , self.nodes[k]) 
    
    def add_node(self, origin, symbol): #Parametros são o node onde começamos e o símbolo ("nucleótido") cujo arco queremos adicionar, ou caso exista verificar
        self.num += 1 #Contador do número de nós
        self.nodes[origin][symbol] = self.num #Indexa ao valor dicionário dentro do value do 1º dicionário
        self.nodes[self.num] = {} #Abre o dicionário de um nove key(node)
    
    def add_pattern(self, p):
        pos = 0
        node = 0
        while pos < len(p): #Enquanto que a posição (iterador) for menor que o tamanho do padrão
            if p[pos] not in self.nodes[node].keys(): # p[pos] corresponde a uma base ATGC/Verifica a presença do "nucleótido" no node que está a ser ieradp
                self.add_node(node, p[pos]) #Se não estiver presente na árvore é adicionado
            node = self.nodes[node][p[pos]]  #Define valor do nó onde estamos na árvore
            pos += 1 #Avançamos na posição do padrão

            
    def trie_from_patterns(self, pats): #Itera os padrões pela função add_pattern
        for p in pats:
            self.add_pattern(p)

#Funções para encontrar padrões numa sequência
            
    def prefix_trie_match(self, text):
        pos = 0 #Contador da posição no texto
        match = "" #String que devolve o padrão encontrado
        node = 0 #Contador do nó
        while pos < len(text):
            if text[pos] in self.nodes[node].keys(): #Verifica se a base está na árvore
                node = self.nodes[node][text[pos]] #Guardo o nó em que a base está (value do 2º dicionário)
                match += text[pos] #Adiciona ao match (padrão)
                if self.nodes[node] == {}: return match #Atingir uma folha da árvore
                else: pos += 1 #Incrementar a posição para continuar a pesquisar o texto
            else: return None #Quando o nucleótido não estiver na trie, interrompe o ciclo e devolve None
        return None #Em caso de má argumentação devolve None
        
    def trie_matches(self, text):
        res = []
        for i in range(len(text)): #Iteração para cada uma das caracteres da string text (posições iniciais)
            m = self.prefix_trie_match(text[i:]) #Fornece o argumento da posição inicial i no texto e guarda o match correspondente
            if m is not None: res.append((i,m)) #Se ouver padrões indexar a res um tuplo com a posição inicial e o padrão
        return res #Devolve a lista com os matches (tuplos)

def test():
    patterns = ["GAT", "CCT", "GAG"]
    t = Trie() #Inicializar a classe
    t.trie_from_patterns(patterns)
    t.print_trie()

def test2():
    patterns = ["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"]
    t = Trie() #Inicializar a classe
    t.trie_from_patterns(patterns) #Gerar árvore a partir dos padrões
    print (t.prefix_trie_match("GAGATCCTA")) #Testar padrão 1ª posição
    print (t.trie_matches("GAGATCCTA")) #Testar padrões em todas as posições iniciais
    
test()
print()
test2()
