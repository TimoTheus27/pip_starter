import tkinter as tk
from typing import Dict, MutableMapping
from Measurement import Measurement
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ContentFrame:
    def __init__(self, main_window: tk.Tk):
        self.frame = tk.Frame(main_window, bd=2, height=994, width=1680, )
        self.frame.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

    def ui_clean_content_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def ui_draw_measurements(self, measurements_dict: MutableMapping[str, Measurement], selected_material: tk.StringVar):
        self.ui_clean_content_frame()

        # top_text = tk.Text(self.frame)
        # top_text.insert(tk.END, measurements_dict[selected_material.get()].material.__str__())
        # top_text.pack(fill=tk.BOTH)
        # fds_results = measurements_dict[selected_material.get()].fds_results
        # fig1 = fds_results.plot.line(title="FDS Resukts", y='Frequency [Hz]', figsize=(3,3)).get_figure()
        #
        # plot1 = FigureCanvasTkAgg(fig1, self.frame)
        # plot1.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        fds_results = tk.Text(self.frame)
        fds_results.insert(tk.END, measurements_dict[selected_material.get()].fds_results.info().__str__())
        fds_results.pack(fill=tk.BOTH, expand=True)




    def ui_draw_frequencies(self, selected_frequency):
        self.ui_clean_content_frame()

        lbl = tk.Label(self.frame, textvariable=selected_frequency)
        lbl.pack()

    def ui_draw_scrollbars(self, frame: tk.Frame) -> Dict[str, tk.Scrollbar]:
        # create a horizontal scrollbar by
        # setting orient to horizontal
        h = tk.Scrollbar(frame, orient='horizontal')

        # attach Scrollbar to root window at
        # the bootom
        h.pack(side=tk.BOTTOM, fill=tk.X)

        # create a vertical scrollbar-no need
        # to write orient as it is by
        # default vertical
        v = tk.Scrollbar(frame)

        # attach Scrollbar to root window on
        # the side
        v.pack(side=tk.RIGHT, fill=tk.Y)

        return {
            'v': v,
            'h': h
        }