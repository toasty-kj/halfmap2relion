import glob
import re
import tkinter
from tkinter import filedialog, messagebox

class ReadFile:
    def reedfile(self):
        # hide root window
        root = tkinter.Tk()
        root.withdraw()
        # select directory
        while True:
            direc = filedialog.askdirectory()
            direc_sharp = direc +"/*sharp.mrc"
            direc_half = direc +"/**"
            sharp_map = glob.glob(direc_sharp)
            if not sharp_map:
                print(
                    "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")
                messagebox.showerror("cound't find file !!", "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")
            if sharp_map:
                print("loaded successfully!" + " :" + str(sharp_map))
                half_map =[p for p in glob.glob(direc_half, recursive=True)
                       if re.search("map_half", p)]
                messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!!")
                return half_map
                break










