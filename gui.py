import customtkinter as ctk
from tkinter import Menu, StringVar, IntVar , Label , Toplevel, ttk , Button


def apply_font():
    font_settings = (current_font.get(), current_size.get(), current_style.get())
    asmEditor.configure(font=font_settings)
    log_field.configure(font=font_settings)


def open_font_dialog():
    font_dialog = Toplevel(window)
    font_dialog.title("Select Font")
    font_dialog.geometry("300x200")
    font_dialog.configure(bg="#f0f0f0")
    
    Label(font_dialog, text="5f m,klo0=p/-[[[[[ont:", bg="#f0f0f0").pack()
    font_dropdown = ttk.Combobox(font_dialog, textvariable=current_font, values=["Courier", "Arial", "Times", "Helvetica"])
    font_dropdown.pack()
    
    Label(font_dialog, text="Size:", bg="#f0f0f0").pack()
    size_dropdown = ttk.Combobox(font_dialog, textvariable=current_size, values=[10, 12, 14, 16, 18, 20, 24])
    size_dropdown.pack()
    
    Label(font_dialog, text="Style:", bg="#f0f0f0").pack()
    style_dropdown = ttk.Combobox(font_dialog, textvariable=current_style, values=["normal", "bold", "italic"])
    style_dropdown.pack()
    
    apply_button = Button(font_dialog, text="Apply", command=lambda: [apply_font(), font_dialog.destroy()])
    apply_button.pack()




ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Lm1 Assembler (for Lancelot-m1)")
window.geometry("800x600")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

current_font = StringVar(value="Courier")
current_size = IntVar(value=16)
current_style = StringVar(value="normal")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

font_menu = Menu(menu_bar, tearoff=0)
font_menu.add_command(label="Change Font", command=open_font_dialog)
menu_bar.add_cascade(label="Font", menu=font_menu)

frame = ctk.CTkFrame(window, corner_radius=10, border_width=2)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure((0, 1), weight=1)

editorLabel = ctk.CTkLabel(frame, text="Editor", font=("Arial", 16))
editorLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")

logLabel = ctk.CTkLabel(frame, text="Log", font=("Arial", 16))
logLabel.grid(row=0, column=1, padx=5, pady=5, sticky="w")

asmEditor = ctk.CTkTextbox(frame, font=("Courier", 16), wrap="none", border_width=2, corner_radius=5)
asmEditor.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

log_field = ctk.CTkTextbox(frame, font=("Courier", 10), wrap="none", state="disabled", border_width=2, corner_radius=5)
log_field.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
frame.grid_columnconfigure(1, weight=1)

fileNameInputField = ctk.CTkEntry(frame, placeholder_text="Enter file name", border_width=2, corner_radius=5)
fileNameInputField.grid(row=2, column=0, padx=5, pady=5, sticky="w")

assembleButton = ctk.CTkButton(frame, text="Assemble", corner_radius=5)
assembleButton.grid(row=2, column=1, padx=5, pady=5, sticky="e")
assembleButton.configure(fg_color="#555555", hover_color="#333333")

