import glob
import tkinter
from tkinter import filedialog

class ReadFile:
    def reedfile(self):

        # hide root window
        root = tkinter.Tk()
        root.withdraw()
        # select directory
        direc = filedialog.askdirectory()
        return direc

    def get_mrc_path(self, direc):
        direc = direc +"/"
        sharp_map = glob.glob(direc + "*.volume_map_sharp.mrc")
        print(sharp_map)






