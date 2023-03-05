import glob
import pathlib
import subprocess
from tkinter import messagebox


class ImportRelion:
    def __init__(self, proc_path, kv, inp, gainref=False, software=0, optic_group_name="opticsGroup1",
                 beamtile_x="0",
                 beamtile_y="0",
                 ofile="movies.star"):
        self.gainref = gainref
        if self.gainref:
            # odir = "Import/importgainref"
            odir = "imported_gainref"
        if not self.gainref:
            odir = "imported_mic"
        self.odir = "Import/" + odir
        if software == 1:  # JADAS
            self.input = inp + "*FrameImage.tif"
            if kv == 200:
                self.angpix = 0.854
            else:
                self.angpix = 0.752
        elif software == 2:  # EPU
            self.input = inp + "*Fractions.mrc"
            if kv == 200:
                self.angpix = 1.228
            else:
                print("please input pix cell size")
                self.angpix = int(input("pixel size (A)>>>"))
        elif software == 3:
            self.input = inp + "*.tif"
            if kv == 200:
                self.angpix = 0.849
            else:
                print("please input pix cell size")
                self.angpix = int(input("pixel size (A)>>>"))
        else:
            print("failed to detect software. please input pixel size manually")
            messagebox.showinfo("failed to detect software", "failed to detect software.please input pixel size "
                                                             "manually")
            self.angpix = int(input("pixel size (A)>>>"))
        pwd = pathlib.Path(proc_path)
        path = pathlib.Path(self.input)
        # self.input = "\\" + "\"" + str(path.relative_to(pwd)) + "\\" + "\""
        self.input = "\"" + str(path.relative_to(pwd)) + "\""
        self.kv = str(kv)
        self.angpix = str(self.angpix)
        self.Cs = "2.7"
        self.do_movies = "--do_movies"
        self.optic_group_name = optic_group_name
        self.Q0 = "0.1"
        self.beamtilt_x = beamtile_x
        self.beamtilt_y = beamtile_y
        # import_mic, import_gainref
        self.ofile = ofile
        self.pipeline_control = "Import/"

    def import2relion(self):
        # voltage =
        # subprocess.run(["relion", "&"])
        command = ["relion_import", self.do_movies, "--optics_group_name", self.optic_group_name, "--angpix",
                   self.angpix, "--kV", self.kv, "--Cs",
                   self.Cs, "--Q0",
                   self.Q0, "--beamtilt_x", self.beamtilt_x, "--beamtilt_y", self.beamtilt_y, "--i", self.input,
                   "--odir", self.odir, "--ofile", self.ofile, "--pipeline_control", self.pipeline_control]
        command_line = (
                "relion_import " + self.do_movies + " --optics_group_name " + self.optic_group_name + " --angpix " +
                self.angpix + " --kV " + self.kv + " --Cs " +
                self.Cs + " --Q0 " + self.Q0 + " --beamtilt_x " + self.beamtilt_x + " --beamtilt_y " +
                self.beamtilt_y + " --i " + self.input +
                " --odir " + self.odir + " --ofile " + self.ofile + " --pipeline_control " + self.pipeline_control)
        print(command_line)
        subprocess.run(command_line, shell=True)
        input_for_gainref = self.odir + self.ofile
        return input_for_gainref


def JEOL_num(direc):
    """
    determine which software is used for the data acquisition
    :param direc: path for the directory store raw data
    :return: return 1 for JADAS, 2 for EPU and 3 for SerialEM
    """
    direc_raw = direc + "/*FrameImage.tif"
    # direc_half = direc + "/**"
    sharp_map = glob.glob(direc_raw)
    # if selected directory doesn't contain refined mrc map
    if not sharp_map:
        direc_raw = direc + "/Frames/supervisor*/Image*/GridSquare*/Data/*Fractions.mrc"
        sharp_map = glob.glob(direc_raw)
        if sharp_map:  # EPU
            software = 2
            print("Loaded data obtained with EPU from ThermoScientific")
            return software
        if not sharp_map:
            direc_raw = direc + "*.tif"
            sharp_map = glob.glob(direc_raw)
            if sharp_map:  # SerialEM
                software = 3
                print("Loaded data obtained with SerialEM")
                return software
    # if it contains raw data
    if sharp_map:  # JADAS
        # print number of micrographs in the selected directory
        # return boolean class True for JEOL, False for Thermo
        software = 1
        print("Loaded data of JADAS")
        return software


def ask_kv():
    kv_bl = messagebox.askquestion("Select voltage", "Would you like to set voltage \"300kV\"?"
                                                     "  Click No for \"200kV\"")
    if kv_bl == True:
        voltage = 300
    else:
        voltage = 200
    return voltage
