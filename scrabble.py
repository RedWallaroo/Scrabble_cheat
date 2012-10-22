import sys
import pdb
from operator import itemgetter,attrgetter


def isRackInDictionary(srack,word):
   
   
    for x in range (len(word)):

        if word[x] in srack:
           srack.remove(word[x])
        
        else:
            return False
    return True

def getScore(validword):

    total_Score = 0

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

    for letter in range(len(validword)):
        letter_Score = scores[validword[letter]]
        total_Score += letter_Score
    
    return total_Score    

def printFinalList(sortedlist):
    for t in sortedlist:
        print t[1] + " " + t[0]



def scrabble(srack):

    
    wordfilename = "/users/sandralombardi/downloads/sowpods.txt"
    file = open(wordfilename, 'r')
    dlist = file.readlines()
    srack = srack.lower()

    dlist =[x.lower() for x in dlist]
    
    tempResultList = []
    
    for x in range(len(dlist)):

        dlist[x] = dlist[x].strip()
        temprack = list(srack)
        if isRackInDictionary(temprack,dlist[x]):
            total_Score = getScore(dlist[x])
            tempResultList.append((dlist[x],str(total_Score)))
            
    sortedlist = sorted(tempResultList, key= itemgetter(1), reverse = True)
    printFinalList(sortedlist)
    
    

if len(sys.argv) > 1:
    srack = sys.argv[1]
else:
    srack = "AEFGREE"

scrabble(srack)