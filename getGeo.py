import pandas as pd
import requests
import json

df = pd.read_csv("Restaurants.csv")
key = 'ENTER YOUR KEY HERE'

for i, row in df.iterrows():
    print('Iteration ' + str(i))
    apiAddress = str(df.at[i,'street'])+','+str(df.at[i,'zip'])+','+str(df.at[i,'city'])+','+str(df.at[i,'country'])
    print(apiAddress)
    parameters = {
        "key":key,
        "location": apiAddress
    }

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    data = response.text
    dataJson = json.loads(data)['results']
    lat = (dataJson[0]['locations'][0]['latLng']['lat'])
    lng = (dataJson[0]['locations'][0]['latLng']['lng'])
    
    df.at[i,'lat'] = lat
    df.at[i,'long'] = lng
    
df.to_csv('Restaurants_Geo.csv')