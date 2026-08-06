from abc import ABC, abstractmethod
# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy=None):
        self.strategy = strategy

    # Change payment strategy at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected.")
        else:
            self.strategy.pay(amount)


# Driver Code
processor = PaymentProcessor()

# Credit Card Payment
processor.set_strategy(CreditCardPayment())
processor.process_payment(5000)

# PayPal Payment
processor.set_strategy(PayPalPayment())
processor.process_payment(2500)

# Bitcoin Payment
processor.set_strategy(BitcoinPayment())
processor.process_payment(1000)