import os

import GainRef_relion
import Import_relion
import MortionCorr
import Preprocessing

"""
take raw data acquired from CryoEM for Single Particle Analysis (select on GUI)
make directory for processing (make movie directory under process directory)
Then link data from original directory containing raw data.
Finally, run relion and make gainref file (import linked data and data for gainref, then produce gainref through relion).
(you can proceed to motion correction on relion if Yes.)
"""
Preprocessing.print_sep()
raw_dir = Preprocessing.sel_raw_data()  # select path od directory for obtained data
soft = Import_relion.JEOL_num(raw_dir)  # determine machine manufacturer and return True for JEOL and False for Thermo
raw_mic = Preprocessing.get_raw_mic(raw_dir, soft)  # get a list with path of each micrographs
Preprocessing.print_sep()
path_list = Preprocessing.dir_maker(
    raw_dir)  # generate processing, "movie" and "gainref" directory under selected directory
proc_path = path_list[0]  # selected directory processing directory is made
new_proc_path = path_list[1]  # path of processing directory
new_movie_dir = path_list[2]  # path of "movie" directory under processing directory
new_gainref_dir = path_list[3]  # path of "gainref" directory under processing directory
os.chdir(
    new_proc_path)  # set processing directory as working directory since it avoid making error when you import data
Preprocessing.print_sep()
Preprocessing.make_link(new_movie_dir, raw_mic)  # make symbolic for movie directory
Preprocessing.make_link(new_gainref_dir, raw_mic, 1000)  # make the link for gainref directory up to 1,000 mics
Preprocessing.print_sep()
voltage = Import_relion.ask_kv()  # set accelerating voltage for import
param = Import_relion.ImportRelion(new_proc_path, kv=voltage, inp=new_movie_dir, gainref=False, software=soft)
os.mkdir(new_proc_path + "/" + "Import" + "/")  # generate "Import" directory under processing directory
input_for_proc = param.import2relion()  # import raw data for relion
Preprocessing.print_sep()
gainref_param = Import_relion.ImportRelion(new_proc_path, kv=voltage, inp=new_movie_dir, gainref=True, software=soft)
input_for_gainref = gainref_param.import2relion()  # import raw data for gainref for relion
Preprocessing.print_sep()
gainref = GainRef_relion.GainRef(input_for_gainref, 24)  # estimate gainref, default number of thread is 12
gainref.estimate_gain()
Preprocessing.print_sep()
motionCorr_param = MortionCorr.MorrtionCorr(input_for_proc, "gainref.mrc")
motionCorr_param.correctMotion()
Preprocessing.print_sep()
