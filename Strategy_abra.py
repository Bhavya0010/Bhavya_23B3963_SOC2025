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
        prices=pd.read_csv('/Users/bhavya/Documents/GitHub/AlgoTradingBacktester/data/abra_price.csv')
        ts=prices['timestamp']
         # Order("PRODUCT_NAME": str, price: int, quantity: int)
        ts=prices['timestamp']
        as1=prices['ask_price_1']
        as2=prices['ask_price_2']
        as3=prices['ask_price_3']
        ps1=prices['bid_price_1']
        ps2=prices['bid_price_1']
        ps3=prices['bid_price_1']
        def av(a):
            pa1=0;pa2=0;pa3=0;pb1=0;pb2=0;pb3=0;pa=0;pb=0
            if a==1:
                pa1+=sum(as1[0:2000])
                pa2+=sum(as2[0:2000])
                pa3+=sum(as3[0:2000])
                pb1+=sum(ps1[0:2000])
                pb2+=sum(ps2[0:2000])
                pb3+=sum(ps3[0:2000])
                pa=min(pa1,min(pa2,pa3))/2000
                pb=max(pb1,max(pb2,pb3))/2000
                return [pa,pb]
            if a==2:
                pa1+=sum(as1[2001:4000])
                pa2+=sum(as2[2001:4000])
                pa3+=sum(as3[2001:4000])
                pb1+=sum(ps1[2001:4000])
                pb2+=sum(ps2[2001:4000])
                pb3+=sum(ps3[2001:4000])
                pa=min(pa1,min(pa2,pa3))/2000
                pb=max(pb1,max(pb2,pb3))/2000
                return [pa,pb]
            if a==3:
                pa1+=sum(as1[4001:6000])
                pa2+=sum(as2[4001:6000])
                pa3+=sum(as3[4001:6000])
                pb1+=sum(ps1[4001:6000])
                pb2+=sum(ps2[4001:6000])
                pb3+=sum(ps3[4001:6000])
                pa=min(pa1,min(pa2,pa3))/2000
                pb=max(pb1,max(pb2,pb3))/2000
                return [pa,pb]
            if a==4:
                pa1+=sum(as1[6001:8000])
                pa2+=sum(as2[6001:8000])
                pa3+=sum(as3[6001:8000])
                pb1+=sum(ps1[6001:8000])
                pb2+=sum(ps2[6001:8000])
                pb3+=sum(ps3[6001:8000])
                pa=min(pa1,min(pa2,pa3))/2000
                pb=max(pb1,max(pb2,pb3))/2000
                return [pa,pb]
            if a==5:
                pa1+=sum(as1[8001:10000])
                pa2+=sum(as2[8001:10000])
                pa3+=sum(as3[8001:10000])
                pb1+=sum(ps1[8001:10000])
                pb2+=sum(ps2[8001:10000])
                pb3+=sum(ps3[8001:10000])
                pa=min(pa1,min(pa2,pa3))/2000
                pb=max(pb1,max(pb2,pb3))/2000
                return [pa,pb]
        p1=av(1)
        p2=av(2)
        p3=av(3)
        p4=av(4)
        p5=av(5)
        if state.timestamp<ts[2000]:
            if p1[1]>p1[0]:
                orders.append(Order("PRODUCT", p1[1]-3, 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p1[0]+3, -10)) # Negative quantity -> Sell order
            else:
                # Order("PRODUCT_NAME": str, price: int, quantity: int)
                orders.append(Order("PRODUCT", p1[1], 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p1[0], -10)) # Negative quantity -> Sell order
        elif state.timestamp>ts[2000] and state.timestamp<ts[4000]:
            if p2[1]>p2[0]:
                orders.append(Order("PRODUCT", p2[1]-3, 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p2[0]+3, -10)) # Negative quantity -> Sell order
            else:
                # Order("PRODUCT_NAME": str, price: int, quantity: int)
                orders.append(Order("PRODUCT", p2[1], 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p2[0], -10)) # Negative quantity -> Sell order
        elif state.timestamp>ts[4000] and state.timestamp<ts[6000]:
            if p3[1]>p3[0]:
                orders.append(Order("PRODUCT", p3[1]-3, 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p3[0]+3, -10)) # Negative quantity -> Sell order
            else:
                # Order("PRODUCT_NAME": str, price: int, quantity: int)
                orders.append(Order("PRODUCT", p3[1], 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p3[0], -10)) # Negative quantity -> Sell order
        elif state.timestamp>ts[6000] and state.timestamp<ts[8000]:
            if p4[1]>p4[0]:
                orders.append(Order("PRODUCT", p4[1]-3, 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p4[0]+3, -10)) # Negative quantity -> Sell order
            else:
                # Order("PRODUCT_NAME": str, price: int, quantity: int)
                orders.append(Order("PRODUCT", p4[1], 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p4[0], -10)) # Negative quantity -> Sell order
        elif state.timestamp>ts[8000]:
            if p5[1]>p5[0]:
                orders.append(Order("PRODUCT", p5[1]-3, 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p5[0]+3, -10)) # Negative quantity -> Sell order
            else:
                # Order("PRODUCT_NAME": str, price: int, quantity: int)
                orders.append(Order("PRODUCT", p5[1], 10)) # Positive quantity -> Buy order
                orders.append(Order("PRODUCT", p5[0], -10)) # Negative quantity -> Sell order
        result["PRODUCT"] = orders
        return result    