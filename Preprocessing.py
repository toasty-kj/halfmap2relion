import glob
import os
import tkinter
from tkinter import messagebox, filedialog


def sel_raw_data():
    """
    select path of a directory with raw data
    :return: path of the directory raw data in it
    """
    # hide root window
    root = tkinter.Tk()
    root.withdraw()
    # select directory
    messagebox.showinfo("Select directory containing raw data", "Select Directory containing raw data")
    while True:

        direc = filedialog.askdirectory(initialdir="/media/")
        direc_raw = direc + "/*FrameImage.tif"
        # direc_half = direc + "/**"
        sharp_map = glob.glob(direc_raw)
        # if selected directory doesn't contain refined mrc map
        if not sharp_map:
            direc_raw = direc + "/Frames/supervisor*/Image*/GridSquare*/Data/*Fractions.mrc"
            sharp_map = glob.glob(direc_raw)
            if sharp_map:  # EPU
                print("loaded successfully!")
                print("loaded " + str(len(sharp_map)) + " micrographs")
                messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!! "
                                                            "loaded " + str(len(sharp_map)) + " micrographs")
                return direc
            if not sharp_map:
                direc_raw = direc + "*.tif"
                sharp_map = glob.glob(direc_raw)
                if sharp_map:  # SerialEM
                    print("loaded successfully!")
                    print("loaded " + str(len(sharp_map)) + " micrographs")
                    messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!! "
                                                                "loaded " + str(len(sharp_map)) + " micrographs")
                    return direc
            if not sharp_map:
                print(
                    "couldn't find \"FrameImage.tif\", please make sure you select directory with raw data")
                messagebox.showerror("couldn't find file !!",
                                     "couldn't find \"FrameImage.tif\" , \"Fractions.mrc\" or \"*.tif\", please make sure you raw data is contained in the selected directory")
        # if it contains raw data
        if sharp_map:  # JADAS
            # print number of micrographs in the selected directory

            print("loaded successfully!")
            print("loaded " + str(len(sharp_map)) + " micrographs")
            messagebox.showinfo("Loaded Successfully!", "Loaded Successfully!! "
                                                        "loaded " + str(len(sharp_map)) + " micrographs")
            # return list stored two path(both half map)
            return direc
            break


def get_raw_mic(raw_dir, jeol):
    """
    get FrameImage.tif from variable raw data format
    :param raw_dir: selected directory with raw data
    :return: list of FrameImage.tif
    """
    if jeol == True:
        direc_raw = raw_dir + "/*FrameImage.tif"
    else:
        direc_raw = raw_dir + "/Frames/supervisor*/Image*/GridSquare*/Data/*Fractions.mrc"
    # direc_half = raw_dir + "/**"
    sharp_map = glob.glob(direc_raw)
    return sharp_map


def dir_maker(raw_dir):
    """
    Select destination which actual processing will be conducted
    :param raw_dir: selected directory with raw data
    :return: a list contains path of directory process file is made, process file, movie file under the process file, and gain reference file in this order.
    """
    messagebox.showinfo("Select Path", "Select path you want to make a directory for processing")
    print("Select path you want to make a directory for processing")
    proc_path = filedialog.askdirectory(initialdir=raw_dir)
    print(raw_dir)
    messagebox.showinfo("name process directory", "name process directory on console, ex) process_Lsi1 ")
    print("name process directory on console, ex) process_Lsi1 ")
    # dir_new_name=tkinter.Entry(textvariable=tkinter.StringVar())
    dir_new_name = input()
    new_proc_path = proc_path + "/" + dir_new_name
    os.mkdir(new_proc_path)
    new_movie_dir = new_proc_path + "/" + "movie" + "/"
    os.mkdir(new_movie_dir)
    print("made " + "\"movie\"" + " directory")
    new_gainref_dir = new_proc_path + "/" + "gainref" + "/"
    os.mkdir(new_gainref_dir)
    print("made " + "\"gainref\"" + " directory")
    # make process and Movie directory
    path_list = [proc_path, new_proc_path, new_movie_dir, new_gainref_dir]
    return path_list


def make_link(new_movie_dir, raw_mic, limit=999999999):
    """
    make symbolic link
    :param new_movie_dir: path of movie directory under process directory
    :param raw_mic: list of FramaImage.tif
    :param limit: limit of number of micrograph used for the link, the limit is used for gain reference file
    """
    if limit < len(raw_mic):
        n = limit
    else:
        n = len(raw_mic)
    i = 0
    for i in range(n):
        name = raw_mic[i].split("/")
        dis = new_movie_dir + name[-1]
        os.symlink(raw_mic[i], dis)
        """print(raw_mic[i])
        print(">>>>")
        print(dis)
        print("")
        """

    print("made symbolic link!")


def print_sep():
    """
    print separation between main functions
    """
    print("-----------------------------------------------")


def further_proc():
    furproc = messagebox.askquestion("Further analysis",
                                     "Would you proceed to further analysis on RELION after estimation of "
                                     "gainref? "
                                     "If you choose \"Yes\", automatically proceed to Motioncorrection and "
                                     "CTF estimation after the estimation")
    return furproc
