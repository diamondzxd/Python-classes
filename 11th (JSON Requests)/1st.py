import requests
response=requests.get("http://gadgetworld.000webhostapp.com/getproducts.php?cid=10")
data=response.json()
#print(data)
for v in data:
    print(v["name"],v["price"],sep=" : ")
