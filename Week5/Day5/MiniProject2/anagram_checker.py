from turtle import isvisible

class AnagramChecker():
    def __init__(self) -> None:
        self.list = list()
        with open(direction, mode='r') as myFile:
            self.text = myFile.read().lower()
        for line in open(direction, mode='r'):
            self.list.append(line[:-1].lower())
        # print(self.text)
        # print(type(self.text))
        # print(self.list)

    def isValidWord(self, word: str) -> bool:
        word = word.lower()
        if word in self.list:
            # print(word, 'is a valid english word')
            return True
        else:
            # print(word, 'is not a valid english word')
            return False
    
    def getAnagrams(self, word: str) -> list:
        word = word.lower()
        sameLength = list()
        wordList = list()
        newList = list()
        anagramList = list()
        for i in word:
            wordList.append(i)
        for i in self.list:
            if len(i) == len(word):
                sameLength.append(i)
        for i in sameLength:
            newList = list()
            for j in i:
                newList.append(j)
            if sorted(newList) == sorted(wordList):
                anagramList.append(i)
        anagramList.remove(word)
        # print('Anagrams are:',anagramList)
        return anagramList


# a1 = AnagramChecker(direction=r'C:\Users\Acca\Desktop\DI-Bootcamp\Week-5\day-5\mini-project-2\sowpods.txt')
# a1.getAnagrams('meat')


            