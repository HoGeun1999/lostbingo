from gettext import find
from itertools import count
from sre_parse import State
import tkinter
from tkinter.constants import COMMAND
from typing import Text
window=tkinter.Tk()
window.title("lostbingo")
window.geometry("1200x650+200+100")

canvas = tkinter.Canvas(width=400,height=400,bg="white")
canvas.pack()
x_bingo = []
y_bingo = []
check_bnt = []
dic = {}
count = 0
points = [0,200,200,400,400,200,200,0]
canvas.create_polygon(points,outline="black",fill="white",width=2)
for x in range(5):
    for y in range(5):
        small_points = [160-40*y+40*x,40+40*y+40*x,200-40*y+40*x,80+40*y+40*x,240-40*y+40*x,40+40*y+40*x,200-40*y+40*x,0+40*y+40*x]
        canvas.create_polygon(small_points,outline="black",fill="white",width=2)
def find_index(x,y):
    for i in range(len(check_bnt)):
        if check_bnt[i][0] == x and check_bnt[i][1] == y:
                print(i)
                return i

def drow_oval(x,y):
    def drow_oval_2():
        x_bingo_count = 0
        y_bingo_count = 0
        global count
        if count < 2:
            button1 = dic[(x,y)]
            button1["state"] = 'disabled'
            count = count + 1
            canvas.create_oval(170-40*y+40*x,15+40*y+40*x,230-40*y+40*x,65+40*y+40*x,outline='blue',width='2')
            check_bnt.append([x+1,y+1])
            if count == 2:
                button1 = dic[(check_bnt[0][0]-1,check_bnt[0][1]-1)]
                button1["state"] = 'normal'
                button1 = dic[(check_bnt[1][0]-1,check_bnt[1][1]-1)]
                button1["state"] = tkinter.NORMAL
            return
        print(x_bingo)
        if [x+1,y+1] in check_bnt:
            canvas.create_oval(170-40*y+40*x,15+40*y+40*x,230-40*y+40*x,65+40*y+40*x,outline='white',width='2')  #(170,15,230,65) == 1,1 에 그리는 원좌표
            check_bnt.pop(find_index(x+1,y+1))
        else:
            canvas.create_oval(170-40*y+40*x,15+40*y+40*x,230-40*y+40*x,65+40*y+40*x,outline='blue',width='2')
            check_bnt.append([x+1,y+1])
        if x-1>=0:
            print(x+1,y+1)
            if y+1 in x_bingo:
                return
            if [x,y+1] in check_bnt:
                canvas.create_oval(170-40*y+40*(x-1),15+40*y+40*(x-1),230-40*y+40*(x-1),65+40*y+40*(x-1),outline='white',width='2')
                check_bnt.pop(find_index(x,y+1))
            else:
                canvas.create_oval(170-40*y+40*(x-1),15+40*y+40*(x-1),230-40*y+40*(x-1),65+40*y+40*(x-1),outline='blue',width='2')
                check_bnt.append([x,y+1])
        if x+1<5:
            if y+1 in x_bingo:
                return
            if [x+2,y+1] in check_bnt:
                canvas.create_oval(170-40*y+40*(x+1),15+40*y+40*(x+1),230-40*y+40*(x+1),65+40*y+40*(x+1),outline='white',width='2')
                check_bnt.pop(find_index(x+2,y+1))
            else:
                canvas.create_oval(170-40*y+40*(x+1),15+40*y+40*(x+1),230-40*y+40*(x+1),65+40*y+40*(x+1),outline='blue',width='2')
                check_bnt.append([x+2,y+1])
        if y-1>=0:
            if y+1 in x_bingo:
                return
            if [x+1,y] in check_bnt:
                canvas.create_oval(170-40*(y-1)+40*x,15+40*(y-1)+40*x,230-40*(y-1)+40*x,65+40*(y-1)+40*x,outline='white',width='2')
                check_bnt.pop(find_index(x+1,y))
            else:
                canvas.create_oval(170-40*(y-1)+40*x,15+40*(y-1)+40*x,230-40*(y-1)+40*x,65+40*(y-1)+40*x,outline='blue',width='2')
                check_bnt.append([x+1,y])
        if y+1<5:
            if y+1 in x_bingo:
                return
            if [x+1,y+2] in check_bnt:
                canvas.create_oval(170-40*(y+1)+40*x,15+40*(y+1)+40*x,230-40*(y+1)+40*x,65+40*(y+1)+40*x,outline='white',width='2')
                check_bnt.pop(find_index(x+1,y+2))
            else:
                canvas.create_oval(170-40*(y+1)+40*x,15+40*(y+1)+40*x,230-40*(y+1)+40*x,65+40*(y+1)+40*x,outline='blue',width='2')
                check_bnt.append([x+1,y+2])
        for i in range(1,6):        
            x_bingo_count = 0
            for j in range(len(check_bnt)):
                if check_bnt[j][1] == i:
                    x_bingo_count = x_bingo_count + 1
            if x_bingo_count == 5:
                if i not in x_bingo:
                    x_bingo.append(i)
                    for k in range(5):
                        canvas.create_oval(170-40*y+40*k,15+40*y+40*k,230-40*y+40*k,65+40*y+40*k,outline='red',width='2')
                else:
                    pass
        # for i in range(1,6):        
        #     y_bingo_count = 0
        #     for j in range(len(check_bnt)):
        #         if check_bnt[j][0] == i:
        #             y_bingo_count = y_bingo_count + 1
        #     if y_bingo_count == 5:
        #         for k in range(5):
        #             print(101)
        #             canvas.create_oval(170-40*y+40*x,15+40*y+40*x,230-40*y+40*x,65+40*y+40*x,outline='red',width='2')
                
        
    return drow_oval_2


for x in range(5):
    for y in range(5):
        f = drow_oval(x,y)
        button1 = tkinter.Button(window,command = drow_oval(x,y),text = "%d,%d"%(x+1,y+1),width='3')
        dic[(x,y)] = button1
        button1_window = canvas.create_window(200-40*y+40*x,40+40*y+40*x,window=button1)


window.mainloop()