import tkinter as tkinter

window = tkinter.Tk()
window.title("Calender")
window.geometry("1000x800")
btn = tkinter.Button(window, text = 'This should quit the program', bd = '5', command = window.destroy)
btn.pack(side = 'right')
window.mainloop()
