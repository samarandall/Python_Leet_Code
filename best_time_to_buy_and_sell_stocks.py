prices = [7,1,5,3,6,4]
current_lowest_day = 0
best_profit = 0
buy_day = 0
sell_day = 0
        
for day in range(1, len(prices)):
    if prices[day] < prices[current_lowest_day]:
        current_lowest_day = day
    elif prices[day] - prices[current_lowest_day] > best_profit:
        best_profit = prices[day] - prices[current_lowest_day]
        buy_day = current_lowest_day
        sell_day = day
        
sell_day += 1
buy_day += 1
if best_profit > 0:
    print("Buy on day" , buy_day)
    print("Sell on day" , sell_day)
    print("Profit" , best_profit) 

else: 
    print("Dont buy or sell")

    