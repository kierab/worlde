from tkinter import *
import time
import random


root = Tk();
root.resizable(False,False)
root.title('worlde 👌')

WORDLIST = []
TESTWORD = "tiles"
# global position
position = 0
guessword = ""

# game functions
def generate_word():
    # get big dict or something of 5 letter words
    pass

def newgame():
    # also generate a new word
    global position
    word_guess.delete(0, len(word_guess.get()))
    position = 0
    status['text'] = "hi"
    reset_btn.config(bg='#f0f0f0')
    for i in range(6):
        for j in range(5):
            tiles[i][j]['text'] = ""
            tiles[i][j].config(bg="#f0f0f0")
    print(f"answer = {TESTWORD}")

def send_word():
    #test
    guess = word_guess.get()
    if len(guess.strip().lower()) != 5 : word_guess.delete(0,len(guess))
    else:
        word_guess.delete(0, len(guess))
        guess = guess.strip().lower()
        print(guess)
        i = 0
        global position
        global guessword
        guessword = guess

        for c in guess:
            tiles[position][i]['text'] = c
            i += 1
        check_word()
        position+=1
        print(position)
        if position == 6:
            status['text'] = f"gameover, word was: {TESTWORD}"
            reset_btn.config(bg='#ed766d')


def check_word():
    # iterate thru letters in the string? idk
    global guessword
    global position

    tmp = list(guessword)
    tmp2 = list(TESTWORD)

    #check if in word
    for i in range(len(tmp2)):
        if guessword[i] not in tmp2:
                tiles[position][i].config(bg="#858585")

    for i in range(len(guessword)):
        if guessword[i] == tmp2[i]:
            tiles[position][i].config(bg="#66e362")
            tmp2[tmp2.index(guessword[i])] = '#'
            print(tmp2)

    for i in range(len(tmp2)):
        if guessword[i] in tmp2:
                tiles[position][i].config(bg="#e3d462")
                tmp2[tmp2.index(guessword[i])] = '#'

    for i in tiles[position]:
        if i['bg'] == "SystemButtonFace":
            i.config(bg="#858585")



        # else:
        #     tiles[position][i].config(bg="#858585")


    # #check if in correct location
    # for i in range(len(guessword)):
    #     if guessword[i] == TESTWORD[i]:
    #         tiles[position][i].config(bg="#66e362")
    #
            # tmp = list(guessword)
            # tmp[i] = '$'
            # guessword = "".join(tmp)



    if guessword == TESTWORD:
        status['text'] = 'CONGRATS BEAST 🤬😎💯🥰♥'
        reset_btn.config(bg='#ed766d')



tiles = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

heading = Label(text="worlde 👌💪", font=("Helvetica",30))
heading.pack(side="top")

reset_btn = Button(text="reset", font=("Helvetica",15),command=newgame)
reset_btn.pack()

status = Label(text="hi", font=("Helvetica",15))
status.pack(pady=2)

tileframe = Frame(root) # letter tiles
tileframe.pack(padx=15)

for row in range(6):
    for col in range(5):
        tiles[row][col] = Button(tileframe,text="",font=("Helvetica",15),width=5,height=2)
        tiles[row][col].grid(row=row,column=col)


enterframe = Frame(root)
enterframe.pack(pady=10)
word_guess = Entry(enterframe,width=10,font=("Helvetica",15),borderwidth=5)
word_guess.pack(side=LEFT)
enter_btn = Button(enterframe,text="enter",command=send_word,font=("Helvetica",15))
enter_btn.pack(side=RIGHT)





root.mainloop()