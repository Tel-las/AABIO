# -*- coding: utf-8 -*-


class Automata:
    """

    Construir tabela em que vamos ter um dicionario da sequencia em que os matches são contruidos.


    """
    def __init__(self, alphabet, pattern):
        self.numstates = len(pattern) + 1
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)
    
    def buildTransitionTable(self, pattern):
        """
        Tabela de transição é implementada como um dicionário, em que as chaves são tuplos (estado anterior, símbolo) e
        os valores representam o próximo estado
        """
        for q in range(self.numstates):
            for a in self.alphabet:
                prefix = pattern[0:q] + a
                self.transitionTable[(q,a)] = overlap(prefix, pattern)
       
    def printAutomata(self):
        print ("States: " , self.numstates)
        print ("Alphabet: " , self.alphabet)
        print ("Transition table:")
        for k in self.transitionTable.keys():
            print (k[0], ",", k[1], " -> ", self.transitionTable[k])
         
    def nextState(self, current, symbol):
        return self.transitionTable.get((current, symbol))

    def applySeq(self, seq):
        """
    Computa a lista de estados que o algoritmo avança ao processar a sequencia
        """
        q = 0
        res = [q]
        for c in seq:
            q = self.nextState(q, c)
            res.append(q)
        return res
        
    def occurencesPattern(self, text):
        """
        Providencia a lista das posições do padrão na sequência

        """
        q = 0 
        res = []
        #self.applySeq(text).index(self.numstates)
        for i in range(len(text)):
            q = self.nextState(q, text[i])
            if q == self.numstates - 1: #Após encontrar uma ocorrência é necessário encontrar a posição inicial subtraindo o tamanho do padrão
                res.append(i - self.numstates + 2)
        return res

def overlap(s1, s2):
    """
   Provides the  maximum overlap between the two sequences
    """
    maxov = min(len(s1), len(s2))
    for i in range(maxov,0,-1):
        if s1[-i:] == s2[:i]: return i
    return 0
               
def test():
    auto = Automata("AC", "ACA")
    auto.printAutomata()
    print (auto.applySeq("CACAACAA"))
    print (auto.occurencesPattern("CACAACAA"))

test()

#States:  4
#Alphabet:  AC
#Transition table:
#0 , A  ->  1
#0 , C  ->  0
#1 , A  ->  1
#1 , C  ->  2
#2 , A  ->  3
#2 , C  ->  0
#3 , A  ->  1
#3 , C  ->  2
#[0, 0, 1, 2, 3, 1, 2, 3, 1]
#[1, 4]



