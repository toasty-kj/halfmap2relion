import tkinter
from tkinter import filedialog, messagebox
import shutil

class Copy2Relion:
    def copy2relion(self, half_map):
        # hide root window
        root = tkinter.Tk()
        root.withdraw()
        # select directory
        messagebox.showinfo("Select destination", "Please select directory currently processing on Relion")
        destination = filedialog.askdirectory()
        destination_A = destination+"/run_half1_class001_until.mrc"
        destination_B = destination + "/run_half2_class001_until.mrc"
        shutil.copy(half_map[0], destination_A)
        print("copied " + half_map[0] +"→" + "to" + destination + "and renamed to" +destination_A)
        shutil.copy(half_map[1], destination_B)
        print("copied " + half_map[1] + "→" + "to" + destination + "and renamed to" + destination_B)


