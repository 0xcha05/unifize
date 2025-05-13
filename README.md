# unifize

## Assumptions & Decisions

- Discounts are applied in this order: **Brand → Category → Voucher → Bank**
- Discount rules (like “40% off on PUMA”) are defined in config files so they’re easy to update
- Voucher is skipped if the cart has any excluded brand

## how to run

python -m tests.test_pipeline

## structure

models.py – defines products, cart items, and customer

engine/ – tracks cart state during discount calculation

rules/ – where all the discount rules live

services/ – the main discount service logic

tests/ – test case for the sample scenario

## eg output

Original Price: 1000
Final Price: 150.66
Applied Discounts:

- Brand Offer - PUMA: -400.00
- Category Offer - T-shirts: -60.00
- Voucher SUPER69: -372.60
- ICICI Bank Offer: -16.74
