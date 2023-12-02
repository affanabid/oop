class BankAccount:

    def __init__(self, minbal, curbal) -> None:
        self.__min_bal = float(minbal)
        self.__cur_bal = float(curbal)

    def withdraw(self, amount):
        new_amount = self.__cur_bal - amount
        if new_amount < self.__min_bal:
            raise Exception('Not enough balance')
        else:
            self.__cur_bal = new_amount
            print(f'Amount Withdrawn({amount})')
            print(f'Current Balance: {self.__cur_bal}')

    def __str__(self) -> str:
        return f'Current Balance: {self.__cur_bal}\nMinimum Balance: {self.__min_bal}'
        
b = BankAccount(10, 50)
print(b)
b.withdraw(25)
