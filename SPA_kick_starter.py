"""
take raw data acquired from CryoEM for Single Particle Analysis (select on GUI)
make directory for processing (make movie directory under process directory)
Then link data from original directory containing raw data.
Finally, run relion and make gainref file (import linked data and data for gainref, thne produce gainref through relion).
(you can proceed to motion correction on relion if Yes.)
"""
import glob
import re
import shutil
import tkinter
from tkinter import messagebox, filedialog

def sel_raw_data():
    # hide root window
    root = tkinter.Tk()
    root.withdraw()
    # select directory
    messagebox.showinfo("Select directory containing raw data", "Select Job Directory you want to start processing")
    while True:
        direc = filedialog.askdirectory()
        direc_raw = direc + "/*FrameImage.tif"
        direc_half = direc + "/**"
        sharp_map = glob.glob(direc_raw)
        # if selected directory doesn't contain refined mrc map
        if not sharp_map:
            print(
                "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")
            messagebox.showerror("cound't find file !!",
                                 "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")

        # if it contains refined map
        if sharp_map:
            print("loaded successfully!" + " :" + str(sharp_map))
            half_map = [p for p in glob.glob(direc_half, recursive=True)
                        if re.search("map_half", p)]
            messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!!")
            # return list stored two path(both half map)
            return half_map
            break

raw_mic = 