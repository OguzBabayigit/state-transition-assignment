def is_shipping_free(price, number_of_items, prime_member):
    """
    Determines if shipping is free based on business rules.

    Rules:
    - Free if Prime member.
    - Free if total price >= 50.
    - Free if number of items >= 3 and price >= 25.
    - Free if price >= 10 and Prime member.
    Otherwise, not free.
    """
    if prime_member:
        return True
    if price >= 50:
        return True
    if number_of_items >= 3 and price >= 25:
        return True
    if price >= 10 and prime_member:
        return True
    return False
