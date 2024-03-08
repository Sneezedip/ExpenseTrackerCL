import time
from AppStatics.StaticMethods import StaticMethods
from AppConfigs.FileManagement import Management
import os
class Usage():
    class Global:
        History = ""
    def BalanceModifier(AddBalance=False,expense=False,expense_value = 0):
        def Apply(final,type="MONEY"):
            with open(Management.CONFIG_LOCATION, 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if type in line:
                    lines[i] = f"{type}:{final}\n"
                    break
            with open(Management.CONFIG_LOCATION, 'w') as file:
                file.writelines(lines)
        def Confirmation():
            print("""
            Your expense is higher than the current balance.
                  Do you want to continue?
                  
            [1] - Yes
            [2] - No
            """)
            CHOICE = StaticMethods.ValidInteger("-> ",2,1,notify_Exception=True)

            match CHOICE:
                case 1: return True
                case 2: return False           
        if not expense:
            amount = StaticMethods.ValidInteger("How much would you like to {0}?\n-> ".format("remove" if not AddBalance else "add"),500000)
            if AddBalance:
                Apply(int(Management.GetInfo('MONEY')) + amount)
            else:
                Apply(int(Management.GetInfo('MONEY')) - amount)
            return
        else:
            if expense_value > int(Management.GetInfo('BUDGET')):
                if Confirmation():
                    pass
                else:
                    return
            Apply(int(Management.GetInfo('MONEY')) - expense_value)
            Apply(int(Management.GetInfo('CURRENT_MONTH')) - expense_value,type="CURRENT_MONTH")
            Apply(int(Management.GetInfo('BUDGET')) - expense_value,type="BUDGET")
    def SetBudget(Remove=False):
        if int(Management.GetInfo("MONEY")) <=0:
            os.system("cls")
            print(StaticMethods.Centered("Can't set budget while balance equal or less than 0€","RED"))
            input("Press any key to return.")
            return
        with open(Management.CONFIG_LOCATION, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if 'BUDGET' in line:
                lines[i] = "BUDGET:"+str(StaticMethods.ValidInteger("How much would you like to set to?\n-> ",int(Management.GetInfo("MONEY")),notify=True,notify_message="Budget can't be higher than the balance"))+"\n"
                break
        with open(Management.CONFIG_LOCATION, 'w') as file:
            file.writelines(lines)
    def SetNewExpense():
        with open(Management.CONFIG_LOCATION, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if 'HISTORY' in line:
                old = lines[i].split(":")[1]
                lines[i] = str("HISTORY:"+Usage.Global.History+","+old)
                break
        with open(Management.CONFIG_LOCATION, 'w') as file:
            file.writelines(lines)
            