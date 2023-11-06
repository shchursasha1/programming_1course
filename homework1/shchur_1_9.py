a, b, n = [int(d) for d in input().split()]
price_in_coins = (a * 100) + b
total_price_in_coins = n * price_in_coins
total_price_uah = total_price_in_coins // 100
total_price_coins = total_price_in_coins % 100
print(total_price_uah, total_price_coins)