import subprocess


class MorrtionCorr:
    def __init__(self, i, gainref, j=12, bin_factor=1, path_x=5, path_y=5):
        self.i = i
        self.out = "MotionCorr/"
        self.first_frame_sum = str(1)
        self.last_frame_sum = str(-1)
        self.j = str(j)
        self.bin_factor = str(bin_factor)
        self.bin_factor = str(1)
        self.bfactor = str(150)
        self.dose_per_frame = str(1)
        self.preexposure = str(0)
        self.patch_x = str(path_x)
        self.patch_y = str(path_y)
        self.eer_grouping = str(32)
        self.gainref = gainref
        self.gain_rot = str(0)
        self.gain_flip = str(0)
        self.grouping_for_ps = str(4)
        self.pipeline_control = self.out

    def correctMotion(self):
        # os.mkdir()
        command_line = ("`which relion_run_motioncorr_mpi` --i " + self.i + " --o " + self.out + " --first_frame_sum "
                        + self.first_frame_sum + " --last_frame_sum " + self.last_frame_sum + " --use_own --j " + self.j
                        + " --float16 --bin_factor " + self.bin_factor + " --bfactor " + self.bfactor + " --dose_per_frame " + self.dose_per_frame
                        + " --preexposure " + self.preexposure + " --patch_x " + self.patch_x + " --patch_y " + self.patch_y
                        + " --eer_grouping " + self.eer_grouping + " --gainref " + self.gainref + " --gain_rot " + self.gain_rot
                        + " --gain_flip " + self.gain_flip + " --dose_weighting --grouping_for_ps " + self.grouping_for_ps
                        + " --pipeline_control " + self.pipeline_control)
        print(command_line)
        subprocess.run(command_line, shell=True)
        motcorr_path = self.out + "corrected_micrographs.star"
        return motcorr_path
