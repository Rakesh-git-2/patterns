def max_profit (price_list):
    min_price = float('inf')
    max_profit = 0
    for price in price_list:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit




print(max_profit(price_list=[1,3,4,67,0]))