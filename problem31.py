def num_of_changes(coins, target_amount):
    changes = [1] + [0]* target_amount
    for coin in coins:
        for amt in range(coin, target_amount + 1):
            changes[amt] += changes[amt - coin]
    return changes[target_amount]

if __name__ == '__main__':
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target_amount = 200
    print num_of_changes(coins, target_amount)
