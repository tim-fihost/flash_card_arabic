import tkinter
import pandas
import random
answer = None
BACKGROUND_COLOR = "#B1DDC6"
words = {}
#===========================================================
try:
    data = pandas.read_csv("flash_card\\data\\words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("flash_card\\data\\arabicwords.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

#------------------------Word----------------------------
def random_word():
    global answer, flip_timer
    window.after_cancel(flip_timer)
    answer = random.choice(words)
    print(answer)
    canva.itemconfig(for_second,text=answer["Arabic"],fill="black")
    canva.itemconfig(for_first,text="Arabic",fill="black")
    canva.itemconfig(card_back_ground,image=card_front)
    flip_timer = window.after(3000,func=flip_card)
    #Adding word into csv
    with open("flash_card//data//words_learned.csv","a", encoding="utf8",newline="\n") as word_data:
        word_data.write(answer["English"])
        word_data.write(",")
        word_data.write(answer["Arabic"]+"\n")
        

def flip_card():
    global answer
    canva.itemconfig(for_first,text="English",fill="white")
    canva.itemconfig(for_second,text=answer["English"],fill="white")
    canva.itemconfig(card_back_ground,image=card_back)

def is_known():
    words.remove(answer)
    print(len(words))
    data = pandas.DataFrame(words)
    data.to_csv("flash_card//data//words_to_learn.csv",index=False)
    random_word()

#-------------------------UI-----------------------------
window = tkinter.Tk()
window.title("Arabic")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

card_front = tkinter.PhotoImage(file="flash_card\\images\\card_front.png")
card_back = tkinter.PhotoImage(file="flash_card\\images\\card_back.png")
canva = tkinter.Canvas(width=800,height=530)#426
card_back_ground = canva.create_image(400,265,image = card_front) #IMPORTANT 
canva.config(bg=BACKGROUND_COLOR,highlightthickness=0)



for_first = canva.create_text(400,150,text="Arabic",font=("Arial",40,"italic"))
for_second = canva.create_text(400,265,text="Word",font=("Arial",60,"bold"))
canva.grid(row=0,column=0,columnspan=2)

#Buttons and Images
my_rigt = tkinter.PhotoImage(file="flash_card\\images\\right.png")
button1 = tkinter.Button(image=my_rigt, highlightthickness=0,command=is_known)
button1.grid(row=1,column=1)
my_wrong = tkinter.PhotoImage(file="flash_card\\images\\wrong.png")
button2 = tkinter.Button(window,image=my_wrong,highlightthickness=0,command=flip_card)
button2.grid(row=1,column=0)
random_word()
window.mainloop()