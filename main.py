from AppConfigs.FileManagement import Management
from AppStatics.StaticMethods import StaticMethods
from AppStatics.StaticValues import StaticValues
import time,os
class Program():
    def __init__(self):
        print("EXPENSE TRACKER")  
        self.Login()
        os.system("cls")
        print("Access Granted")

    def Login(self):
        os.system("cls")
        while True:
            if StaticValues.LOGIN_ATTEMPTS <= 5:
                if StaticMethods.ValidInteger("Insert Pin: ",9999) == int(Management.GetInfo("PIN")): return
                else: print("Incorrect PIN");StaticValues.LOGIN_ATTEMPTS+=1
            else: 
                print("Too Many Failed Attempts")
                time.sleep(0.3)
                StaticValues.BLOCK = True
                self.Block()
                break

    def Block(self):
        while StaticValues.BLOCK:
            os.system("cls")
            print(f"You've been blocked! Please wait {StaticValues.BLOCK_TIME} seconds") 
            time.sleep(1)
            if StaticValues.BLOCK_TIME == 0 :
                StaticValues.BLOCK = False
                StaticValues.LOGIN_ATTEMPTS = 0
                StaticValues.BLOCK_TIME += (StaticValues.CURRENT_BLOCK_TIME*2)
                StaticValues.CURRENT_BLOCK_TIME = StaticValues.BLOCK_TIME
                break
            else:
                StaticValues.BLOCK_TIME -= 1
        Program()
Program()

