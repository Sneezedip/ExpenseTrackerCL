import tempfile,os,os.path
class Management():
    DEFAULT_CONFIGURATIONS = "AUTO_LOGIN:False\nPIN:{0}\nMONEY:0\nCURRENT_MONTH:0\nBUDGET:0\nHISTORY:"
    CONFIG_LOCATION = tempfile.gettempdir()+"\\FileManagement.cfg"
    def CheckConfigs():
        if os.path.isfile(Management.CONFIG_LOCATION): return True
        else: return False
    def GetInfo(Type):
        if not Management.CheckConfigs(): 
            with open (Management.CONFIG_LOCATION,"w") as file: file.write(Management.DEFAULT_CONFIGURATIONS.format("DEFAULT"))
        with open (Management.CONFIG_LOCATION,"r") as file:
            for line in file.readlines():
                separated = line.split(":")
                if separated[0] == Type: return separated[1].strip()
    def ChangePIN(isnew=False):
        while True:
            if isnew:
                NEW = str(input("You dont have any pin set.\n Insert A New Pin: "))
                if len(NEW) == 4:
                    try:
                        with open (Management.CONFIG_LOCATION,"w") as file: file.write(Management.DEFAULT_CONFIGURATIONS.format(int(NEW)))
                        os.system("cls")
                        print("New PIN Set! ",NEW)
                        return          
                    except:
                        print("Pin is only numeric.")
                else:
                    print("Pin need to have 4 digits.")
            else:
                OLD = str(input("Insert your old PIN: "))
                if len(OLD) == 4:
                    if OLD == Management.GetInfo("PIN"):
                        while True:
                            NEW = input("Insert A new PIN: ")
                            wrong = False
                            if len(NEW) == 4:
                                with open(Management.CONFIG_LOCATION, 'r') as file:
                                    lines = file.readlines()
                                for i, line in enumerate(lines):
                                    if 'PIN' in line:
                                        try:
                                            lines[i] = f"PIN:{int(NEW)}\n"
                                            wrong = False
                                            break
                                        except:
                                            print("PIN is only numeric.")
                                            wrong = True
                                if not wrong:
                                    break
                            else:
                                print("PIN has to have 4 digits")
                        with open(Management.CONFIG_LOCATION, 'w') as file:
                            file.writelines(lines)
                        os.system("cls")
                        print("NEW PIN Set! ",NEW)
                        return     
                    else:
                        print("Pin doesn't match with old pin.")         
                else:
                    print("Pin need to have 4 digits.")        


