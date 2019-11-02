

class Transanction:
    balance = 1000
    def __init__(self):
        self.balance = Transanction.balance

    def menu(self):
        info = """
1.Balance
2.Withdraw
3.Deposit
4.Exit 
            """
        choice = 0
        while choice != 4:
            try:
                print(info)
                choice = int(input('Please select your transanction： '))
                if choice == 1:
                    self.show_balance()
                elif choice == 2:
                    self.withdraw()
                elif choice == 3:
                    self.deposit()
                elif choice == 4:
                    print('Your transanction ends. Thank you!')
                    break
                else:
                    print('Wrong input!')
            except Exception:
                print('ERROR: Wrong input!')

    def show_balance(self):
        print('Your current balance is {}.'.format(self.balance))

    def withdraw(self):
        withdraw_temp = int(input('Please input withdraw amount: '))
        if self.balance < withdraw_temp:
            print('Sorry, your current balance is not enough. Withdraw fails.')
        else:
            self.balance += - withdraw_temp
            print('You withdraw {}.\nYour current balance is {}.'.format(withdraw_temp, self.balance))

    def deposit(self):
        deposit_temp = int(input('Please input deposit amount: '))
        self.balance += deposit_temp
        print('You deposit {}.\nYour current balance is {}.'.format(deposit_temp, self.balance))


ATM = Transanction()
ATM.menu()