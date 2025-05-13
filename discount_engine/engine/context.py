from typing import List, Dict
from decimal import Decimal
from models import CartItem, CustomerProfile, PaymentInfo


class DiscountContext:
    def __init__(
        self,
        cart: List[CartItem],
        customer: CustomerProfile,
        payment_info: PaymentInfo = None,
    ):
        self.cart = cart
        self.customer = customer
        self.payment_info = payment_info
        self.original_price = sum(
            item.product.base_price * item.quantity for item in cart
        )
        self.current_price = self.original_price
        self.discounts_applied: Dict[str, Decimal] = {}
        self.messages: List[str] = []

    def apply_discount(self, name: str, amount: Decimal):
        if amount > 0:
            self.current_price -= amount
            self.discounts_applied[name] = amount
            self.messages.append(f"{name}: -{amount:.2f}")
