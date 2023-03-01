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
        '''
        delete one line below and replace with this code #direc = filedialog.askdirectory()
        '''
        direc = filedialog.askdirectory(initialdir="/home/koji/Downloads")
        direc_raw = direc + "/*FrameImage.tif"
        #direc_half = direc + "/**"
        sharp_map = glob.glob(direc_raw)
        # if selected directory doesn't contain refined mrc map
        if not sharp_map:
            print(
                "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")
            messagebox.showerror("cound't find file !!",
                                 "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")

        # if it contains refined map
        if sharp_map:
            #print number of micrographs in the selected directory
            print(str(sharp_map))
            print("loaded successfully!")
            print("loaded " + str(len(sharp_map)) + " micrographs")
            messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!!")
            # return list stored two path(both half map)
            return direc
            break
def get_raw_mic(raw_dir):
    direc_raw = raw_dir + "/*FrameImage.tif"
    # direc_half = raw_dir + "/**"
    sharp_map = glob.glob(direc_raw)
    return sharp_map
def dir_maker(raw_dir):
    print("Select path you want to make a directory for processing")
    proc_path = filedialog.askdirectory(initialdir=raw_dir)
    return proc_path
    #make process and Movie directory

raw_dir = sel_raw_data()
raw_mic = get_raw_mic(raw_dir)
print(raw_mic)
proc_path = dir_maker(raw_dir)