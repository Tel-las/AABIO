# -*- coding: utf-8 -*-

class BoyerMoore:
    
    def __init__(self, alphabet, pattern):
        self.alphabet = alphabet
        self.pattern = pattern
        self.preprocess()

    def preprocess(self):
        self.process_bcr()
        self.process_gsr()
        
    def process_bcr(self):
        """
        Implementação do pré-processamento da bad-character rule
        Avançamos no padrão para a próxima ocorrencia do simbolo na sequencia na posição do mismatch.
        Se nenhuma ocorrencia daquele símbolo existir no padrão, avançamos até ao final do padrão

        Criamos um dicioário com todos os símbolos possíveis como chaves , com os valores definindo a posição mais
        à direita onde o símbolo ocorre no padrão (-1 no caso de não ocorrer)
        """
        self.occ = {c: -1 for c in self.alphabet}
        for i in range(len(self.pattern)):
            c = self.pattern[i]
            self.occ[c] = i

    def process_gsr(self):
        """
        Implementação do pré-processamento do good suffix rule
        Em caso de um mismatch, avançamos para a próxima instancia no padrão da parte (sufixo) que deu match depois
        (a direira) do mismatch
        Cria uma lista que guarda o número de posições que podem ser avançadas, dependendo da posição do mismatch no padrão.

        """
        self.f = [0] * (len(self.pattern) + 1)
        self.s = [0] * (len(self.pattern) + 1)
        i = len(self.pattern)
        j = len(self.pattern) + 1
        self.f[i] = j

        while i > 0:
            while j <= len(self.pattern) and self.pattern[i-1] != self.pattern[j-1]:
                if self.s[j] == 0:
                    self.s[j] = j-i
                j = self.f[j]

            i -= 1 #Decrementação dos contadores
            j -= 1

            self.f[i] = j

        j = self.f[0]

        for i in range(len(self.pattern)):
            if self.s[i] == 0: self.s[i] = j
            if i==j : j =self.f[j]

    def search_pattern(self, text):
        """
        Permite o uso de um objeto inicializado da classe BoyerMoore para pesquisar as sequencias alvo pelo padrão fornecido.
        Utiliza as estruturas resultantes do pré-processamento, usando as duas regras para avançar para o número máximo de posições permitidas.

        """
        res = []
        i = 0 #1º contador
        while i <= (len(text) - len(self.pattern)):
            j = len(self.pattern) - 1 #Inicialização do 2º contador
            while j >= 0 and self.pattern[j] == text[j+i]:
                j = j - 1 #2º contador

            if j < 0:
                res.append(i)
                i += self.s[0] #caso j seja negativo
            else:
                c = text[j + 1]
                i += max(self.s[j+1], j-self.occ[c]) #Aplicar as regras
        return res  #Devovler a solução

def teste():
    bm = BoyerMoore("ACTG", "ACCA")
    print (bm.search_pattern("ATAGAACCAATGAACCATGATGAACCATGGATACCCAACCACC"))

teste()

# result: [5, 13, 23, 37]
            
