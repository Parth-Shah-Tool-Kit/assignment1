#You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.


price = []  
n = int(input('Enter the number of days \n'))
print('Enter the cosst of stock on each day')

for i in range(0, n):
    ele = int(input())  
    price.append(ele)
    

def max_profit(the_price):
    profit = []
    for i in range(len(the_price)):
        for j in range(len(the_price)):
            if j <= (len(the_price) - 1  - i):
                profit.append(the_price[len(the_price) - 1  - i] - the_price[j])
                
    profit.sort()
    return profit[-1]
                

print('The max profit is:')
print(max_profit(price))
