# SimpleCheckout
The SimpleCheckout class has instance variables for base prices and special prices. These can both be altered by using the
setter methods set_prices() and set_special_prices().

The calculate_prices() function runs in O(n) time where n is the number of items in the input array. This function
uses a Counter dictionary/hashmap to count the number of each type of item in the input array. We then use this to
calculate the total price for the array.

    Multi priced offer:
    We use integer division to find out how many times the special offer can be applied.
    We use the modulo to work out the number of items left over that will be priced at the original price.

    Buy n get 1 free:
    We use Integer division to find out how many times the special offer can be applied.
    We subtract this from our total count as we know this is the number of free items we have.

I believe this function handles most if not all the possible edge cases, it works on an empty array and arrays of length 1. 
Test cases including extremely large arrays have not been added, which may be where some edge cases have been missed.
For error handling we use type hinting so that invalid data types cannot be passed into the calculate_price() function, 
any invalid input that is a string will not impact the total price as our calculate_price function only looks for 
items labelled 'A', 'B' or 'C'.