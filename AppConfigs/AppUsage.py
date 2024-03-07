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
        if not expense:
            amount = StaticMethods.ValidInteger("How much would you like to {0}?\n-> ".format("remove" if not AddBalance else "add"),500000)
            if AddBalance:
                Apply(int(Management.GetInfo('MONEY')) + amount)
                Apply(int(Management.GetInfo('CURRENT_MONTH')) + amount,type="CURRENT_MONTH")
            else:
                Apply(int(Management.GetInfo('MONEY')) - amount)
            return
        else:
            Apply(int(Management.GetInfo('MONEY')) - expense_value)
            Apply(int(Management.GetInfo('CURRENT_MONTH')) - expense_value,type="CURRENT_MONTH")
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
                lines[i] = f"BUDGET:{StaticMethods.ValidInteger("How much would you like to set to?\n-> ",int(Management.GetInfo("MONEY")),notify=True,notify_message="Budget can't be higher than the balance")}\n"
                break
        with open(Management.CONFIG_LOCATION, 'w') as file:
            file.writelines(lines)
    def SetNewExpense():
        with open(Management.CONFIG_LOCATION, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if 'HISTORY' in line:
                old = lines[i].split(":")[1]
                lines[i] = f"HISTORY:{Usage.Global.History+","+old}"
                break
        with open(Management.CONFIG_LOCATION, 'w') as file:
            file.writelines(lines)
            