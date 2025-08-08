from tkinter.filedialog import askopenfilename, asksaveasfilename
from gui import asmEditor


def open_file():
    file_path = askopenfilename(filetypes=[("LM1 assembly", "*.lasm"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            asmEditor.delete("1.0", "end")
            asmEditor.insert("1.0", file.read())

def save_file():
    file_path = asksaveasfilename(filetypes=[("LM1 assembly", "*.lasm"), ("All Files", "*.*")])
    if not file_path.endswith(".lasm"):
        file_path += ".lasm"
    if file_path:
        with open(file_path, 'w') as file:
            file.write(asmEditor.get("1.0", "end"))
            
            

