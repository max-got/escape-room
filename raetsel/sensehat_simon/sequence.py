import random

class Sequence:
    def __init__(self, symbols): #dict[str, list[list[int]]]):
        self.sequence = []
        self.symbols = symbols
    def generate(self, length):
        for i in range(0, length):
            self.addSymbol()
    def setSequence(self, seq):
        self.sequence = seq
    def getSequence(self):
        return self.sequence
    def getSymbols(self):
        return self.symbols
    def getLength(self):
        return len(self.sequence)
    def getSymbolName(self, index):
        return self.sequence[index]
    def addSymbol(self):
        self.sequence.append(
            random.choice(list(self.symbols.keys()))
        )
    def valuesAsArray(self):
        arr = []
        for i in range(0, len(self.sequence)):
            arr.append(self.symbols[self.sequence[i]])
        return arr
    def clear(self):
        self.sequence = []
