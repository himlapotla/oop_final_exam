class Bank:
    usersss = []
    admins = []
    loan_feature = 1
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount
        self.loan_amount = 0

class Customer:
    def __init__(self, name, email, address, ac_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.ac_type = ac_type
        self.ac_number = len(Bank.usersss)+100
        self.balance = 0
        self.loan = 0

        Bank.usersss.append(self)
        self.transaction_his = []

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            bank.amount += amount
            print(f'{amount} taka has been added to {self.name}s account')
        self.transaction_his.append(f'{amount} taka has added to {self.name}s account')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'{amount} taka has been withdrawed')
            self.transaction_his.append(f'{amount} taka has been withdrawed')
        else:
            print('Withdrawal amount exceeded')

    def transfer(self, amount, ac_num):
        for a_n in Bank.usersss:
            if a_n.ac_number == ac_num:
                a_n.balance += amount
                self.balance -= amount
                print(f'{amount} taka has been transfered to {ac_num}s account')
        self.transaction_his.append(f'{amount} has transfered to account {ac_num} by {self.name}')

    def history(self):
        for t in self.transaction_his:
            print(t)

    def check_balance(self):
        print(f' this is your current balance {self.balance}')

    def take_loan(self, amont):
        if bank.loan_feature == 1:
            if self.loan < 2:
                self.balance += amont
                bank.amount -= amont
                self.loan += 1
                print(f'loan successfully added to {self.name}s account')
                bank.loan_amount += amont
            else:
                print('your loan limit is finish')
        else:
            print('loan feature is off')
            

class Admin:
    def __init__(self, name, email, type) -> None:
        self.name = name
        self.email = email
        self.type = type
        self.ac_number = len(Bank.admins)+1
        Bank.admins.append(self)

    def see_all_accounts(self):
        print('this are the all bank accounts -- ')
        for accounts in bank.usersss:
            print(f'account name -- {accounts.name} account number -- {accounts.ac_number} account type -- {accounts.ac_type}')

    def delete_account(self, acc_n):
        for acc in bank.usersss:
            if acc.ac_number == acc_n:
                bank.usersss.remove(acc)
                print(f"Account {acc_n} has been deleted.")

    def total_balance_of_bank(self):
        print(f'total bank amount -- {bank.amount}')

    def total_loan_amount(self):
        print(f'total loan amount -- {bank.loan_amount}')

    def control_loan_feature(self):
        op = int(input('if you want to loan off press 2 : '))
        print()
        if op == 2:
            bank.loan_feature = 2
            print('loan feature has been turned off')
            print()
        

bank = Bank('Sonali Bank', 10000)
himla = Customer('himla', 'him@gmail.cm', 'chapai', 'savings')
mimla = Customer('mimla', 'mim@gmail.cm', 'rajshahi', 'current')
Shah = Admin('shah', 'shah@gmail.com', 'ADMIN')


while(True):
    # initialy there are 2 user himla and mimla. Their account numbres are himla - 100 and mimla - 101. And there
    # are one admin and his account number is 1. 

    print()
    print('1. deposit money')
    print('2. withdraw money')
    print('3. check available balance')
    print('4. check transaction history')
    print('5. take a loan')
    print('6. transfer money')
    print('7. delete user account')
    print('8. see all users account')
    print('9. total balance of bank')
    print('10. total loan amount of bank')
    print('11. on or off loan feature')
    print('12. exit')
    print()

    op = int(input('Choose an option : '))

    if op == 1:
        ac_num = int(input('enter your account num : '))
        print()
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                amt = int(input('enter your deposit amount : '))
                print()
                print()
                usr.deposit(amt)
                break
        else:
            print('invalid account number')
            print()

    if op == 2:
        ac_num = int(input('enter your account num : '))
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                amt = int(input('enter your withdrw amount : '))
                print()
                usr.withdraw(amt)
                break
        else:
            print('invalid account number')
            print()
        
    if op == 3:
        ac_num = int(input('enter your account num : '))
        print()
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                usr.check_balance()
                break
        else:
            print('invalid account number')
            print()

    if op == 4:
        ac_num = int(input('enter your account num : '))
        print()
        print(f'all the tramsaction history of {usr.name}s account -- ')
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                for th in usr.transaction_his:
                    print(th)
                break
        else:
            print('invalid account number')
            print()

    if op == 5:
        ac_num = int(input('enter your account num : '))
        print()
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                if bank.loan_feature == 1:
                    amt = int(input('enter your loan amount : '))
                    print()
                    usr.take_loan(amt)
                else:
                    print('loan feature is off')
                break
        else:
            print('invalid account number')
            print()

    if op == 6:
        ac_num = int(input('enter your account num : '))
        print()
        for usr in bank.usersss:
            if usr.ac_number == ac_num:
                amt = int(input('enter your transfer amount : '))
                acnt = int(input('enter the account you want ta transfer : '))
                usr.transfer(amt, acnt)
                break
        else:
            print('invalid account number')
            print()

    if op == 7:
        ac_num = int(input('enter your admin account num : '))
        print()
        for usr in bank.admins:
            if usr.ac_number == ac_num:
                acc_n = int(input('enter the account number you want to deleted : '))
                print()
                usr.delete_account(acc_n)
                break
        else:
            print('invalid admin account number')
            print()

    if op == 8:
        ac_num = int(input('enter your admin account num : '))
        print()
        for usr in bank.admins:
            if usr.ac_number == ac_num:
                usr.see_all_accounts()
                break
        else:
            print('invalid admin account number')
            print()

    if op == 9:
        ac_num = int(input('enter your admin account num : '))
        print()
        for usr in bank.admins:
            if usr.ac_number == ac_num:
                usr.total_balance_of_bank()
                break
        else:
            print('invalid admin account number')
            print()

    if op == 10:
        ac_num = int(input('enter your admin account num : '))
        print()
        for usr in bank.admins:
            if usr.ac_number == ac_num:
                usr.total_loan_amount()
                break
        else:
            print('invalid admin account number')
            print()

    if op == 11:
        ac_num = int(input('enter your admin account num : '))
        print()
        for usr in bank.admins:
            if usr.ac_number == ac_num:
                usr.control_loan_feature()
                break
        else:
            print('invalid admin account number')
            print()

    if op == 12:
        break

