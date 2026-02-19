def calculate_price(price, discount=0):
    final_price = price - (price * discount / 100)
    print("Final price:", final_price)

calculate_price(100)       
calculate_price(100, 10)    
