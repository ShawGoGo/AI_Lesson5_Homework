
class Lijing: # 李靖
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name, weapons=[], power=10):
        self.name = name
        self.weapons = weapons
        self.power = power

    def count_fight(self, weapon, weapon_power):
        self.weapons.append(weapon)
        self.power += weapon_power  # 总战力=武器战力之和

lijing = Lijing('李靖')
print(lijing.weapons)
lijing.count_fight('七宝玲珑塔', 50)  # 七宝玲珑塔 战力 50\n",
print(lijing.power)

class Nezha(Lijing):
    def __init__(self, name, weapons = ['混天绫', '乾坤圈'], power = 50):
        self.name = name
        self.weapons = weapons
        self.power = power
    def count_fight(self, weapon, weapon_power):
        #self.weapons.append(weapon)
        #self.power += weapon_power  # 总战力=武器战力之和
        Lijing.count_fight(self, weapon, weapon_power)

nezha = Nezha('哪吒')
nezha.count_fight('火尖枪', 40)
print(nezha.weapons)
print(nezha.power)