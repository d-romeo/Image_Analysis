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

        # Creazione delle etichette delle immagini senza immagini inizialmente
        self.img_label1 = tk.Label(master, bg="#f0f0f0")
        self.img_label1.pack(side=tk.LEFT, padx=10)

        self.img_label2 = tk.Label(master, bg="#f0f0f0")
        self.img_label2.pack(side=tk.RIGHT, padx=10)

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
            self.status_label.config(text="Cancello Chiuso", fg="red")
        img1_path = "temp/true.jpg"
        img2_path = "temp/img.jpg"
        self.update_images(img1_path, img2_path)

    def update_vector_label(self):
        self.vector_label.config(text="Targhe Ammesse: " + str(self.vector))

    def update_vector_label(self):
        self.vector_label.config(text="Targhe Ammesse: " + str(self.vector))

    def update_images(self, img1_path, img2_path):
        # Aggiorna le immagini con nuovi percorsi
        img1 = Image.open(img1_path)
        img1 = img1.resize((200, 150), Image.Resampling.LANCZOS)
        img1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(img2_path)
        img2 = img2.resize((200, 150), Image.Resampling.LANCZOS)
        img2 = ImageTk.PhotoImage(img2)

        # Aggiorna le etichette con le nuove immagini
        self.img_label1.config(image=img1)
        self.img_label1.image = img1

        self.img_label2.config(image=img2)
        self.img_label2.image = img2

def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()