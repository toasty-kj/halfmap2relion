import glob
import subprocess
from tkinter import messagebox


class Import2Relion:
    def __int__(self, kv, input, output, software=0):
        self.kv = kv
        self.input = input
        self.output = output
        if software == 1:
            if kv == 200:
                self.angpix = 0.854
            else:
                self.angpix = 0.752
        elif software == 2:
            if kv == 200:
                self.angpix = 1.228
            else:
                print("please input pix cell size")
                self.angpix = int(input("pixel size (A)>>>"))
        elif software == 3:
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

        self.cs = 2.7

    def JEOL_num(self, direc):
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

    def import2relion(self, ):
        # voltage =
        subprocess.run([])
