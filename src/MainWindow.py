import tkinter as tk
from tkinter.filedialog import askopenfile
from typing import Type, Dict
import pandas as pd

from functools import partial
from typing import MutableMapping
from PIL import ImageTk,Image
from CSVReader import create_data_frame_with
from Measurement import Measurement
from MenuFrame import MenuFrame
from ContentFrame import ContentFrame
class MainWindow:
    def __init__(self):
        print("2. Initialize the new instance of GUI.")
        self.window = self.ui_configure_window()
        # create empty measurement's dictionary
        # this contains instances of measurements by key -> value
        self.measurements: MutableMapping[str, Measurement] = {}

        self.selected_material = tk.StringVar(self.window)
        self.selected_material.set("Loading")

        self.frequencies = [
            "-1 Khz",
            "0 Khz",
            "1 Khz",
        ]
        self.selected_frequency = tk.StringVar(self.window)
        self.selected_frequency.set("1 Khz")
        self.content = ContentFrame(self.window)
        self.menu = self.ui_draw_menu()

        self.window.mainloop()

    def ui_configure_window(self):
        window = tk.Tk()
        window.title('Materialdatenbank')
        window.geometry("1680x1050")

        window.rowconfigure(0, minsize=56, weight=1)
        window.rowconfigure(1, minsize=994, weight=1)
        window.columnconfigure(0, minsize=1680, weight=1)
        return window

    def ui_draw_menu(self):
        menu = MenuFrame(self.window)
        menu.ui_draw_read_csv_button(self.read_csv)
        menu.ui_draw_material_dropdown(self.measurements, self.selected_material)
        menu.ui_draw_display_data_button(
            partial(self.content.ui_draw_measurements, self.measurements, self.selected_material)
        )
        menu.ui_draw_logo()
        menu.ui_draw_frequency_dropdown(self.frequencies, self.selected_frequency)
        menu.ui_draw_frequency_button(partial(self.content.ui_draw_frequencies, self.selected_frequency))
        return menu

    # Open CSV and initialize dataframe
    def read_csv(self):
        # Chose File to open
        file = askopenfile(mode='r', filetypes=[("csv files", "*.csv")])
        if not file:
            print('Unable to access file')
            return None
        print(file.name)

        measurements_df = create_data_frame_with('MEASUREMENTS', file.name)
        fds_results_df = create_data_frame_with('FDS RESULTS', file.name)

        # create new measurement class
        measurement = Measurement(measurements_df, fds_results_df)
        self.add_measurement(measurement)

    # store measurement in dictionary key: name of measurement, value: measurement class instance itself
    def add_measurement(self, measurement):
        self.measurements[measurement.get_name()] = measurement
        self.selected_material.set(measurement.get_name())

        # new data => draw dropdown again
        self.menu.ui_draw_material_dropdown(self.measurements, self.selected_material)
    # def ui_displ
    #def ui_display_data(self):
