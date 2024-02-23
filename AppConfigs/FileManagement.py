import tempfile,os,os.path
class Management():
    DEFAULT_CONFIGURATIONS = "AUTO_LOGIN:False\nPIN:1234"
    CONFIG_LOCATION = tempfile.gettempdir()+"\\FileManagement.cfg"
    def CheckConfigs():
        if os.path.isfile(Management.CONFIG_LOCATION): return True
        else: return False
    def GetInfo(Type):
        if not Management.CheckConfigs(): 
            with open (Management.CONFIG_LOCATION,"w") as file: file.write(Management.DEFAULT_CONFIGURATIONS)
        with open (Management.CONFIG_LOCATION,"r") as file:
            for line in file.readlines():
                separated = line.split(":")
                if separated[0] == Type: return separated[1].strip()
