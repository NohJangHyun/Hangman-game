# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(" ")

    print (len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


print(">>>")
print("Welcome to the game, Hangman!")
randomword=str(choose_word(wordlist))
print("I am thinking of a word that is",len(randomword),"letters long.")
print("------------")

Chance = 8 
Alphabet="abcdefghijklmnopqrstuvwxyz"
x=[]

print("You have",Chance ,"guesses left.")
print("Available letters:", Alphabet)
Attempt=str(input("Please guess a letter: " ))
Attempts=Attempt.strip()
attempt=Attempts.lower() 
x.append(attempt)
if attempt in Alphabet: 
    ans=Alphabet.find(attempt) 
    alphabet=str(Alphabet[:ans]+Alphabet[ans+1:]) 
if attempt not in Alphabet: 
    alphabet=Alphabet

answer=""
for i in randomword:
    if i in attempt:
        answer += i
    else:
        answer = answer+"_"
if attempt in randomword:
    print("Good guess:", answer)
else:
    print("Oops! That letter is not in my word:", answer)
    Chance-=1
print("------------")

if(answer!=randomword):    
    while(Chance!=0):
        print("You have",Chance ,"guesses left.")
        print("Available letters:", alphabet)    
        Attempt=str(input("Please guess a letter: "))
        Attempts=Attempt.strip()
        attempt=Attempts.lower()
        x.append(attempt)
        if attempt in alphabet:
            ans=alphabet.find(attempt)
            alphabet=str(alphabet[:ans]+alphabet[ans+1:])
        
        answer=""
        for i in randomword:
            if i in x:
                answer += i
            else:
                answer = answer+"_"
        if attempt in randomword:
            print("Good guess:", answer)
        else:
            print("Oops! That letter is not in my word:", answer)
            Chance-=1
        print("------------")

if(answer==randomword):
    print("Congratulations, you won!")
else:
    print("Answer was",randomword,"you lose!")