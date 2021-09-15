
from nsetools import Nse  

import pandas as pd
def getNselive(stocknames):
    d={}
    nse=Nse()
    for i in stocknames:
        info = nse.get_quote(i)
        d[i]=info

    res={}
    for di in d:
        res[di]= dict((k,d[di][k]) for k in ['closePrice','dayHigh','dayLow','deliveryQuantity','deliveryToTradedQuantity','open','totalTradedVolume'] )

    return res
stocknames=['reliance', 'hdfcbank', 'adaniports','sbicard', 'itc', 'ioc', 'rblbank']

result=getNselive(stocknames)
new = pd.DataFrame.from_dict(result)
  
print(new)


