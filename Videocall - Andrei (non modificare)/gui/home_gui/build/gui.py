
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\stehino\Desktop\New folder\Andrei\Scuola\TPSIT\Laboratorio\Videocall\gui\home_gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#7492AE")



def open_join_window():

    # Chiudi la finestra corrente
    #window.destroy()

    # Apri la finestra di join
    join_window = Toplevel(window)
    join_window.geometry("1000x600")
    join_window.title("Finestra di Join")

    join_canvas = Canvas(
        join_window,
        bg="#7593AE",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    join_canvas.place(x=0, y=0)

    join_button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    join_button_1 = Button(
        join_canvas,
        image=join_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked in join_window"),
        relief="flat"
    )
    join_button_1.place(
        x=375.0,
        y=300.0,
        width=250.0,
        height=60.0
    )

    join_canvas.create_text(
        331.0,
        196.0,
        anchor="nw",
        text="Inserisci il codice della stanza",
        fill="#FFFFFF",
        font=("Inter", 26 * -1)
    )

    join_entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    join_entry_bg_1 = join_canvas.create_image(
        500.0,
        267.5,
        image=join_entry_image_1
    )
    join_entry_1 = Entry(
        join_canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    join_entry_1.place(
        x=325.0,
        y=250.0,
        width=350.0,
        height=33.0
    )

    join_canvas.create_text(
        465.0,
        313.0,
        anchor="nw",
        text="Entra",
        fill="#FFFFFF",
        font=("Inter", 26 * -1)
    )


canvas = Canvas(
    window,
    bg = "#7492AE",
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
    command=open_join_window,
    relief="flat"
)
button_1.place(
    x=641.0,
    y=223.0,
    width=250.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=639.0,
    y=316.0,
    width=250.0,
    height=60.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    600.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    712.0,
    238.0,
    anchor="nw",
    text="Connettiti\n",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    736.0,
    330.0,
    anchor="nw",
    text="Crea",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    143.0,
    147.0,
    anchor="nw",
    text="SGC",
    fill="#000000",
    font=("Inter Thin", 100 * -1)
)

canvas.create_text(
    33.0,
    286.0,
    anchor="nw",
    text="Applicazione per videochiamate",
    fill="#000000",
    font=("Inter Thin", 30 * -1)
)
window.resizable(False, False)
window.mainloop()
