print('Hangman')

from random import randint

fin = open('words.txt')

dic=[line.strip() for line in fin]

def word_generator(level):
    uncommon_letters=['q','j','z','x','v','k','w']
    semicommon_letters=['y','f','b','g','h','m','p']
    word=dic[randint(0,len(dic)-1)]

    if level=='E' or level=='e':
        while len(word)>4:
            word=dic[randint(0,len(dic)-1)]

    elif level=='M' or level=='m':
        while  len(word)<=4:
                word=dic[randint(0,len(dic)-1)]
    else:
        while len(word)<=7:
            word=dic[randint(0,len(dic)-1)]
    return word

def upper_to_lower(x):
    upper_lower={'M': 'm', 'B': 'b', 'X': 'x', 'A': 'a', 'Z': 'z', 'L': 'l', 'T': 't', 'Q': 'q', 'W': 'w',
    'R': 'r', 'V': 'v', 'Y': 'y', 'J': 'j', 'C': 'c', 'E': 'e', 'K': 'k', 'S': 's', 'H': 'h', 'O': 'o',
    'F': 'f', 'I': 'i', 'N': 'n', 'P': 'p', 'U': 'u', 'D': 'd', 'G': 'g'}

    if x in upper_lower:
        return upper_lower[x]
    else:
        return x

def check_letter(x):
    lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
    'y','z']
    if x not in lower_case:
        print('Not a letter')
        return False
    elif x in guessed_letters:
        print('Letter already guessed')
        return False
    return True

def create_blanks(x):
    blank=[]
    n=0
    while n<len(x):
        blank.append('')
        n+=1
    return blank

def fill_blank(letter,word,blank):
    n=0
    while n<len(word):
        if letter==word[n]:
            blank[n]=letter
        n+=1
    return blank

def check_win():
    global blank
    if '' in blank:
        return False
    return True

def check_lose():
    global guesses
    if guesses==0:
        return True
    return False

def hanger():
    global guesses
    if guesses==6:
        print("""                     _______
                    |       |
                            |
                            |
                            |
                            |
                        ____|____""")
    if guesses==5:
        print("""                     _______
                    |       |
                    O       |
                            |
                            |
                            |
                        ____|____""")
    if guesses==4:
        print("""                     _______
                    |       |
                    O       |
                    |       |
                            |
                            |
                        ____|____""")
    if guesses==3:
        print("""                     _______
                    |       |
                    O       |
                   /|       |
                            |
                            |
                        ____|____""")
    if guesses==2:
        print("""                     _______
                    |       |
                    O       |
                   /|\      |
                            |
                            |
                        ____|____""")
    if guesses==1:
        print("""                     _______
                    |       |
                    O       |
                   /|\      |
                   /        |
                            |
                        ____|____""")
    if guesses==0:
        print("""                     _______
                    |       |
                    O       |
                   /|\      |
                   / \      |
                            |
                        ____|____""")

NewGame=str(input("New Game? Y for Yes N for No:"))

while NewGame=='Y' or NewGame=='y':

    Difficulty=str(input("Choose difficulty (E, M, or H):"))

    word=word_generator(Difficulty)

    blank=create_blanks(word)

    guessed_letters=[]

    guesses=6

    def play():
        global guesses
        hanger()
        if check_win():
            print('You win!')
            return 1
        if check_lose():
            print('You lose')
            print(word)
            return 0
        print('Letters guessed: %s' %(guessed_letters))
        print(blank)
        guess=input(str('Choose a letter (or type Guess):'))
        guess=upper_to_lower(guess)
        if guess=='Guess' or guess=='guess':
            guessed_word=input(str('Guess (type lower case):'))
            if guessed_word != word:
                print('You lose')
                print('Word: %s' %word)
                return 0
            else:
                print('You win!')
                return 1
        while not check_letter(guess):
            guess=input(str('Choose a letter:'))
            guess=upper_to_lower(guess)
        if guess in word:
            fill_blank(guess,word,blank)
            guessed_letters.append(guess)
            play()
        else:
            guessed_letters.append(guess)
            guesses-=1
            play()

    play()
    NewGame=str(input("New Game? Y for Yes N for No:"))
