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


#in this part I define the function game. 
#It runs the game from the base.
def game():
    pass


def run():
#in this part I extract from the data file the list and put it in a list
    words = read()
    game(words)

if __name__ == '__main__':
    run()