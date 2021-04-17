
coins = [500, 100, 50, 10]
change = 1200
total = 0
for i in range(len(coins)):
    coin = coins[i]
    if change // coin >= 1:
        total = total + change // coin
        change = change - coin * (change//coin)
        print(total, coin, change)

