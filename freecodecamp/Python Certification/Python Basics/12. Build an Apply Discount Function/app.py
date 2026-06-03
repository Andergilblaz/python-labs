# =========================================================
# LAB: BUILD AN APPLY DISCOUNT FUNCTION
# =========================================================
#
# OBJECTIVE
# ---------------------------------------------------------
# Create a function that calculates the final price
# after applying a percentage discount.
#
# Example:
#
# Price: 50
# Discount: 20%
#
# Discount amount = 10
# Final price = 40
#
# =========================================================
# REQUIREMENTS
# =========================================================
#
# Function name:
#
# apply_discount
#
# Parameters:
#
# price
# discount
#
# =========================================================
# VALIDATIONS
# =========================================================
#
# 1. If price is not a number:
#
#     return "The price should be a number"
#
# ---------------------------------------------------------
#
# 2. If discount is not a number:
#
#     return "The discount should be a number"
#
# ---------------------------------------------------------
#
# 3. If price <= 0:
#
#     return "The price should be greater than 0"
#
# ---------------------------------------------------------
#
# 4. If discount < 0 or discount > 100:
#
#     return "The discount should be between 0 and 100"
#
# =========================================================
# CALCULATION
# =========================================================
#
# Discount amount:
#
# price * (discount / 100)
#
# Final price:
#
# price - discount_amount
#
# Return the final price.
#
# =========================================================
# SOLUTION
# =========================================================

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return f'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return f'The discount should be a number'
    elif price <= 0: 
        return f'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return f'The discount should be between 0 and 100'
    else:
        total = price - (price * (discount / 100))
        return total


print(apply_discount(100, 120))
# =========================================================
# TEST CASES
# =========================================================
#
# apply_discount("100", 20)
#
# Expected:
# "The price should be a number"
#
# ---------------------------------------------------------
#
# apply_discount(100, "20")
#
# Expected:
# "The discount should be a number"
#
# ---------------------------------------------------------
#
# apply_discount(0, 20)
#
# Expected:
# "The price should be greater than 0"
#
# ---------------------------------------------------------
#
# apply_discount(100, -5)
#
# Expected:
# "The discount should be between 0 and 100"
#
# ---------------------------------------------------------
#
# apply_discount(100, 20)
#
# Expected:
# 80
#
# ---------------------------------------------------------
#
# apply_discount(200, 50)
#
# Expected:
# 100
#
# ---------------------------------------------------------
#
# apply_discount(50, 0)
#
# Expected:
# 50
#
# ---------------------------------------------------------
#
# apply_discount(100, 100)
#
# Expected:
# 0
#
# ---------------------------------------------------------
#
# apply_discount(74.5, 20.0)
#
# Expected:
# 59.6
#
# =========================================================