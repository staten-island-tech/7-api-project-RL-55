import tkinter as tk
window = tk.Tk()
window.title("BOTW")
window.geometry("600x550")
window.resizable(False, False)
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
window.mainloop()