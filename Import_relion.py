import glob
from tkinter import messagebox


class Import2Relion:
    def __int__(self, kv, input, output, JEOL=True):
        self.kv = kv
        self.input = input
        self.output = output
        if JEOL == True:
            if kv == 200:
                self.angpix = 0.854
            else:
                self.angpix = 0.752
        elif JEOL == False:
            if kv == 200:
                self.angpix = 1.228
            else:
                print("please input pix cell size")
                self.angpix = input("pixel size >>>")
        self.cs = 2.7

    def JEOL_boolean(self, direc):
        direc_raw = direc + "/*FrameImage.tif"
        # direc_half = direc + "/**"
        sharp_map = glob.glob(direc_raw)
        # if selected directory doesn't contain refined mrc map
        if not sharp_map:
            direc_raw = direc + "/Frames/supervisor*/Image*/GridSquare*/Data/*Fractions.mrc"
            sharp_map = glob.glob(direc_raw)
            if sharp_map:
                JEOL = False
                print("Loaded data of Thermo Scientific")
                return JEOL
            if not sharp_map:
                print(
                    "couldn't find \"FrameImage.tif\", please make sure you select Job from Homogeneous Refinement")
                messagebox.showerror("cound't find file !!",
                                     "couldn't find \"FrameImage.tif\" or \"Fractions.mrc\", please make sure you select Job from Homogeneous Refinement")
        # if it contains raw data
        if sharp_map:
            # print number of micrographs in the selected directory
            # return boolean class True for JEOL, False for Thermo
            JEOL = True
            print("Loaded data of JEOL")
            return JEOL
