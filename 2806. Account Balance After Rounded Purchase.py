def accountBalanceAfterPurchase(purchaseAmount):
    return 100 - round(purchaseAmount / 10) * 10
print(accountBalanceAfterPurchase(19))