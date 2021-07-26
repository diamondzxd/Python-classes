import requests

'''response=requests.get("http://gadgetworld.000webhostapp.com/getproducts.php?cid=8")
data=response.json()

data=list(filter(lambda x: float(x['price'])<50000, data))

for product in data:
    print(product['name'])
    print(product['price'])'''

#using through reduce
from functools import reduce

response=requests.get("http://gadgetworld.000webhostapp.com/getproducts.php?cid=8")
data=response.json()

product=reduce(lambda x,y:x if float(x['price']) > float(y['price']) else y, data)
