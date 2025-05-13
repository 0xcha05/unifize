def match_brand(item, rule):
    return item.product.brand == rule["brand"]


def match_category(item, rule):
    return item.product.category.lower() == rule["category"].lower()


def match_bank(payment_info, rule):
    return (
        payment_info
        and payment_info.bank_name == rule["bank"]
        and payment_info.method == rule["method"]
    )
