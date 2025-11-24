import tkinter as tk
import random
window = tk.Tk()
window.title("Let's Go Gambling")
window.geometry("600x550")
def gamble():
    a=random.randint(1,9)
    b=random.randint(1,9)
    c=random.randint(1,9)
    x=a,b,c
    if a==b==c:
        outputtext = tk.Label(window, text=x, font=("Courier New", 14),fg="green",wraplength=570, justify="left")
        outputtext.pack(pady=2)
    else:
        outputtext = tk.Label(window, text=x, font=("Courier New", 14),fg="tomato",wraplength=570, justify="left")
        outputtext.pack(pady=2)
confirm_button=tk.Button(window, text=" Roll ",font=("Georgia", 14),command=gamble)
confirm_button.pack(pady=2)
window.mainloop()