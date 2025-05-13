from decimal import Decimal
from rules.matchers import match_brand, match_category, match_bank
from rules.config import BRAND_DISCOUNTS, CATEGORY_DISCOUNTS, BANK_OFFERS, VOUCHERS


def evaluate_brand_discounts(context):
    for rule in BRAND_DISCOUNTS:
        percent = Decimal(str(rule["percent"])) / Decimal("100")
        for item in context.cart:
            if match_brand(item, rule):
                amount = item.product.base_price * percent
                context.apply_discount(rule["name"], amount * item.quantity)


def evaluate_category_discounts(context):
    for rule in CATEGORY_DISCOUNTS:
        percent = Decimal(str(rule["percent"])) / Decimal("100")
        for item in context.cart:
            if match_category(item, rule):
                discounted_price = item.product.base_price * Decimal(
                    "0.6"
                )  # Assuming brand applied
                amount = discounted_price * percent
                context.apply_discount(rule["name"], amount * item.quantity)


def evaluate_bank_offers(context):
    for rule in BANK_OFFERS:
        percent = Decimal(str(rule["percent"])) / Decimal("100")
        if match_bank(context.payment_info, rule):
            amount = context.current_price * percent
            context.apply_discount(rule["name"], amount)


def evaluate_voucher(context, code):
    if not code or code not in VOUCHERS:
        return
    voucher = VOUCHERS[code]
    if context.customer.tier not in voucher["customer_tiers"]:
        return
    for item in context.cart:
        if item.product.brand in voucher["excluded_brands"]:
            return
    percent = Decimal(str(voucher["percent"])) / Decimal("100")
    amount = context.current_price * percent
    context.apply_discount(voucher["name"], amount)
