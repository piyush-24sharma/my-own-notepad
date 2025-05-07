import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("MY Own Notepad!!")
window.rowconfigure(0, minsize=800)
window.columnconfigure(0,minsize=1000)

def saving_file():
    file_location = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    window.title(f"MY OWN NOTEPAD - {file_location}")

def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_location:
        return
    text_edit.delete(1.0,tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    window.title(f"MY OWN NOTEPAD - {file_location}")

text_edit = tk.Text(window)
text_edit.grid(row=0, column=1)

frame_button = tk.Frame(window, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=3, sticky="nsew")

save_button = tk.Button(frame_button, text="SAVE AS FILE", command=saving_file)
save_button.grid(row=0, column=1, padx=5, pady=3)

window.mainloop()
