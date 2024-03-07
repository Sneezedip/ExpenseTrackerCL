from AppStatics.StaticMethods import StaticMethods
from AppConfigs.FileManagement import Management
class Usage():
    def BalanceModifier(AddBalance=False):
        def Apply(final):
            with open(Management.CONFIG_LOCATION, 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'MONEY' in line:
                    lines[i] = f"MONEY:{final}\n"
                    break
            with open(Management.CONFIG_LOCATION, 'w') as file:
                file.writelines(lines)
        amount = StaticMethods.ValidInteger("How much would you like to {0}?\n-> ".format("remove" if not AddBalance else "add"),500000)
        if AddBalance:
            Apply(int(Management.GetInfo('MONEY')) + amount)
        else:
            Apply(int(Management.GetInfo('MONEY')) - amount)
        return
    def SetBudget(Remove=False):
        with open(Management.CONFIG_LOCATION, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if 'BUDGET' in line:
                lines[i] = f"BUDGET:{StaticMethods.ValidInteger("How much would you like to set to?\n-> ",500000)}\n"
                break
        with open(Management.CONFIG_LOCATION, 'w') as file:
            file.writelines(lines)