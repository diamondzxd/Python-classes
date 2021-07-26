import requests
import datetime
'''response=requests.get("https://tools.learningcontainer.com/sample-json.json")
data=response.json()
print("name",data["firstName"]+" "+data["lastName"],sep=" : ")
print("Gender",data["gender"])
print("Age",data["age"])
print("Address",data["address"]["streetAddress"],data["address"]["city"],data["address"]["state"],data["address"]["postalCode"],sep=", ")
'''

#Testing Delhivery's API for shipment tracking
response=requests.get("https://track.delhivery.com/api/packages/json/?token=69913e883cd7443bf868fa4bb6bcf377340a934f&waybill=1784510012891&verbose=2")
data=response.json()
#print(data)
shipment_data=data["ShipmentData"]

for ShipmentData in shipment_data:
    scan_data=ShipmentData["Shipment"]["Scans"]
    for scans in scan_data:
        #print(scans["ScanDetail"]["ScanDateTime"])
        print(datetime.datetime.strptime(scans["ScanDetail"]["ScanDateTime"][:19],'%Y-%m-%dT%H:%M:%S'))
        
        parameters=(scans["ScanDetail"]["ScanDateTime"])
        print(scans["ScanDetail"]["ScanDateTime"], scans["ScanDetail"]["Scan"],scans["ScanDetail"]["Instructions"])
        #print("test")
        #print(scan_data["Scans"][0]["ScanDetail"]["ScanType"])

