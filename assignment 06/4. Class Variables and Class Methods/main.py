class Bank:
    # Class variable
    bank_name = "Allied Bank"
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display_info(self):
        print(f"Bank: {self.bank_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("-" * 30)

# Create two bank accounts
account1 = Bank("ACC001", 1500)
account2 = Bank("ACC002", 2500)

# Display initial information
print("Initial bank information:")
account1.display_info()
account2.display_info()

# Change the bank name using class method
Bank.change_bank_name("New Global Bank")

# Display information after changing bank name
print("\nAfter changing bank name:")
account1.display_info()
account2.display_info()
