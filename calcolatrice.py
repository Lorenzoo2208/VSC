import tkinter as tk


window = tk.Tk()


window.title("Calcolatrice Semplice")


window.geometry("600x600")


window.resizable(True, True) #permette di aumentare la grandezza della finestra


window.configure(background="black")


#Mettiamo qui i widget


etichetta=tk.Label(window, text="Calcolatrice", fg="#FF0000", font=("Helvetica", 16))
etichetta.grid(row=0, column=0, sticky= "W", padx=10, pady=10)


#funzione per stampare button


input_text = tk.Entry(window)
input_text.grid(row=0, column=0, sticky="W")


input_text2 = tk.Entry(window)
input_text2.grid(row=2, column=0, sticky="W")


#operazione per la moltiplicazione

def Operazione_Moltiplicazione():


   int_input_text = int(input_text.get())
   int_input_text2 = int(input_text2.get())
   risultato = int_input_text * int_input_text2
   output_risultato = tk.Label(window, text=risultato, fg bla bla)
   output_risultato.grid(row 1, column=0, sticky"W", padx=10, padx=10)


   moltiplicazione = tk.Button()
   moltiplicazione.grid(row=1)


if __name__=="__main__":
   window.mainloop()

