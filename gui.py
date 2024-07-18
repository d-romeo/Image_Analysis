import tkinter as tk
from PIL import Image, ImageTk
import utils
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestione Targhe")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")  # Colore di sfondo

        self.vector = []

        # Label per inserire il testo
        self.label = tk.Label(master, text="Inserisci elemento:", bg="#f0f0f0", font=("Helvetica", 12))
        self.label.pack(pady=(10, 5))  # Margine sopra e sotto

        # Campo di testo per inserire il testo
        self.text_entry = tk.Entry(master, font=("Helvetica", 12), bd=2, relief="groove")
        self.text_entry.pack(pady=(0, 10))  # Margine sotto

        # Bottone per aggiungere elemento al vettore
        self.add_button = tk.Button(master, text="Aggiungi", command=self.add_element, bg="#4caf50", fg="white",
                                    font=("Helvetica", 12), bd=0, relief="flat", padx=10, pady=5)
        self.add_button.pack(pady=(0, 10))  # Margine sotto

        # Bottone per rimuovere ultimo elemento dal vettore
        self.remove_button = tk.Button(master, text="Rimuovi", command=self.remove_element, bg="#f44336",
                                       fg="white", font=("Helvetica", 12), bd=0, relief="flat", padx=10, pady=5)
        self.remove_button.pack(pady=(0, 20))  # Margine sotto

        # Spazio per visualizzare il vettore
        self.vector_label = tk.Label(master, text="Targhe ammesse: " + str(self.vector), bg="#f0f0f0",
                                     font=("Helvetica", 12))
        self.vector_label.pack(pady=(0, 20))  # Margine sotto

        # Bottone per simulare arrivo auto
        self.request_button = tk.Button(master, text="Richiesta di ingresso", command=self.request, bg="#2196f3",
                                        fg="white", font=("Helvetica", 12), bd=0, relief="flat", padx=10, pady=5)
        self.request_button.pack(pady=(0, 20))  # Margine sotto

        # Spazio per visualizzare lo stato del cancello
        self.status_label = tk.Label(master, text="Cancello Chiuso", fg="red", bg="#f0f0f0",font=("Helvetica", 12, "bold"))
        self.status_label.pack()

        # Aggiunta delle immagini
        self.add_images(master)

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
            self.status_label.config(text="Macchina AMMESSA", fg="green")
        else:
            self.status_label.config(text="Cancello Chiuso" , fg="red")

    def update_vector_label(self):
        self.vector_label.config(text="Targhe Ammesse: " + str(self.vector))
    def add_images(self, master):
        img1 = Image.open("plates/plate2.jpg")  # Sostituisci con il percorso della tua immagine
        img1 = img1.resize((200, 150), Image.Resampling.LANCZOS)
        img1 = ImageTk.PhotoImage(img1)

        img2 = Image.open("plates/plate2.jpg")  # Sostituisci con il percorso della tua immagine
        img2 = img2.resize((200, 150), Image.Resampling.LANCZOS)
        img2 = ImageTk.PhotoImage(img2)

        # Crea le label per le immagini
        self.img_label1 = tk.Label(master, image=img1, bg="#f0f0f0")
        self.img_label1.image = img1  # Per evitare che l'immagine venga garbage collected
        self.img_label1.pack(side=tk.LEFT, padx=10)

        self.img_label2 = tk.Label(master, image=img2, bg="#f0f0f0")
        self.img_label2.image = img2  # Per evitare che l'immagine venga garbage collected
        self.img_label2.pack(side=tk.RIGHT, padx=10)

def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()