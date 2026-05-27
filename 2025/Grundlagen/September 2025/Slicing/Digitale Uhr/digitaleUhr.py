
#22.09.25


import tkinter
import time
 
def uhrzeit():
    aktuelle_uhrzeit = time.strftime('%H:%M:%S')
    uhr_label.config(text= aktuelle_uhrzeit)
    uhr_label.after(1000, uhrzeit)
 
root = tkinter.Tk()
root.geometry("300x100")
root.title("Digitale Uhr")
uhr_label = tkinter.Label(root, font=("Helvetica", 48), background="#2980B9", foreground="white")
 
uhr_label.pack(anchor="center")
 
uhrzeit()
 
root.mainloop()
 