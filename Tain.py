import Main
import Funcs


class Updatas(Main.Datas, Main.MetaDatas):
    data_bef = []
    data_aft = []

    mdata_bef = []
    mdata_aft = []

    def __init__(self, new_id, new_i):
        Main.Datas.__init__(self, new_id)
        self.data_bef = self.data
        Main.MetaDatas.__init__(self, new_id)
        self.mdata_bef = self.mdata
        with open(self.filepath, "w+") as datafile:
            self.data = new_i
            datafile.write(self.data)
            datafile.close()
        self.data_aft = self.data
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = Funcs.sumaxxbs_bl(self.data)
            mdatafile.write(self.mdata)
            mdatafile.close()
        self.mdata_aft = self.mdata


class Upnodes(Main.Nodes):
    node_bef = []
    node_aft = []

    def __init__(self, new_fromid, new_toid, new_i):
        Main.Nodes.__init__(self, new_fromid, new_toid)
        self.node_bef = self.node
        with open(self.filepath, "w+") as nodefile:
            nodefile.write(new_i)
            nodefile.close()
        self.node_aft = self.node


class UpLlinks(Main.LayerLinks):
    llink_bef = []
    llink_aft = []

    def __init__(self, new_id, new_i):
        Main.LayerLinks.__init__(self, new_id)
        self.llink_bef = self.llink
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()
        self.llink_aft = self.llink


class UpNlinks(Main.NodeLinks):
    nlink_bef = []
    nlink_aft = []

    def __init__(self, new_id, new_i):
        Main.NodeLinks.__init__(self, new_id)
        self.nlink_bef = self.nlink
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()
        self.nlink_aft = self.nlink

