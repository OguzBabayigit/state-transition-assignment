def is_shipping_free(price, numberOfItems, isPrimeShoppingMember):
    print("Additional Statement 1")
    if price > 50 or isPrimeShoppingMember:
        print("Additional Statement 2")
    if price > 25 and numberOfItems <3:
        print("Additional Statement 3")
    elif price > 10 and numberOfItems == 1 :
        print("Additional Statement 4(discount)")
        return False
    return True
    print("Additional Statement 5")
