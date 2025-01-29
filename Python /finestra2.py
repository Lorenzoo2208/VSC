
import tkinter as tk


window = tk.Tk()


window.title("Cacato nel puzzo")


window.geometry("600x600")


window.resizable(True, True) #permette di aumentare la grandezza della finestra


window.configure(background="white")




#Mettiamo qui i widget


etichetta=tk.Label(window, text="etichetta di prova", fg="#FF0000", font=("Helvetica", 16))
etichetta.grid(row=0, column=0, sticky= "W", padx=10, pady=10)


#funzione per stampare button


def stampa_etichetta():
   text = "etichetta di prova da funzione"
   text_output = tk.Label(window, text=text, fg="#ff0000", font=("Helvetica",16))


   text_output.grid(row=1, column=0, sticky="W")


#button


first_button = tk.Button(text="Clicca!", command=stampa_etichetta)
first_button.grid(row=0, column=1, sticky="W")


#stringa per scrivere quello che vuoi


input_text = tk.Entry(window)
input_text.grid(row=2, column=0, sticky="W")




#funzione per stampare un'etichetta con input


def stampa_etichetta_input():
   testo = input_text.get ()
   text_output1= tk.Label(window, text=testo, fg="#FF0000", font=("Helvetica, 16"))
   text_output1.grid(row=5, column=0, sticky="w")


#Creazione del campo input
input_text = tk.Entry(window)
input_text.grid(row=4, column=0, sticky="W")


# Creazione del secondo bottone
secondo_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
secondo_button.grid(row=4, column=1, sticky="W")


# from threading import Thread
# import time
# class MioThread(Thread):
#     def __init__(self,nome,durata): da  finire


if __name__=="__main__":
   window.mainloop()


