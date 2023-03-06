import pathlib
import subprocess


class CTFfind:
    def __init__(self, i, out, pwd, Box=512, ResMin=30, ResMax=5, dFMin=5000, dFMax=50000, FStep=500,
                 dAst=100, ctfWin=-1):
        self.i = i
        self.o = out
        self.Box = str(Box)
        self.ResMin = str(ResMin)
        self.ResMax = str(ResMax)
        self.dFMin = str(dFMin)
        self.dFMax = str(dFMax)
        self.FStep = str(FStep)
        self.dAsp = str(dAst)
        pwd = pathlib.Path(pwd)
        path = pathlib.Path("/home/pub/ctffind-4.1.14/bin/ctffind")
        self.ctffind_exe = str(path.relative_to(pwd))
        #
        print(self.ctffind_exe)
        self.ctfwin = str(ctfWin)
        self.pipeline_control = out

    def ctffind(self):
        command_line = ("`which relion_run_ctffind_mpi` --i " + self.i + " --o " + self.o + " --Box "
                        + self.Box + " --ResMin " + self.ResMin + " --ResMax " + self.ResMax
                        + " --dFMin " + self.dFMin + " --dFMax " + self.dFMax
                        + " --FStep " + self.FStep + " --dAst_x " + self.dAsp + " --ctffind4_exe " + self.ctffind_exe
                        + " --ctfWin " + self.ctfwin + " --is_ctffind4 --use_given_ps --pipeline_control"
                        + self.pipeline_control)
        print(command_line)
        subprocess.run(command_line, shell=True)
