from src.backtester import Order
from src.backtester import Order, OrderBook
from typing import List
import pandas as pd
# Strategy.py must include the Trader class with a run() method
class Trader:
    '''
    INPUT:
        - state: holds information about market trades, timestamps, position etc.,
                 Some attributes may not be available right now. 
    OUTPUT:
        - results: Dict{"PRODUCT_NAME": List[Order]} 
                   holds your orders for each product in a dictionary
    '''
    
    def run(self, state,current_position):
        result = {}
        orders: List[Order] = []
        
        orders.append(Order("PRODUCT", 9998, 10)) # Positive quantity -> Buy order
        orders.append(Order("PRODUCT", 10002, -10)) # Negative quantity -> Sell order  
        result["PRODUCT"] = orders
        return result    