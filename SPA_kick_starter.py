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

def sel_raw_data()