from AppConfigs.FileManagement import Management
from AppStatics.StaticMethods import StaticMethods
from AppConfigs.AppUsage import Usage
from AppStatics.StaticValues import StaticValues
import time,os
class Program():
    def __init__(self):
        self.Login()
        self.Menu()
        
    def Menu(self):
        while True:
            os.system("cls")
            print(f"""
            {StaticMethods.Centered("Balance: "+Management.GetInfo("MONEY")+"€")}
            {StaticMethods.Centered("This Month: "+Management.GetInfo("CURRENT_MONTH")+"€")}
            {StaticMethods.Centered("Budget: "+Management.GetInfo("BUDGET")+"€")}

            {StaticMethods.Centered("[1] - View Account Settings")}
            """)

            CHOICE = StaticMethods.ValidInteger("-> ",1,1,notify_Exception=True)

            match CHOICE:
                case 1: self.AccountSettings()
    def AccountSettings(self):
        os.system("cls")
        print(f"""
        {StaticMethods.Centered("Account Settings")}
        \n
        {StaticMethods.Centered("[1] - Add Balance")}
        {StaticMethods.Centered("[2] - Set Budget")}
        """)
        CHOICE = StaticMethods.ValidInteger("-> ",2,1,notify_Exception=True)
        match CHOICE:
                case 1: Usage.BalanceModifier(True)
                case 2: Usage.SetBudget()
        return
    def Login(self):
        os.system("cls")
        while True:
            if Management.GetInfo("PIN") == "DEFAULT":
                Management.ChangePIN()
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

