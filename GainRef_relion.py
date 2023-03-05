import subprocess


class GainRef:
    def __init__(self, inp, j=12):
        """
        params for estimate gainref
        :param inp: path for imported data for the estimation
        :param j: number of threads of CPU, default is 12
        """
        self.input = inp
        self.j = str(j)

    def estimate_gain(self):
        """
        estimate gainref
        """
        command_line = "relion_estimate_gain --i " + self.input + " --o gainref.mrc --j " + self.j
        print(command_line)
        subprocess.run(command_line, shell=True)
