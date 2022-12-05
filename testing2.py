import pandas as pd
import time
# import numpy as np
# import matplotlib as plt
t1 = time.time()
prova = pd.read_parquet('/Users/stefanoperone01/Desktop/Università/Programmazione/Progetto 2/yellow_tripdata_2022-01.parquet', engine='pyarrow')
taxi_zones = pd.read_csv('/Users/stefanoperone01/Desktop/Università/Programmazione/Progetto 2/taxi+_zone_lookup.csv')

a = prova[['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'PULocationID', 'DOLocationID', 'fare_amount']]
b = taxi_zones[['LocationID', 'Borough']]

data = pd.merge(a, b, left_on='PULocationID', right_on='LocationID', how='left')

data = data[['VendorID', 'PULocationID', 'DOLocationID', 'Borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count']]

data = data[data['passenger_count'].notna()]

# a = pd.to_datetime(data['tpep_pickup_datetime']).dt.time
# b = pd.to_datetime(data['tpep_dropoff_datetime']).dt.time

start = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour
end = pd.to_datetime(data['tpep_dropoff_datetime']).dt.hour
start = start.astype('str')
end = end.astype('str')
data['passenger_count'] = data['passenger_count'].astype('int8')
data['VendorID'] = data['VendorID'].astype('int8')
data['PULocationID'] = data['PULocationID'].astype('int16')
data['DOLocationID'] = data['DOLocationID'].astype('int16')
data['tpep_pickup_datetime'] = start
data['tpep_dropoff_datetime'] = end
del a
del b
del start
del end
# print(data)
# print(data[['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']])
keywords = ['0:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00', '5:00 - 6:00',
            '6:00 - 7:00', '7:00 - 8:00', '8:00 - 9:00', '9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
            '12:00 - 13:00', '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
            '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '22:00 - 23:00', '23:00 - 24:00']
boroughs = data['Borough'].unique()
boroughs.sort()
print(boroughs)
fasce_orarie = dict.fromkeys(boroughs, dict)
id = []
for i in range(len(keywords)):
    id.append([keywords[i].split(':')[0], keywords[i]])
for bor in boroughs:
    d = dict.fromkeys(keywords, 0)
    test_data = data[data['Borough'] == bor]
    test_data = test_data.reset_index(drop=True)
    for i in range(len(test_data)):
        for j in range(len(keywords)):
            if test_data['tpep_pickup_datetime'][i] == id[j][0] and test_data['tpep_dropoff_datetime'][i] == id[j][0]:
                d[id[j][1]] += int(test_data['passenger_count'][i])
            elif j < 23 and test_data['tpep_pickup_datetime'][i] == id[j][0] and test_data['tpep_dropoff_datetime'][i] == id[j + 1][0]:
                d[id[j][1]] += int(test_data['passenger_count'][i])
                d[id[j + 1][1]] += int(test_data['passenger_count'][i])
            elif j == 23 and test_data['tpep_pickup_datetime'][i] == id[j][0] and test_data['tpep_dropoff_datetime'][i] == id[0][0]:
                d[id[j][1]] += int(test_data['passenger_count'][i])
                d[id[0][1]] += int(test_data['passenger_count'][i])
    fasce_orarie[bor] = d

fasce_orarie['Total'] = dict.fromkeys(keywords, 0)
for bor in boroughs:
    for i in keywords:
        fasce_orarie['Total'][i] += fasce_orarie[bor][i]

# with open('/Users/stefanoperone01/Desktop/Università/Programmazione/Progetto 2/prova3.json', "w") as outfile:
# json.dump(fasce_orarie, outfile)
ending = pd.DataFrame.from_dict(fasce_orarie)
ending.to_csv('/Users/stefanoperone01/Desktop/Università/Programmazione/Progetto 2/prova_gennaio.csv')
t2 = time.time()
print(t2-t1)
