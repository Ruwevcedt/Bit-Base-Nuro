import Funcs
import ast

user = "ruwevcedt"


class Dir:
    Username = ""
    Maindir = ""
    Datadir = ""
    Metadir = ""
    Nodedir = ""
    LLinkdir = ""
    NLinkdir = ""
    
    def __init__(self, new_username):
        self.Maindir = "/home/{}/odor/".format(Username)
        self.Datadir = Maindir + "Datas/"
        self.Metadir = Datadir + "m/"
        self.Nodedir = Maindir + "Nodes/"
        self.LLinkdir = Maindir + "Links/Layers/"
        self.NLinkdir = Maindir + "Links/Nodes/"
        

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
        self.filepath = Dir(user).Datadir + self.filename
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
        self.mfilepath = Dir(user).Metadir + self.mfilepath
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = ast.literal_eval(mdatafile.readline())
            mdatafile.close()


class MetaMain(MetaDatas):
    I = []
    O = []

    def __init__(self, new_id, new_i):
        MetaDatas.__init__(self, new_id)
        self.I = new_i
        self.O = Funcs.andbbl_bl(self.mdata, self.I)


class MetaSub(MetaDatas):
    I = []
    O = []

    def __init__(self, new_id, new_i, n1, n2):
        MetaDatas.__init__(self, new_id)
        self.I = new_i
        self.O = Funcs.andbb_b(self.I[n1], self.mdata[n2])


class Updatas(Datas, MetaDatas):
    I = []

    def __init__(self, new_i):
        self.I = new_i
        with open(self.filepath, "w+") as datafile:
            self.data.append(self.I)
            datafile.write(self.data)
            datafile.close()
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = Funcs.sumaxxbs_bl(self.data)
            mdatafile.write(self.mdata)
            mdatafile.close()
        Datas.__init__(self, self.ID)
        MetaDatas.__init__(self, self.ID)


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
    # node[toid_nuron_num][fromid_nuron_num1, 2, ...]
    # if node[toid_nuron_num] == []:
    #   you should delete
    #       Datas(self.toID).data[all smplz][toid_nuron_num]
    #   and MetaDatas(self.toID).mdata[toid_nuron_num]

    def __init__(self, new_fromid, new_toid):
        InteLayer.__init__(self, new_fromid, new_toid)
        self.filename = "Node{}-{}.txt".format(new_fromid, new_toid)
        self.filepath = Dir(user).Nodedir + self.filename
        with open(self.filepath, "w+") as nodefile:
            self.node = ast.literal_eval(nodefile.readline())
            nodefile.close()


class Upnodes(Nodes):

    def __init__(self, new_fromid, new_toid, new_i):
        Nodes.__init__(self, new_fromid, new_toid)
        with open(self.filepath, "w+") as nodefile:
            nodefile.write(new_i)
            nodefile.close()


class Circuit:
    ID = 0

    def __init__(self, new_id):
        self.ID = new_id


class LayerLinks(Circuit):
    filename = ""
    filepath = ""
    layer_data = []
    # layer_data[sequence_num == dept1, 2, ...][self.dept_layer.id1, 2, ...]

    def __init__(self, new_id):
        Circuit.__init__(self, new_id)
        self.filename = "Link{}.txt".format(self.ID)
        self.filepath = Dir(user).LLinkdir + self.filename
        with open(self.filepath, "w+") as linkfile:
            self.layer_data = ast.literal_eval(linkfile.readline())
            linkfile.close()


class UpLlinks(LayerLinks):

    def __init__(self, new_id, new_i):
        LayerLinks.__init__(self, new_id)
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()


class NodeLinks(Circuit):
    filename = ""
    filepath = ""
    node_data = []
    # node_data[sequence_num == dept][self.dept_toid1, 2, ...][self.toid_fromid1, 2, ...]

    def __init__(self, new_id):
        Circuit.__init__(self, new_id)
        self.filename = "Link{}.txt".format(self.ID)
        self.filepath = Dir(user).NLinkdir + self.filename
        with open(self.filepath, "w+") as linkfile:
            self.node_data = ast.literal_eval(linkfile.readline())
            linkfile.close()


class UpNlinks(NodeLinks):

    def __init__(self, new_id, new_i):
        NodeLinks.__init__(self, new_id)
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()


class Base(LayerLinks, NodeLinks):
    CurQ = 0
    Dept = 0
    PreLayer_IDs = []
    CurLayer_IDs = []
    PosLayer_IDs = []

    PC_IntLyr = []
    CP_IntLyr = []

    def __init__(self, new_id):
        LayerLinks.__init__(self, new_id)
        NodeLinks.__init__(self, new_id)
        self.Dept = len(self.layer_data)
        self.PreLayer_IDs = []
        self.CurLayer_IDs = self.layer_data[0]
        self.PosLayer_IDs = self.layer_data[1]

        self.PC_IntLyr = []
        self.CP_IntLyr = self.node_data[0]


class Main(Base):
    I = []
    O = []

    def step(self):
        self.CurQ += 1
        self.PreLayer_IDs = self.CurLayer_IDs
        self.CurLayer_IDs = self.PosLayer_IDs
        self.PosLayer_IDs = self.layer_data[self.CurQ + 1]

        self.PC_IntLyr = self.CP_IntLyr
        self.CP_IntLyr = self.node_data[self.CurQ]

    def start(self):
        curlyr_mem = []

        for l_id in self.CurLayer_IDs:
            curlyr_mem.append(MetaMain(l_id, self.I).O)

        self.step()
        return curlyr_mem
    # mem[output1, 2, ... sorted by curlayer_ids]

    def preflash(self, prelyr_mem):
        curlyr_mem = []

        for fid in self.CurLayer_IDs:
            temp_hi = []
            for toid in self.CP_IntLyr[fid]:
                node = Nodes(fid, toid).node
                temp_push = []

                for to_nur in node:
                    num_tonur = float(len(node[to_nur]))
                    temp_push = [0] * num_tonur
                    for from_nur in node[to_nur]:
                        temp_push[from_nur] += Funcs.andbb_b(prelyr_mem[self.PreLayer_IDs.index(fid)][from_nur], node[to_nur][from_nur])
                    if temp_push >= num_tonur / 2:
                        temp_hi.append(True)
                    else:
                        temp_hi.append(False)

                temp_hi.append(temp_push)
            curlyr_mem.append(temp_hi)

        return curlyr_mem
    # mem[fromid1, 2, ... sorted by curlayer_ids][hidden input for toid1, 2, ... sorted by cp_intlyr]

    def flash(self, curlyr_mem):
        
