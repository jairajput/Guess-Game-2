import random as rmd

def wowcorrect(c,lctn,word):
    pos=0
    wrd1=[]
    finded=[]
    wrd1[:0]=word
    finded[:0]=lctn
    for i in wrd1:
        if i==c:
            finded[pos]=c
        pos+=1
    tillguessed=''.join(finded)
    return tillguessed  
    

def checkenterprevious(c,checking):
    count=0
    for i in checking:
        if c==i:
            count+=1
    if count>1:
        return False
    else:
        return True


def guess_word(word):
    turnleft=len(word)
    ans=False
    won=0
    a=['*'] * len(word)
    guessing=''.join(a)
    wrd=[]
    wrd[:0]=word
    wrongguess=[]
    print("Hey there! Whatsup\nTry to find the word\nA hint for you since you are my wellwisher\nEven the creator doesn't know the word")
    print("You Have ",len(word)," Turn to find the word")
    print("word is ",''.join(a)," its length is ",len(word))
    while turnleft>0:
        ans=False
        print("You have ",turnleft,"attempts left")
        char=input("Enter a letter(IN LOWERCASE): ")
        wrongguess.append(char)
        for i in wrd:
            if char==i:
                ans=True
        if ans==True:
            print("Correct...")
            guessing=wowcorrect(char,guessing,word)
            print(guessing)
        else:
            print("Previous guess: ",char)
            print("Try again...")
            print(guessing)
            find=checkenterprevious(char,wrongguess)
            if find==True:
                turnleft-=1
        if guessing==word:
            turnleft=0
            won=1
    if won==1:
        print("Word is ",word)
        print("Congratulations! you got the word")
        print("Let's have some party in the house")
    else:
        print("Word is ",word)
        print("You played well, better luck next time")


    
words=["blood","queen","oxide","eared","gable","macaw","peace","acute","event","blame","faith","chief","error","light","month","pilot","phase","radio","ratio","route","rugby","scale","share","shape","spite","speed","steam","store","trust","union","youth"]
findout=rmd.choice(words)
guess_word(findout)