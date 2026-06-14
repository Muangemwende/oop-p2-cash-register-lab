#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add price to total
        self.total += price * quantity
        # Add item name to items list (repeated if quantity > 1)
        for _ in range(quantity):
            self.items.append(title)
        # Track last transaction for void
        self._last_transaction = price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= self._last_transaction
        self._last_transaction = 0#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add price to total
        self.total += price * quantity
        # Add item name to items list (repeated if quantity > 1)
        for _ in range(quantity):
            self.items.append(title)
        # Track last transaction for void
        self._last_transaction = price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= self._last_transaction
        self._last_transaction = 0