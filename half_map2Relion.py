'''
#relionのmaskcreationに用いるディレクトリ(J30みたいな感じ)を選択すると
maskcreationにもちいるmrc file(sharp.mrc?)のpathを保存
そのhalf file2つも別のリストにpathを保存する
relionの解析ディレクトリのパスを選択する
2つのhalf fileを選択されたrelionの解析ディレクトリにcopyする
２つのcopyされたhalf fileの名前をrenameする
'''
import glob
import re
import shutil
import tkinter
from tkinter import messagebox, filedialog


def reedfile():
    # hide root window
    root = tkinter.Tk()
    root.withdraw()
    # select directory
    messagebox.showinfo("Select Job directory", "Select Job directory on Refinement from CryoSparc")
    while True:
        direc = filedialog.askdirectory()
        direc_sharp = direc + "/*sharp.mrc"
        direc_half = direc + "/**"
        sharp_map = glob.glob(direc_sharp)
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


def copy2relion(half_map):
    # hide root window
    root = tkinter.Tk()
    root.withdraw()
    # select destination
    messagebox.showinfo("Select destination", "Please select directory currently processing on Relion")
    destination = filedialog.askdirectory()
    destination_A = destination + "/run_half1_class001_until.mrc"
    destination_B = destination + "/run_half2_class001_until.mrc"

    # Copy half map from half_map and rename it for relion to destination path
    shutil.copy(half_map[0], destination_A)
    print("copied " + half_map[0] + " →→→→→" + "to " + destination + " and renamed to " + destination_A)
    shutil.copy(half_map[1], destination_B)
    print("copied " + half_map[1] + " →→→→→ " + "to " + destination + " and renamed to " + destination_B)


# main process
half_map = reedfile()
copy2relion(half_map)

print("done")
print("プログラムを終了しています")
