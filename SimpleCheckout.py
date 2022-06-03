from typing import List
import collections
import sys

class SimpleCheckout:

    # An array of size 3 is used to describe the special offer
    # First element - (0 or 1) represents whether we have a multi-priced offer or a buy n get 1 free respectively
    # Second element - represents the number of items
    # Third element - represents the price if multi-priced offer, and is always 1 if we have a buy n get 1 free offer
    def __init__(self):
        self.__price_A = 0
        self.__price_B = 0
        self.__price_C = 0
        self.__special_price_A = [0] * 3
        self.__special_price_B = [0] * 3
        self.__special_price_C = [0] * 3
    
    def set_prices(self, price_A: float, price_B: float, price_C: float):
        self.__price_A = price_A
        self.__price_B = price_B
        self.__price_C = price_C
    
    def set_special_prices(self, special_price_A: List[float], special_price_B: List[float], special_price_C: List[float]):
        self.__special_price_A = special_price_A
        self.__special_price_B = special_price_B
        self.__special_price_C = special_price_C
    
    def calculate_price(self, items: List[str]):
        # Helper method to calculate the total cost per item label
        def calculate(price, special_price, count) -> float:
            if (count == 0):
                return 0
            
            # No special offer for item
            if (special_price[1] == 0 or special_price[2] == 0):
                return count * price
            
            # Multi priced offer
            if (special_price[0] == 0):
                discounted_items = count // special_price[1]
                remainder = count % special_price[1]
                return (discounted_items * special_price[2]) + (remainder * price)
            # Buy n get 1 free
            else:
                discounted_items = count // (special_price[1] + 1)
                return (count - discounted_items) * price
            
        # Count the number of each item
        counter = collections.Counter()
        for i in items:
            counter[i] += 1
        
        A_price = calculate(self.__price_A, self.__special_price_A, counter['A'])
        B_price = calculate(self.__price_B, self.__special_price_B, counter['B'])
        C_price = calculate(self.__price_C, self.__special_price_C, counter['C'])

        return A_price + B_price + C_price


SKU = SimpleCheckout()

# Using the prices defined in the problem specification
SKU.set_prices(0.50, 0.75, 0.25)

# Using the special prices defined in the problem specification
special_A = [0, 0, 0]
special_B = [0, 2, 1.25]
special_C = [1, 3, 1]
SKU.set_special_prices(special_A, special_B, special_C)

# Move command line arguments into items array
n = len(sys.argv) - 1
items = []
for i in range(1, n):
    items.append(sys.argv[i])

price = SKU.calculate_price(items)

# Last command line argument is our expected price, below we test if our program has the
# expected output
if (price == float(sys.argv[n])):
    print(str(items) + " " + str(price) + " PASS")
else:
    print(str(items) + " " + str(price) + " FAIL")