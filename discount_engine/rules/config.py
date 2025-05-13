BRAND_DISCOUNTS = [
    {"brand": "PUMA", "percent": 40.0, "name": "Brand Offer - PUMA"},
]

CATEGORY_DISCOUNTS = [
    {"category": "T-shirt", "percent": 10.0, "name": "Category Offer - T-shirts"},
]

BANK_OFFERS = [
    {"bank": "ICICI", "method": "CARD", "percent": 10.0, "name": "ICICI Bank Offer"},
]

VOUCHERS = {
    "SUPER69": {
        "percent": 69.0,
        "excluded_brands": [],
        "customer_tiers": ["GOLD", "SILVER"],
        "name": "Voucher SUPER69",
    }
}

#can be moved to db and updated at runtime, hence extensible for business