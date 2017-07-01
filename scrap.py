import requests

d = {'loginid':'225H7882', 'password':'dse456$', 'lang1':'default'}
url = "https://bangladeshstockmarket.com/LoadBalance.do"
frame = "https://bangladeshstockmarket.com/Frame.jsp"
orderurl = "https://bangladeshstockmarket.com/OrderEntry.do"
order1url = "https://bangladeshstockmarket.com/Order1.do?exchangeSelected=CTG"
order1_data = {'spdBuySymbol':'', 'spdSellSymbol':'','submitbutton':'Submit', 'exchange':'CTG',
'selectProduct':'EQUITY', 'segment':'DELIVERY', 'symbol':'IDLC','buysell':'BUY',
'quantity':'1', 'referenceId':'','pricetype':'LIMIT','price':'5', 'triprice':'0',
'disquan':'', 'protectionPercent':'', 'filltype':'GFD','minFillQty':'',
 'expirydate':'','settlerid':'','priceViolation':'N','lotsize':'1', 'userExchangeList':'CTG',
  'hidboardtype':'NR'}
'''
spdBuySymbol:
spdSellSymbol:
submitbutton:Submit
exchange:CTG
selectProduct:EQUITY
segment:DELIVERY
symbol:IDLC
buysell:BUY
quantity:1
referenceId:
pricetype:LIMIT
price:5
triprice:0
disquan:
protectionPercent:
filltype:GFD
minFillQty:
expirydate:
settlerid:
priceViolation:N
lotsize:1
userExchangeList:CTG
hidboardtype:NR
'''

verifyPassword = "https://bangladeshstockmarket.com/PasswordCheck.do"
orderparams = {'exchange':'CTG', 'selectProduct':'EQUITY', 'segment':'DELIVERY', 'symbol':'ACI', 'buysell':'BUY', 'quantity':'7', 'referenceId':'', 'pricetype':'LIMIT', 'price':'5', 
'triprice':'0', 'disquan':'0', 'protectionPercent':'1', 'filltype':'GFD', 'minFillQty':'0', 'expirydate':'', 
'clentid':'225H7882','settlerid':'', 'priceViolation':'N', 'lotsize':'0', 'userExchangeList':'CTG', 'hidboardtype':'NR', 'submitbutton':'SUBMIT'}
with requests.Session() as s:
    r = s.post(url, data=d)
    #print r.text
    r = s.post(verifyPassword, data={'pagePassword':'dse456$'})
    print r.text
    r = s.post(order1url, data=order1_data)
    with open('data.txt', 'w+') as f:
        f.write(r.text)

