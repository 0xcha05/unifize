from engine.context import DiscountContext
from models import DiscountedPrice
from rules.evaluators import (
    evaluate_brand_discounts,
    evaluate_category_discounts,
    evaluate_voucher,
    evaluate_bank_offers,
)


class DiscountService:
    async def calculate_cart_discounts(
        self, cart_items, customer, payment_info=None, voucher_code=None
    ):
        context = DiscountContext(cart_items, customer, payment_info)

        evaluators = self.get_discount_evaluators(voucher_code)
        for evaluator in evaluators:
            evaluator(context)

        return DiscountedPrice(
            original_price=context.original_price,
            final_price=context.current_price,
            applied_discounts=context.discounts_applied,
            message="; ".join(context.messages),
        )

    def get_discount_evaluators(self, voucher_code):
        return [
            self.apply_brand_discounts,
            self.apply_category_discounts,
            lambda ctx: self.apply_voucher(ctx, voucher_code),
            self.apply_bank_offers,
        ]

    def apply_brand_discounts(self, context):
        evaluate_brand_discounts(context)

    def apply_category_discounts(self, context):
        evaluate_category_discounts(context)

    def apply_voucher(self, context, code):
        evaluate_voucher(context, code)

    def apply_bank_offers(self, context):
        evaluate_bank_offers(context)
