# Order details - already filled in for you
item_name = "Veg Biryani"
quantity = int("4")       # quantity arrives as text, so convert it
unit_price = 135.0

subtotal = quantity * unit_price

# Placeholder values - your decision blocks must replace these
tier = "?"
discount_rate = 0
delivery_fee = 0

# TODO 1: if / elif / else block that sets tier and discount_rate
if subtotal >= 500:
    tier = "Gold"
    discount_rate = 0.15
elif subtotal >= 300:
    tier = "Silver"
    discount_rate = 0.10
else:
    tier = "Bronze"
    discount_rate = 0

# TODO 2: if / else block that sets delivery_fee
if subtotal >= 300:
    delivery_fee = 0
else:
    delivery_fee = 40

discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount + delivery_fee

print("Item:", item_name)
print("Subtotal:", subtotal)
print("Tier:", tier)
print("Discount rate:", discount_rate)
print("Discount amount:", round(discount_amount, 2))
print("Delivery fee:", delivery_fee)
print("Final total:", round(final_total, 2))