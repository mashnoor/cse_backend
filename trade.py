import requests

symbol = raw_input("Enter Symbol")
qty = raw_input("Enter Quantity")
price = raw_input("Enter price")

d = {'loginid':'225H7882', 'password':'dse456$', 'lang1':'default'}
url = "https://bangladeshstockmarket.com/LoadBalance.do"
frame = "https://bangladeshstockmarket.com/Frame.jsp"
orderurl = "https://bangladeshstockmarket.com/OrderEntry.do"
order1url = "https://bangladeshstockmarket.com/Order1.do?exchangeSelected=CTG"
order1_data = {'spdBuySymbol':'', 'spdSellSymbol':'','submitbutton':'Submit', 'exchange':'CTG',
'selectProduct':'EQUITY', 'segment':'DELIVERY', 'symbol':symbol,'buysell':'BUY',
'quantity':qty, 'referenceId':'','pricetype':'LIMIT','price':price, 'triprice':'0',
'disquan':'', 'protectionPercent':'', 'filltype':'GFD','minFillQty':'',
 'expirydate':'','settlerid':'','priceViolation':'N','lotsize':'1', 'userExchangeList':'CTG',
  'hidboardtype':'NR'}

verifyPassword = "https://bangladeshstockmarket.com/PasswordCheck.do"

with requests.Session() as s:
    r = s.post(url, data=d)
    #print r.text
    r = s.post(verifyPassword, data={'pagePassword':'dse456$'})
    print r.text
    r = s.post(order1url, data=order1_data)
    print r.text
    with open('data.txt', 'w+') as f:
        f.write(r.text)

