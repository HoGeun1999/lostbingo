import tkinter

window=tkinter.Tk()
window.title("lostbingo")
window.geometry("1200x650+200+100")

canvas = tkinter.Canvas(width=500,height=600,bg="white")
canvas.pack()
for y in range(5):
    for x in range(5):
        canvas.create_rectangle(x*100,y*100,x*100+100,y*100+100)

button = tkinter.Button(window, overrelief="solid", width=10, text = '1,1')
button.pack()

window.mainloop()
