from tkinter import messagebox
# load the database
global wordList
wordList = []

global letters
letters = 'abcdefghijklmnopqrstuvwxyz'


def replaceEnd(item):
    return item.replace('\n', '')


def lowercaseEnd(item):
    return item.lower()


def load_wordList_Data():
    getWords = []
    for i in letters:
        with open(f"asset/{i}.txt", mode='r') as loadFile:
            getWords.append(loadFile.readlines())
        wordList.append(getWords[letters.index(i)])


def fixingData(strx):
    for i in range(len(wordList)):
        wordList[i] = list(map(replaceEnd, wordList[i]))
        wordList[i] = list(map(lowercaseEnd, wordList[i]))
    getCharIndex = list({letters.index(x) for x in strx})
    return getCharIndex


def getData(strx):
    indexToFollow = fixingData(strx)
    anagramReturn = []
    for i in indexToFollow:
        for j in range(len(wordList[i])):
            myShuffledText = [x for x in strx]
            getWord = [y for y in wordList[i][j]]
            isAnagram = True
            for k in getWord:
                if k in myShuffledText:
                    myShuffledText.remove(k)
                else:
                    isAnagram = False
            if(isAnagram):
                anagramReturn.append(wordList[i][j])
    return anagramReturn

def useAnagram(text):
    try:
       listOfAnagram = getData(text)
       listOfAnagram.sort(key=len,reverse=True)
       return listOfAnagram
    except:
        messagebox.showwarning("No Special Characters are Allowed")

load_wordList_Data()