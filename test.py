import tkinter as tk
window = tk.Tk()
window.title("BOTW")
window.geometry("600x550")
window.resizable(False, False)
entry_field = tk.Entry(window, width=50)
entry_field.pack(pady=10)
def get_entry_text():
    text = entry_field.get()
    print(f"Entry text: {text}")
button = tk.Button(window, text="Get Entry Text", command=get_entry_text)
button.pack()
window.mainloop()