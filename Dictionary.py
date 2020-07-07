Fuel_Type = {"Petrol":1,"Diesel":2,"CNG":3}
print(Fuel_Type)

print(Fuel_Type['Petrol'])

print(Fuel_Type.keys()) 

print(Fuel_Type.values())

print(Fuel_Type.items())

Fuel_Type['adarsh']=5

print(Fuel_Type)

Fuel_Type.update({'mani':6,'electric':7})
print(Fuel_Type)

for i in Fuel_Type.items():
    print(i)

import numpy as np