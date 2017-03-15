import Nain
import ast

Username = "ruwevcedt"
Maindir = "/home/{}/odor/".format(Username)
Datadir = Maindir + "Datas/"
Metadir = Datadir + "m/"
Nodedir = Maindir + "Nodes/"
LLinkdir = Maindir + "Links/Layers/"
NLinkdir = Maindir + "Links/Nodes/"


class Layer:
    ID = 0

    def __init__(self, new_id):
        self.ID = new_id


class Datas(Layer):
    filename = ""
    filepath = ""
    data = []
    # data[dataset_num1, 2, ...][data_num == nuron_num1, 2, ...]

    def __init__(self, new_id):
        Layer.__init__(self, new_id)
        self.filename = "Data{}.txt".format(self.ID)
        self.filepath = Datadir + self.filename
        with open(self.filepath, "w+") as datafile:
            self.data = ast.literal_eval(datafile.readline())
            datafile.close()


class MetaDatas(Layer):
    mfilename = ""
    mfilepath = ""
    mdata = []
    # mdata[nuron_num1, 2, ...]

    def __init__(self, new_id):
        Layer.__init__(self, new_id)
        self.mfilename = "mData{}.txt".format(new_id)
        self.mfilepath = Metadir + self.mfilepath
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = ast.literal_eval(mdatafile.readline())
            mdatafile.close()


class MetaMain(MetaDatas):
    I = []
    O = []

    def __init__(self, new_id, new_i):
        MetaDatas.__init__(self, new_id)
        self.I = new_i
        self.O = Nain.andbbl_bl(self.mdata, self.I)


class InteLayer:
    FromID = 0
    ToID = 0

    def __init__(self, new_fromid, new_toid):
        self.FromID = new_fromid
        self.ToID = new_toid


class Nodes(InteLayer):
    filename = ""
    filepath = ""
    node = []
    # node [toid nuron num1, 2, 3, ...][fid nuron number1, 2, ...]
    #
    # if node[toid_nuron_num] == []:
    #   you should delete
    #       Datas(self.toID).data[toid_nuron_num]
    #       MetaDatas(self.toID).mdata[toid_nuron_num]
    #       node[toid_nuron_num]

    def __init__(self, new_fromid, new_toid):
        InteLayer.__init__(self, new_fromid, new_toid)
        self.filename = "Node{}-{}.txt".format(new_fromid, new_toid)
        self.filepath = Nodedir + self.filename
        with open(self.filepath, "w+") as nodefile:
            self.node = ast.literal_eval(nodefile.readline())
            nodefile.close()


class Circuit:
    ID = 0

    def __init__(self, new_id):
        self.ID = new_id


class LayerLinks(Circuit):
    filename = ""
    filepath = ""
    llink = []
    # layer_data[sequence_num == dept1, 2, ...][self.dept_layer.id1, 2, ...]

    def __init__(self, new_id):
        Circuit.__init__(self, new_id)
        self.filename = "Link{}.txt".format(self.ID)
        self.filepath = LLinkdir + self.filename
        with open(self.filepath, "w+") as linkfile:
            self.llink = ast.literal_eval(linkfile.readline())
            linkfile.close()


class NodeLinks(Circuit):
    filename = ""
    filepath = ""
    nlink = []
    # node_data[sequence_num == dept][(fromid, toid)1, ()2, ...]

    def __init__(self, new_id):
        Circuit.__init__(self, new_id)
        self.filename = "Link{}.txt".format(self.ID)
        self.filepath = NLinkdir + self.filename
        with open(self.filepath, "w+") as linkfile:
            self.nlink = ast.literal_eval(linkfile.readline())
            linkfile.close()


class Base(LayerLinks, NodeLinks):
    CurQ = 0
    Dept = 0

    PreLayer_IDs = []
    CurLayer_IDs = []

    PC_IntLyr = []
    CP_IntLyr = []

    def __init__(self, new_id):
        LayerLinks.__init__(self, new_id)
        NodeLinks.__init__(self, new_id)
        self.Dept = len(self.llink) - 1
        self.PreLayer_IDs = []
        self.CurLayer_IDs = self.llink[0]

        self.PC_IntLyr = []
        self.CP_IntLyr = self.nlink[0]


class Main(Base):
    I = {}
    O = {}

    def step(self):
        self.CurQ += 1
        self.PreLayer_IDs = self.CurLayer_IDs
        self.CurLayer_IDs = self.llink[self.CurQ]

        self.PC_IntLyr = self.CP_IntLyr
        self.CP_IntLyr = self.nlink[self.CurQ]

    def start(self):
        curlyr_mem = {}

        for lyrid in self.CurLayer_IDs:
            curlyr_mem[lyrid] = MetaMain(lyrid, self.I[lyrid]).O

        self.step()
        return curlyr_mem

    def preflash(self, prelyr_mem):
        hinput_mem = {}

        for (fid, toid) in self.PC_IntLyr:
            hinput = Nain.pushblis_bl(prelyr_mem[fid], Nodes(fid, toid).node)
            if toid in hinput_mem:
                hinput_mem[toid].append(hinput)
            else:
                hinput_mem[toid] = [hinput]
        for toids in hinput_mem:
            hinput_mem[toids] = Nain.sumaxxbs_bl(hinput_mem[toids])

        return hinput_mem

    def flash(self, curlyr_mem):
        houtput_mem = {}

        for lyrid in self.CurLayer_IDs:
            houtput_mem[lyrid] = MetaMain(lyrid, curlyr_mem[lyrid])

        self.step()
        return houtput_mem

    def __init__(self, new_id, new_i):
        Base.__init__(self, new_id)
        self.I = new_i
        output = self.start()
        while self.CurQ != self.Dept:
            output = self.flash(self.preflash(output))
        self.O = output
