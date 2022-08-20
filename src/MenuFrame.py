import tkinter as tk
from PIL import ImageTk, Image

class MenuFrame:
    def __init__(self, main_window: tk.Tk):
        self.frame = tk.Frame(main_window, bd=0, height=56, width=1680, bg="white", relief=tk.SUNKEN)
        self.configure_menu_grid()
        self.frame.pack(fill=tk.BOTH, side=tk.TOP)

    def configure_menu_grid(self):
        self.frame.columnconfigure(0, weight=1, minsize=280)
        self.frame.columnconfigure(1, weight=1, minsize=280)
        self.frame.columnconfigure(2, weight=1, minsize=280)
        self.frame.columnconfigure(3, weight=1, minsize=280)
        self.frame.columnconfigure(4, weight=1, minsize=280)
        self.frame.columnconfigure(5, weight=1, minsize=280)
        self.frame.rowconfigure(0, weight=1, minsize=56)

    def ui_draw_read_csv_button(self, read_csv_function):
        # Create Add-CSV-Data Button
        add_csv_button = tk.Button(
            self.frame,
            height=2,
            text="Messung hinzufügen",
            command=read_csv_function,
        )
        add_csv_button.grid(row=0, column=0, sticky="ew", padx=10)

    def ui_draw_material_dropdown(self, measurements_dict, selected_material):
        measurements = ["loading"]
        if len(measurements_dict) > 0:
            measurements = measurements_dict

        opt = tk.OptionMenu(
            self.frame, selected_material,
            *measurements
        )
        opt.grid(row=0, column=1, sticky="ew", padx=10)

    def ui_draw_display_data_button(self, display_data_function):
        add_csv_button = tk.Button(
            self.frame,
            height=2,
            text="Messung anzeigen",
            command=display_data_function,
        )
        add_csv_button.grid(row=0, column=2, sticky="ew", padx=10)

    def ui_draw_logo(self):
        canvas = tk.Canvas(self.frame, width=280, height=56, background="white")
        canvas.grid(row=0, column=3, pady=0, sticky="ew", padx=0)
        img = ImageTk.PhotoImage(Image.open("/Users/timogerth/Development/python-example/src/image.png"))
        canvas.create_image(200, 56, anchor=tk.CENTER, image=img)

    def ui_draw_frequency_dropdown(self, frequencies, selected_frequency):
        print(selected_frequency.get())
        opt = tk.OptionMenu(
            self.frame, selected_frequency,
            *frequencies
        )
        opt.grid(row=0, column=4, sticky="ew", padx=10)

    def ui_draw_frequency_button(self, ui_draw_frequencies):
        add_csv_button = tk.Button(
            self.frame,
            height=2,
            text="Frequenzvergleich",
            command=ui_draw_frequencies
        )
        add_csv_button.grid(row=0, column=5, sticky="ew", padx=10)
