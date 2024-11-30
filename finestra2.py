
# import tkinter as tk


# window = tk.Tk()


# window.title("Cacato nel puzzo")


# window.geometry("600x600")


# window.resizable(True, True) #permette di aumentare la grandezza della finestra


# window.configure(background="white")




# #Mettiamo qui i widget


# etichetta=tk.Label(window, text="etichetta di prova", fg="#FF0000", font=("Helvetica", 16))
# etichetta.grid(row=0, column=0, sticky= "W", padx=10, pady=10)


# #funzione per stampare button


# def stampa_etichetta():
#    text = "etichetta di prova da funzione"
#    text_output = tk.Label(window, text=text, fg="#ff0000", font=("Helvetica",16))


#    text_output.grid(row=1, column=0, sticky="W")


# #button


# first_button = tk.Button(text="Clicca!", command=stampa_etichetta)
# first_button.grid(row=0, column=1, sticky="W")


# #stringa per scrivere quello che vuoi


# input_text = tk.Entry(window)
# input_text.grid(row=2, column=0, sticky="W")




# #funzione per stampare un'etichetta con input


# def stampa_etichetta_input():
#    testo = input_text.get ()
#    text_output1= tk.Label(window, text=testo, fg="#FF0000", font=("Helvetica, 16"))
#    text_output1.grid(row=5, column=0, sticky="w")


# #Creazione del campo input
# input_text = tk.Entry(window)
# input_text.grid(row=4, column=0, sticky="W")


# # Creazione del secondo bottone
# secondo_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
# secondo_button.grid(row=4, column=1, sticky="W")


# # from threading import Thread
# # import time
# # class MioThread(Thread):
# #     def __init__(self,nome,durata): da  finire


# if __name__=="__main__":
#    window.mainloop()


import tkinter as tk
import threading
import time


def create_window(width, height, title, bg_color, font_size, font_family):
   # Creare la finestra principale
   root = tk.Tk()
  
   # Impostare le dimensioni della finestra
   root.geometry(f"{width}x{height}")
  
   # Impostare il titolo della finestra
   root.title(title)
  
   # Impostare il colore di sfondo della finestra
   root.configure(bg=bg_color)
  
   # Creare una label con dimensioni e font specificati
   font = (font_family, font_size)
   label = tk.Label(root, text="Questo è un testo colorato!", fg="#FF0000", bg=bg_color, font=font)
   label.pack(pady=20)
  
   # Creare un canvas per disegnare il cerchio
   canvas = tk.Canvas(root, width=100, height=100, bg=bg_color)
   canvas.pack(pady=20)
  
   # Disegnare il cerchio (LED)
   led = canvas.create_oval(25, 25, 75, 75, fill="green")
  
   def blink_led():
       while True:
           current_color = canvas.itemcget(led, "fill")
           new_color = "red" if current_color == "green" else "green"
           canvas.itemconfig(led, fill=new_color)
           time.sleep(0.5)
  
   # Creare e avviare il thread per far lampeggiare il cerchio
   threading.Thread(target=blink_led, daemon=True).start()
  
   # Avviare il ciclo principale della finestra
   root.mainloop()


# Esempio di utilizzo
width = 400
height = 300
title = "Finestra con LED lampeggiante"
bg_color = "lightblue"
font_size = 16
font_family = "Helvetica"


create_window(width, height, title, bg_color, font_size, font_family)
