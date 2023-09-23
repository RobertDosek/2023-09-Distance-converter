import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from win_avareness import set_dpi_awareness

set_dpi_awareness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=30, pady=15, sticky="EW")

        # feet_to_metres = FeetToMeters(container, self)
        # feet_to_metres.grid(row=0, column=0, sticky="NSEW")
        #
        # meters_to_feet = MetersToFeet(container, self)
        # meters_to_feet.grid(row=0, column=0, sticky="NSEW")
        #
        # self.frames[FeetToMeters] = feet_to_metres
        # self.frames[MetersToFeet] = meters_to_feet

        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(MetersToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value)
        feet_label = ttk.Label(self, text="Feet")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self, text="Switch to feet conversion",
                                        command=lambda: controller.show_frame(FeetToMeters))

        meters_label.grid(row=0, column=0, sticky="w")
        meters_input.grid(row=0, column=1, sticky="ew")
        meters_input.focus()
        feet_label.grid(row=1, column=0, sticky="w")
        feet_display.grid(row=1, column=1, sticky="ew")
        calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        for child in self.winfo_children():
            child.grid(padx=5, pady=5)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value)
        meters_label = ttk.Label(self, text="Meters")
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self, text="Switch to meters conversion",
                                        command=lambda: controller.show_frame(MetersToFeet))

        feet_label.grid(row=0, column=0, sticky="w")
        feet_input.grid(row=0, column=1, sticky="ew")
        feet_input.focus()
        meters_label.grid(row=1, column=0, sticky="w")
        meters_display.grid(row=1, column=1, sticky="ew")
        calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        for child in self.winfo_children():
            child.grid(padx=5, pady=5)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f"{meters:.3f}")
        except ValueError:
            pass


root = DistanceConverter()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# set the Azure theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

root.mainloop()
