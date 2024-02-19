StackVowel = [""]*100 #string
StackConsonant = [""]*100 #string
global VowelTop #integer
global ConsonantTop #integer
VowelTop = 0 #integer
ConsonantTop = 0 #integer

def PushData(letterin):
    global VowelTop
    global ConsonantTop
    if letterin.lower() == 'a' or 'e' or 'i'or'o' or 'u':
        if VowelTop == 100:
            print("The Vowel Stack is full.")
        else:
            StackVowel.append(letterin)
            VowelTop=+1
    else:
        if  ConsonantTop == 100:
            print("The Consonant Stack is full.")
        else:
            StackConsonant.append(letterin)
            ConsonantTop=+1

def ReadData():
    filename = "StackData.txt"
    try:
        file = open(filename,'r')
        for info in file:
            PushData(info.strip())
        file.close()
    except:
        print("File not found.")


def PopVowel():
    global VowelTop
    if VowelTop-1>=0:
        VowelTop = VowelTop-1
    else:
        
def PopConsonant():
    