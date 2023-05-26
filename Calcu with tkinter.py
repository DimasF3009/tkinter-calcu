import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator")

        # Membuat label untuk menampilkan input dan hasil
        self.display = tk.Label(master, width=25, height=2, font=("Arial", 12), background="#f0f0f0", anchor="e")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Membuat tombol-tombol untuk kalkulator
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]
        row, col = 1, 0
        for button_text in buttons:
            # Membuat tombol dengan teks button_text dan menempatkannya pada grid
            button = tk.Button(master, text=button_text, width=5, height=2, font=("Arial", 12),
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                col = 0
                row += 1

        self.reset_display()

    def reset_display(self):
        # Menampilkan 0 pada display
        self.display.config(text="0")

    def button_click(self, text):
        if text == "C":
            self.reset_display()
        elif text == "=":
            try:
                # Evaluasi ekspresi pada display dan menampilkan hasilnya pada display
                result = eval(self.display["text"])
                self.display.config(text=str(result))
            except:
                # Menampilkan pesan error pada display jika ekspresi tidak valid
                self.display.config(text="Error")
        else:
            # Menambahkan angka atau operator ke display
            if self.display["text"] == "0":
                self.display.config(text=text)
            else:
                self.display.config(text=self.display["text"] + text)


root = tk.Tk()
app = Calculator(root)
root.mainloop()
