import Funcs

Username = "ruwevcedt"
Maindir = "/home/{}/odor/".format(Username)
Datadir = Maindir + "Datas/"
Metadir = Datadir + "m/"
Nodedir = Maindir + "Nodes/"
Linkdir = Maindir + "Links/"


class Layer:
    ID = 0

    def __init__(self, new_id):
        self.ID = new_id


class Datas(Layer):
    filename = ""
    filepath = ""
    data = []

    def __init__(self, new_id):
        Layer.__init__(self, new_id)
        self.filename = "Data{}.txt".format(self.ID)
        self.filepath = Datadir + self.filename
        with open(self.filepath, "w+") as datafile:
            self.data = Funcs.ridt_bs(datafile.readline())
            datafile.close()


class MetaDatas(Layer):
    mfilename = ""
    mfilepath = ""
    mdata = []

    def __init__(self, new_id):
        Layer.__init__(self, new_id)
        self.mfilename = "mData{}.txt".format(new_id)
        self.mfilepath = Metadir + self.mfilepath
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = Funcs.ridt_bs(mdatafile.readline())
            mdatafile.close()


class MetaMain(MetaDatas):
    I = []
    O = []

    def metamain(self):
        self.O = Funcs.andbbl_bl(self.mdata, self.I)

    def metasub(self, n1, n2):
        self.O = Funcs.andbb_b(self.mdata[n1], self.I[n2])

    def __init__(self, new_id, new_i):
        MetaDatas.__init__(self, new_id)
        self.I = new_i
        self.O = []


class Updatas(Datas, MetaDatas):
    I = []

    def __init__(self, new_i):
        self.I = new_i
        Datas.__init__(self, self.ID)
        MetaDatas.__init__(self, self.ID)
        with open(self.filepath, "w+") as datafile:
            self.data.append(self.I)
            datafile.write(self.data)
            datafile.close()
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = Funcs.sumaxxbs_bl(self.data)
            mdatafile.write(self.mdata)
            mdatafile.close()


class InteLayer:
    FromID = 0
    ToID = 0

    def __init__(self, new_fromid, new_toid):
        self.FromID = new_fromid
        self.ToID = new_toid


class Nodes(InteLayer):
    filename = ""
    filepath = ""
    node = [[]]

    def __init__(self, new_fromid, new_toid):
        InteLayer.__init__(self, new_fromid, new_toid)
        self.filename = "Node{}-{}.txt".format(new_fromid, new_toid)
        self.filepath = Nodedir + self.filename
        with open(self.filepath, "w+") as nodefile:
            self.node = Funcs.ridt_bs(nodefile.readline())
            nodefile.close()
