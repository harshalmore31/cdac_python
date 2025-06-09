
class BankAccount_A5:
    bank_name = "SBI" 

    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder 
        self.balance = balance    

    def show_details(self):
        print(f"Bank Name: {BankAccount_A5.bank_name}") 
        print(f"Account Holder: {self.acc_holder}")
        print(f"Balance: ${self.balance:.2f}")

account1_a5 = BankAccount_A5("Harshal", 5000)
account1_a5.show_details()
