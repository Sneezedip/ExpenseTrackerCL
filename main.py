from AppConfigs.FileManagement import Management
from AppStatics.StaticMethods import StaticMethods
from AppConfigs.AppUsage import Usage
from AppStatics.StaticValues import StaticValues
from colorama import Fore,Style
import time,os
class Program():
    def __init__(self):
        self.Login()
        self.Menu()
        
    def Menu(self):
        while True:
            MONEY_COLOR = Fore.RED if int(Management.GetInfo('MONEY')) < 0 else Fore.GREEN
            CURRENT_COLOR = Fore.RED if int(Management.GetInfo('CURRENT_MONTH')) < 0 else Fore.GREEN
            os.system("cls")
            print(f"""
            {StaticMethods.Centered(f"{Fore.BLUE}Balance: "+MONEY_COLOR+Management.GetInfo("MONEY")+"€")}
            {StaticMethods.Centered(f"{Fore.BLUE}This Month: "+CURRENT_COLOR+Management.GetInfo("CURRENT_MONTH")+"€")}{Style.RESET_ALL}
            {StaticMethods.Centered(f"{Fore.BLUE}Budget: {Style.RESET_ALL}"+Management.GetInfo("BUDGET")+"€")}

            {StaticMethods.Centered("[1] - View Account Settings","RED")}
            {StaticMethods.Centered("[2] - View History","YELLOW")}
            \n
            {StaticMethods.Centered("[3] - Add Expense")}
            """)

            CHOICE = StaticMethods.ValidInteger("-> ",3,1,notify_Exception=True)

            match CHOICE:
                case 1: self.AccountSettings()
                case 2: self.ViewHistory()
                case 3: self.AddExpense()
    def AddExpense(self):
        self.type_buy = "Groceries"
        self.price = 1
        def ChangeType(type):
            os.system("cls")
            print("""
            [1] - Groceries
            [2] - Technology
            [3] - Bills
            """)
            CHOICE = StaticMethods.ValidInteger("-> ",3,1,notify_Exception=True)

            match CHOICE:
                case 1: type = "Groceries"
                case 2: type = "Technology"
                case 3: type = "Bills"
            return type
        def ChangePrice():
            os.system("cls")
            CHOICE = StaticMethods.ValidInteger("Insert Price\n-> ",10000,notify_Exception=True)

            return CHOICE
        while True:
            os.system("cls")

            print(f"""
            [1] - Type of Buy - {self.type_buy}    
            [2] - Price - {self.price}€

            [3] - Confirm

            [4] - Return To Menu
            """)
            CHOICE = StaticMethods.ValidInteger("-> ",4,1,notify_Exception=True)

            match CHOICE:
                case 1: self.type_buy = ChangeType(self.type_buy)
                case 2: self.price = ChangePrice()
                case 3: break
                case 4: return
        Usage.Global.History = f"{self.type_buy};{self.price}"
        Usage.BalanceModifier(expense=True, expense_value=self.price)
        Usage.SetNewExpense()
    def ViewHistory(self):
        print(StaticMethods.CustomPosition(20,"Type")+StaticMethods.CustomPosition(40,"Price"))
        try:
            for item in Management.GetInfo('HISTORY').split(","):
                abs = item.split(";")
                print(StaticMethods.CustomPosition(20,abs[0])+StaticMethods.CustomPosition(40,abs[1]+"€"))
        except IndexError:
            print(StaticMethods.Centered("No more items to show","RED"))
        input("\nPress anything to go back to the menu.\n")
        return
    def ClearHistory(self):
        os.system("cls")
        def Confirmation():
            print("""
            Do you really want to erase it?
            [1] - Yes
            [2] - No
            """)
            CHOICE = StaticMethods.ValidInteger("-> ",2,1,notify_Exception=True)

            match CHOICE:
                case 1: return True
                case 2: return False
        if Confirmation():
            with open(Management.CONFIG_LOCATION, 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'HISTORY' in line:
                    lines[i] = "HISTORY:"
                    break
            with open(Management.CONFIG_LOCATION, 'w') as file:
                file.writelines(lines)
        return
    def AccountSettings(self):
        os.system("cls")
        print(f"""
        {StaticMethods.Centered("Account Settings")}
        \n
        {StaticMethods.Centered(f"[1] - Add Balance | CURRENT: {Management.GetInfo("MONEY")}€")}
        {StaticMethods.Centered(f"[2] - Set Budget  | CURRENT: {Management.GetInfo("BUDGET")}€ ")}
        {StaticMethods.Centered(f"[3] - Clear Purchase History | CURRENT NUMBER OF ITEMS: {len(Management.GetInfo("HISTORY").split(","))-1} ")}
        \n
        {StaticMethods.Centered(f"[4] - Change PIN")}
        {StaticMethods.Centered(f"[5] - Return to Menu")}
        """)
        CHOICE = StaticMethods.ValidInteger("-> ",5,1,notify_Exception=True)
        match CHOICE:
                case 1: Usage.BalanceModifier(True)
                case 2: Usage.SetBudget()
                case 3: self.ClearHistory()
                case 4: Management.ChangePIN()
                case 5:return
        return
    def Login(self):
        os.system("cls")
        while True:
            if Management.GetInfo("PIN") == "DEFAULT":
                Management.ChangePIN(isnew=True)
            if StaticValues.LOGIN_ATTEMPTS < 5:
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

