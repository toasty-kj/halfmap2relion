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
                print("input pix cell size")
                self.angpix = input("pixel size >>>")
        self.cs = 2.7

    def JEOL_boolean(self, ):