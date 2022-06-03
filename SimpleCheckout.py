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

SKU = SimpleCheckout()

# Using the prices defined in the problem specification
SKU.set_prices(0.50, 0.75, 0.25)

# Using the special prices defined in the problem specification
special_A = [0, 0, 0]
special_B = [0, 2, 1.25]
special_C = [1, 3, 1]
SKU.set_special_prices(special_A, special_B, special_C)