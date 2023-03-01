"""
take raw data acquired from CryoEM for Single Particle Analysis (select on GUI)
make directory for processing (make movie directory under process directory)
Then link data from original directory containing raw data.
Finally, run relion and make gainref file (import linked data and data for gainref, thne produce gainref through relion).
(you can proceed to motion correction on relion if Yes.)
"""
import glob
import tkinter
from tkinter import messagebox, filedialog
import os


def sel_raw_data():
    # hide root window
    root = tkinter.Tk()
    root.withdraw()
    # select directory
    messagebox.showinfo("Select directory containing raw data", "Select Directory you want to start processing")
    while True:
        '''
        delete one line below and replace with this code #direc = filedialog.askdirectory()
        '''
        direc = filedialog.askdirectory(initialdir="/home/koji/Downloads")
        direc_raw = direc + "/*FrameImage.tif"
        # direc_half = direc + "/**"
        sharp_map = glob.glob(direc_raw)
        # if selected directory doesn't contain refined mrc map
        if not sharp_map:
            print(
                "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")
            messagebox.showerror("cound't find file !!",
                                 "couldn't find \"volume_map_sharp.mrc\", please make sure you select Job from Homogeneous Refinement")

        # if it contains refined map
        if sharp_map:
            # print number of micrographs in the selected directory
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
    messagebox.showinfo("Select Path", "Select path you want to make a directory for processing")
    print("Select path you want to make a directory for processing")
    proc_path = filedialog.askdirectory(initialdir=raw_dir)
    messagebox.showinfo("name process directory", "name process directory on console, ex) process_Lsi1 ")
    print("name process directory on console, ex) process_Lsi1 ")
    # dir_new_name=tkinter.Entry(textvariable=tkinter.StringVar())
    dir_new_name = input()
    new_proc_path = proc_path + "/" + dir_new_name
    os.mkdir(new_proc_path)
    new_movie_dir = new_proc_path + "/" + "movie"
    os.mkdir(new_movie_dir)
    # make process and Movie directory
    path_list = [proc_path, new_proc_path, new_movie_dir]
    return path_list

def make_link(new_movie_dir, raw_mic):
    i=0
    for i in range(len(raw_mic)):
        name = raw_mic[i].split("/")
        dis = new_movie_dir + name[-1]
        os.symlink(raw_mic[i], dis)
        print(raw_mic[i])
        print(">>>>")
        print(dis)
        print("")
    print("made symbolic link!")

raw_dir = sel_raw_data()
raw_mic = get_raw_mic(raw_dir)
path_list = dir_maker(raw_dir)
proc_path = path_list[0]
new_proc_path = path_list[1]
new_movie_dir = path_list[2]+"/"
make_link(new_movie_dir, raw_mic)