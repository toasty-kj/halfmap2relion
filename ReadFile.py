import tkinter
from tkinter import filedialog

class ReadFile:
    def reedfiles(self):

        # hide root window
        root = tkinter.Tk()
        root.withdraw()
        # select directory
        files = filedialog.askdirectory()
        return files

    def get_mrc_path(self):
        rx = "volume_map_sharp.mrc"





