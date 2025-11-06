class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Yatırılacak tutar pozitif olmalı.")
            return
        self.balance += amount
        self.transactions.append(f"+{amount} TL yatırıldı.")
        print(f" {amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")

    def withdraw(self, amount):
        if amount <= 0:
            print("Çekilecek tutar pozitif olmalı.")
            return
        if amount > self.balance:
            print("Yetersiz bakiye.")
            return
        self.balance -= amount
        self.transactions.append(f"-{amount} TL çekildi.")
        print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")

    def show_balance(self):
        print(f"{self.account_holder} hesabının bakiyesi: {self.balance} TL")

    def show_transactions(self):
        print(f"{self.account_holder} - İşlem Geçmişi:")
        for t in self.transactions:
            print("  -", t)


# --- How to use example ---
if __name__ == "__main__":
    hesap = BankAccount("Ahmet Yılmaz", 1000)
    hesap.show_balance()
    hesap.deposit(500)
    hesap.withdraw(300)
    hesap.withdraw(2000)
    hesap.show_transactions()
