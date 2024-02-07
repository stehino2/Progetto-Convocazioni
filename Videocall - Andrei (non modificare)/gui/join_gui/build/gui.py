
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\stehino\Desktop\New folder\Andrei\Scuola\TPSIT\Laboratorio\Videocall\gui\join_gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#7593AE")


canvas = Canvas(
    window,
    bg = "#7593AE",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=375.0,
    y=300.0,
    width=250.0,
    height=60.0
)

canvas.create_text(
    331.0,
    196.0,
    anchor="nw",
    text="Inserisci il codice della stanza",
    fill="#FFFFFF",
    font=("Inter", 26 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    500.0,
    267.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=325.0,
    y=250.0,
    width=350.0,
    height=33.0
)

canvas.create_text(
    465.0,
    313.0,
    anchor="nw",
    text="Entra",
    fill="#FFFFFF",
    font=("Inter", 26 * -1)
)
window.resizable(False, False)
window.mainloop()