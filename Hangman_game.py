from glob import escape
import random
import os
import msvcrt

#in this part I define the function read. 
#It extracts the data from the "data.txt" file and put it in a list in the correct format.
def read():
    words = []
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f: 
            line = line.replace('\n',"")
            size = len(line)
            if size > 3:
                line.lower()
                words.append(line)
    return words


#fuction made for fixing the input of letters in the game
def try_letter(letter):
    try:
        if (len(letter) > 1 or len(letter) == 0) or not letter.isalpha():
            raise ValueError("you must enter only one letter")
        return letter
    except ValueError as ve:
        os.system("cls")
        print(ve)
        return False


#function of menu after winning/losing
#it returns the variable necesary to break the while cycle
def decide():
    cicle = 1
    print("""DO YOU WANT TO PLAY AGAIN?
        1.Yes
        2.No""")
    while cicle == 1:
        rematch = input()
        if rematch == "1":
            rematch = True
            cicle = 0
        elif rematch == "2":
            rematch = False
            cicle = 0
        os.system("cls")
        print("Select a correct option:")
    return rematch


hangman_draw1 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x
        x   x
        x  x
        x x
        xx
        x
        x
        x
        x
        x
        x
        x
        x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw2 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx
        x
        x
        x
        x
        x
        x
        x
        x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw3 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx                           x
        x                            x
        x                            x
        x                            x
        x                            x
        x                            x
        x
        x
        x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw4 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx                           x
        x                            x
        x                            x
        x                            x
        x                            x
        x                            x
        x                           x
        x                          x
        x                         x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw5 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx                           x
        x                            x
        x                            x
        x                            x
        x                            x
        x                            x
        x                           x x
        x                          x   x
        x                         x     x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw6 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx                           x
        x                            xx
        x                            x x
        x                            x  x
        x                            x   x
        x                            x
        x                           x x
        x                          x   x
        x                         x     x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


hangman_draw7 = """\       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x       x                    x
        x      x                     x
        x     x                      x
        x    x                     xxxxx
        x   x                      xxxxx
        x  x                       xxxxx
        x x                        xxxxx
        xx                           x
        x   x   xxxxxxxxxxxxxxx     xxx
        x   x   x  xx       x      x x x
        x   x   x  xxxxxx   x     x  x  x
        x   x   x  x    x   x    x   x   x
        x   xxxxxxxxxxxxx   x        x
        x                           x x
        x                          x   x
        x                         x     x
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x   x                                      xx
   x    x                                     x x
  x                                          x  x
 x                                          x   x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    x
x  x x  xxx  x   x  xxx   x   x  xxx  x   xx    x
x  x x x   x xx  x x      xx xx xx  x xx  xx   x
x  xxx xxxxx x x x x xxx  x x x xxxxx x x xx  x
x  x x x   x x  xx x   x  x   x x   x x  xxx x
x  x xxx   xxx   x  xxx   x   x x   xxx   xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""


#in this part I define the function game. 
#It runs the game from the base.
def game(words):
    rematch = True
    while rematch == True:
#random word selection
        lwords = len(words)
        n = random.randint(0,lwords)
        rword = words[n]
        lword = len(rword)
#defining lists for the game
        os.system("cls")
        letters = []
        hword = []
        letters_missed = []
#stands for dead count
        dc = 0
        for i in range(0, lword):
            hword.append('_')
        print(hword) 
        print(hangman_draw1)
        while dc < 6:
            print("Enter a letter: ")
            letter = input()
            if try_letter(letter) != False:
                os.system("cls")
                letters.append(letter)
                lletters = len(letters)
                unknown_letters = 0
                for i in range(0, lword):
                    if hword[i] == '_':
                        unknown_letters = unknown_letters + 1
                for i in range(0, lword):
                    for j in range(0, lletters):
                        if hword[i] != '_':
                            break
                        if rword[i] == letters[j]:
                            hword[i] = letters[j]
                        else:
                            hword[i] = '_'
                unknown_letters2 = 0
                a = len(letters)
                a = a - 1
                b = 0
                for i in range(0, lword):
                    if hword[i] == '_':
                        unknown_letters2 = unknown_letters2 + 1
                    if hword[i] == letters[a]:
                        b = 1
                if unknown_letters2 == 0:
                    print("CONGRATULATIONS, YOU WON!!!")
                    rematch = decide()
                    break
                if unknown_letters == unknown_letters2:
                    dc = dc + 1
                if b == 0:
                    letters_missed.append(letters[a])
            print("WORD: ")
            print(hword)
            print("\n")
            print("LETTERS MISSED: ")
            print(letters_missed)
            print("\n")
            if dc == 0:
                print(hangman_draw1)
            elif dc == 1:
                print(hangman_draw2)
            elif dc == 2:
                print(hangman_draw3)
            elif dc == 3:
                print(hangman_draw4)
            elif dc == 4:
                print(hangman_draw5)
            elif dc == 5:
                print(hangman_draw6)
            elif dc == 6:
                print(hangman_draw7)
        if rematch != False:
            print("you just lost")
            rematch = decide()

def run():
#in this part I extract from the data file the list and put it in a list
    words = read()
    option = 0
    print("""Select one opction:
1. Play.
2. Quit.
""")
    while option != 2:
        os.system("cls")
        option = int(input("""Select one option:
1. Play.
2. Quit.
Selection: """))
        if option == 1:
            game(words)
        elif option ==2:
            break
        elif option != 1 and option != 2:
            print("You must select a valid option: ")


    

if __name__ == '__main__':
    run()