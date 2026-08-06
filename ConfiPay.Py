class CreditCardPayment:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")

class UPIPayment:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")

class NetBankingPayment:
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Net Banking.")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("===== Payment Processing System =====")
print("1. Credit Card")
print("2. UPI")
print("3. Net Banking")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: ₹"))

if choice == 1:
    payment = CreditCardPayment()
elif choice == 2:
    payment = UPIPayment()
elif choice == 3:
    payment = NetBankingPayment()
else:
    print("Invalid Choice!")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)
