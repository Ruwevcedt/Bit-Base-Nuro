import Main
import Funcs


class Updatas(Main.Datas, Main.MetaDatas):

    def __init__(self, new_id, new_i):
        Main.Datas.__init__(self, new_id)
        Main.MetaDatas.__init__(self, new_id)
        with open(self.filepath, "w+") as datafile:
            self.data = new_i
            datafile.write(self.data)
            datafile.close()
        with open(self.mfilepath, "w+") as mdatafile:
            self.mdata = Funcs.sumaxxbs_bl(self.data)
            mdatafile.write(self.mdata)
            mdatafile.close()


class Upnodes(Main.Nodes):

    def __init__(self, new_fromid, new_toid, new_i):
        Main.Nodes.__init__(self, new_fromid, new_toid)
        with open(self.filepath, "w+") as nodefile:
            nodefile.write(new_i)
            nodefile.close()


class UpLlinks(Main.LayerLinks):

    def __init__(self, new_id, new_i):
        Main.LayerLinks.__init__(self, new_id)
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()


class UpNlinks(Main.NodeLinks):

    def __init__(self, new_id, new_i):
        Main.NodeLinks.__init__(self, new_id)
        with open(self.filepath, "w+") as linkfile:
            linkfile.write(new_i)
            linkfile.close()

