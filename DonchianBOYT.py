#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[2]:


stocks=yf.download("AAPL")
stocks


# In[3]:


df=stocks[["Close"]]
df


# In[4]:


df.plot(figsize=(12,8),title="Closing Price",fontsize=12)
plt.show()


# In[5]:


period_high=20
df["highest"]=(df["Close"].rolling(window=period_high).max()).shift()


# In[8]:


df.loc["2020"].plot(figsize=(12,8),fontsize=12)
plt.show()


# In[9]:


df["Buy"]=np.where(df["Close"].shift()>df["highest"].shift(),1,0)


# In[11]:


period_low=40
df["lowest"]=(df["Close"].rolling(window=period_low).min()).shift()


# In[13]:


df["Sell"]=np.where(df["Close"].shift()<df["lowest"].shift(),1,0)


# In[14]:


df


# In[15]:


df_trades=df[(df.Buy==1)|(df.Sell==1)]
df_trades


# In[18]:


trade=df_trades[(df_trades.Buy.diff()==1)|(df_trades.Sell.diff()==1)]
trade


# In[19]:


df


# In[20]:


Buy_dates=[]
Sell_dates=[]
buys=[]
sells=[]
open_pos=False


# In[21]:


for i in range(len(df)):
    if df.Buy.iloc[i]:
        if open_pos==False:
            buys.append(i)
            open_pos=True
            Buy_dates.append(df.iloc[i].name)
    elif df.Sell.iloc[i]:
        if open_pos:
            sells.append(i)
            open_pos=False
            Sell_dates.append(df.iloc[i].name)
            


# In[22]:


print(len(buys))
print(len(sells))


# In[23]:


if len(buys)>len(sells):
    buys.pop(-1)
    Buy_dates.pop(-1)


# In[25]:


print(len(buys))
print(len(sells))


# In[27]:


check=pd.DataFrame({'buydate':Buy_dates,'selldate':Sell_dates,'buyprice':df.loc[Buy_dates].Close.values,'sellprice':df.loc[Sell_dates].Close.values})
check


# In[29]:


check["pnl_perc"]=(check.sellprice-check.buyprice)/check.buyprice
check


# In[31]:


check["cumm+pnl_perc"]=(check["pnl_perc"]+1).cumprod()
check


# In[34]:


totaltrades=len(check.pnl_perc)
totaltrades


# In[35]:


profits=df.loc[check.selldate].Close.values-df.loc[check.buydate].Close.values
profits


# In[37]:


i=0
profit_trades=len([i for i in profits if i>0])
profit_trades_perc=(profit_trades/totaltrades)*100


# In[38]:


print("No of profit trades = {}".format(profit_trades))
print("Win ratio = {}". format(profit_trades_perc))


# In[40]:


profits_perc=(df.loc[check.selldate].Close.values-df.loc[check.buydate].Close.values)/df.loc[check.buydate].Close.values


# In[41]:


avg_profit=profits_perc.mean()*100
avg_profit


# In[42]:


list_profits=(profits_perc+1).cumprod()
list_profits


# In[43]:


net_returns_perc=(list_profits[-1]-1)*100
net_returns_perc


# In[45]:


profits_perc.min()


# In[46]:


profits_perc.max()


# In[49]:


init_inv=1000
inv_ret=init_inv*(profits_perc+1).cumprod()
inv_ret[-1]


# In[53]:


def test_strategy(stock, buy_days, sell_days,invest):
    data=yf.download(stock)
    df=data.Close.to_frame()
    df["highest"]=(df["Close"].rolling(window=buy_days).max()).shift()
    df["Buy"]=np.where(df["Close"].shift()>df["highest"].shift(),1,0)
    df["lowest"]=(df["Close"].rolling(window=sell_days).min()).shift()
    df["Sell"]=np.where(df["Close"].shift()<df["lowest"].shift(),1,0)
    
    Buy_dates=[]
    Sell_dates=[]
    buys=[]
    sells=[]
    open_pos=False
    
    for i in range(len(df)):
        if df.Buy.iloc[i]:
            if open_pos==False:
                buys.append(i)
                open_pos=True
                Buy_dates.append(df.iloc[i].name)
        elif df.Sell.iloc[i]:
            if open_pos:
                sells.append(i)
                open_pos=False
                Sell_dates.append(df.iloc[i].name)
    
    if len(buys)>len(sells):
        buys.pop(-1)
        Buy_dates.pop(-1)
    
    check=pd.DataFrame({'buydate':Buy_dates,'selldate':Sell_dates,'buyprice':df.loc[Buy_dates].Close.values,'sellprice':df.loc[Sell_dates].Close.values})
    check["pnl_perc"]=(check.sellprice-check.buyprice)/check.buyprice
    check["cumm+pnl_perc"]=(check["pnl_perc"]+1).cumprod()
    
    profits_perc=(df.loc[check.selldate].Close.values-df.loc[check.buydate].Close.values)/df.loc[check.buydate].Close.values
    list_profits=(profits_perc+1).cumprod()
    net_returns_perc=(list_profits[-1]-1).round(3)*100
    
    inv_ret=init_inv*(profits_perc+1).cumprod()
    return_inv=inv_ret[-1]
    
    large_loss=profits_perc.min().round(3)*100
    large_profit=profits_perc.max().round(3)*100   
    
    return print("Returns perc= {}%".format(net_returns_perc)), print("Invested return= {}".format(return_inv)), print("Largest Loss= {}%".format(large_loss)), print("Largest Profit= {}%".format(large_profit))


    


# In[58]:


test_strategy("KO", 40, 40,1000)


# In[ ]:




