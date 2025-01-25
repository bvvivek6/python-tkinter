import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry = tk.Entry(root, font=("poppins", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]


for text, row, col in buttons:
    button = tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: click(t))
    button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
