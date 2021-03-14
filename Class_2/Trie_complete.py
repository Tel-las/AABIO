# -*- coding: utf-8 -*-

class Trie:
    
    def __init__(self):
        self.nodes = { 0:{} } # dictionary
        self.num = 0
    
    def print_trie(self):
        for k in self.nodes.keys():
            print (k, "->" , self.nodes[k]) 
    
    def add_node(self, origin, symbol):
        self.num += 1
        self.nodes[origin][symbol] = self.num #Indexa ao valor do dicionário dentro do value do 1º dicionário
        self.nodes[self.num] = {}
    
    def add_pattern(self, p):
        pos = 0
        node = 0
        while pos < len(p):
            if p[pos] not in self.nodes[node].keys(): # p[pos] corresponde a uma base ATGC
                self.add_node(node, p[pos])
            node = self.nodes[node][p[pos]]
            pos += 1

            
    def trie_from_patterns(self, pats):
        for p in pats:
            self.add_pattern(p)
            
    def prefix_trie_match(self, text):
        pos = 0
        match = ""
        node = 0
        while pos < len(text):
            if text[pos] in self.nodes[node].keys(): #Verifica se a base está na árvore
                node = self.nodes[node][text[pos]] #Guardo o nó em que a base está (value do 2º dicionário)
                match += text[pos] #Adiciona ao padrão
                if self.nodes[node] == {}: return match #Atingir uma folha da árvore
                else: pos += 1 #Incrementar a posição para continuar a pesquisar o testo
            else: return None
        return None
        
    def trie_matches(self, text):
        res = []
        for i in range(len(text)):
            m = self.prefix_trie_match(text[i:]) #Iterar o texto começando em todas as possíveis posições iniciais
            if m is not None: res.append((i,m)) #Se ouver padrões indexar a res um tuplo com a posição inicial e o padrão
        return res

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
