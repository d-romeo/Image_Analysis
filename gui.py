import tkinter as tk
import utils
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Targhe")
        self.master.geometry("400x300")

        self.vector = []

        # Label per inserire il testo
        self.label = tk.Label(master, text="Inserisci elemento:")
        self.label.pack()

        # Campo di testo per inserire il testo
        self.text_entry = tk.Entry(master)
        self.text_entry.pack()

        # Bottone per aggiungere elemento al vettore
        self.add_button = tk.Button(master, text="Aggiungi", command=self.add_element)
        self.add_button.pack()

        # Bottone per rimuovere ultimo elemento dal vettore
        self.remove_button = tk.Button(master, text="Rimuovi", command=self.remove_element)
        self.remove_button.pack()

        # Spazio per visualizzare il vettore
        self.vector_label = tk.Label(master, text="Targhe ammesse: " + str(self.vector))
        self.vector_label.pack()

        # Bottone per simulare arrivo autp
        self.request_button = tk.Button(master, text="Richiesta di ingresso", command=self.request)
        self.request_button.pack()

        # Spazio per visualizzare il vettore
        self.label = tk.Label(master, text=" Cancello Chiuso", fg="red")
        self.label.pack()


    def add_element(self):
        element = self.text_entry.get()
        if element:
            self.vector.append(element)
            self.update_vector_label()

    def remove_element(self):
        if self.vector:
            self.vector.pop()
            self.update_vector_label()

    def request(self):
        check = utils.request_to_join(self.vector)
        if check:
            self.label.config(text="Macchina AMMESSA", fg="green")
        else:
            self.label.config(text="Cancello Chiuso" , fg="red")
    def update_vector_label(self):
        self.vector_label.config(text="Targhe Ammesse: " + str(self.vector))


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()