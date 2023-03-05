import subprocess


class GainRef:
    def __init__(self, inp, j=12):
        self.input = inp
        self.j = str(j)

    def estimate_gain(self):
        command_line = "relion_estimate_gain --i " + self.input + " --o gainref.mrc --j " + self.j
        print(command_line)
        subprocess.run(command_line, shell=True)
