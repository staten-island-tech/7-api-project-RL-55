import tkinter as tk
import requests
window = tk.Tk()
window.title("Pad")
window.geometry("600x550")
window.resizable(False, False)
prompttext = tk.Label(window, text="Search for:",font=("Arial", 14))
prompttext.pack(pady=10)
entrybox = tk.Entry(window, font=("Arial", 14), width=40)
entrybox.pack(pady=5)
def entryget():
    output = (entrybox.get()).lower()
    print(output)

confirm_button = tk.Button(window, text="Search",font=("Arial", 14),command=entryget)
confirm_button.pack(pady=10)

outputtext = tk.Label(window, text="ww", font=("Arial", 14),fg="blue")
outputtext.pack(pady=5)

window.mainloop()