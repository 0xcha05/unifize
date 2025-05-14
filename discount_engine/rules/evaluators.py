from decimal import Decimal
from rules.matchers import match_brand, match_category, match_bank
from rules.config import BRAND_DISCOUNTS, CATEGORY_DISCOUNTS, BANK_OFFERS, VOUCHERS


def evaluate_brand_discounts(context):
    for rule in BRAND_DISCOUNTS:
        try:
            percent = Decimal(str(rule["percent"])) / Decimal("100")
            for item in context.cart:
                if match_brand(item, rule):
                    amount = item.product.base_price * percent
                    context.apply_discount(rule["name"], amount * item.quantity)
        except Exception as e:
            context.log_error(f"Error in brand discount '{rule}': {e}")


def evaluate_category_discounts(context):
    for rule in CATEGORY_DISCOUNTS:
        try:
            percent = Decimal(str(rule["percent"])) / Decimal("100")
            for item in context.cart:
                if match_category(item, rule):
                    discounted_price = item.product.base_price * Decimal("0.6")
                    amount = discounted_price * percent
                    context.apply_discount(rule["name"], amount * item.quantity)
        except Exception as e:
            context.log_error(f"Error in category discount '{rule}': {e}")


def evaluate_bank_offers(context):
    for rule in BANK_OFFERS:
        try:
            percent = Decimal(str(rule["percent"])) / Decimal("100")
            if match_bank(context.payment_info, rule):
                amount = context.current_price * percent
                context.apply_discount(rule["name"], amount)
        except Exception as e:
            context.log_error(f"Error in bank offer '{rule}': {e}")


def evaluate_voucher(context, code):
    try:
        if not code or code not in VOUCHERS:
            context.log_error(f"Invalid or missing voucher code: {code}")
            return

        voucher = VOUCHERS[code]

        if context.customer.tier not in voucher["customer_tiers"]:
            context.log_error(
                f"Voucher '{code}' not valid for customer tier '{context.customer.tier}'"
            )
            return

        for item in context.cart:
            if item.product.brand in voucher["excluded_brands"]:
                context.log_error(
                    f"Voucher '{code}' excluded for brand '{item.product.brand}'"
                )
                return

        percent = Decimal(str(voucher["percent"])) / Decimal("100")
        amount = context.current_price * percent
        context.apply_discount(voucher["name"], amount)
    except Exception as e:
        context.log_error(f"Error in voucher '{code}': {e}")
