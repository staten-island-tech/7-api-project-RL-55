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
def entry(botw):
    response = requests.get(f"https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{botw.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return{
        "name": data["data"]["name"],
        "id":data["data"]["id"],
        "category": data["data"]["category"],
        "location": data["data"]["common_locations"],
        "drops": data["data"]["drops"],
        "image":data["data"]["image"]
        }
def entryget():
    output = (entrybox.get()).lower()
    entry2=entry(output)
    for key, value in entry2.items():
        x=(key,":",value)
        outputtext = tk.Label(window, text=x, font=("Arial", 14),fg="blue",wraplength=570, justify="left")
        outputtext.pack(pady=2)

confirm_button = tk.Button(window, text="Search",font=("Arial", 14),command=entryget)
confirm_button.pack(pady=10)
window.mainloop()