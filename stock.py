import yfinance as yf
#for example here I'm using FB(facebook) as a searching stock name
stock = yf.Ticker("FB")
data = stock.history (period="Id",start ="2021-1-1",end ="2021-1-29")
print(data)
