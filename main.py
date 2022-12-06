import pandas as pd
import time

t1 = time.time()

anno = input('Inserisci anno da analizzare: ')
mese = input('Inserisci mese da analizzare: ')

prova = pd.read_parquet(f'yellow_tripdata_{anno}-{mese}.parquet', engine='pyarrow')

taxi_zones = pd.read_csv('taxi+_zone_lookup.csv')

a = prova[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'PULocationID', 'DOLocationID', 'fare_amount']]
b = taxi_zones[['LocationID', 'Borough']]

data = pd.merge(a, b, left_on='PULocationID', right_on='LocationID', how='left')

data = data[['PULocationID', 'DOLocationID', 'Borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count']]

data = data[data['passenger_count'].notna()]

start = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour
end = pd.to_datetime(data['tpep_dropoff_datetime']).dt.hour

data['tpep_pickup_datetime'] = start
data['tpep_dropoff_datetime'] = end

data['passenger_count'] = data['passenger_count'].astype('int8')
data['PULocationID'] = data['PULocationID'].astype('int16')
data['DOLocationID'] = data['DOLocationID'].astype('int16')

del a
del b
del start
del end

keywords = ['0:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00', '5:00 - 6:00',
            '6:00 - 7:00', '7:00 - 8:00', '8:00 - 9:00', '9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
            '12:00 - 13:00', '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
            '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '22:00 - 23:00', '23:00 - 24:00']

boroughs = data['Borough'].unique()
boroughs.sort()
print(boroughs)
fasce_orarie = dict.fromkeys(boroughs, dict)
id = []
for bor in boroughs:
    d = dict.fromkeys(keywords, 0)
    test_data = data[data['Borough'] == bor]
    test_data = test_data.reset_index(drop=True)
    for i in range(len(test_data)):
        partenza = test_data['tpep_pickup_datetime'][i] 
        arrivo = test_data['tpep_dropoff_datetime'][i]
        if partenza<23:
            for j in range(partenza,arrivo+1):
                d[keywords[j]] += int(test_data['passenger_count'][i])
        else: 
            d[keywords[partenza]] += int(test_data['passenger_count'][i])
            for k in range(0,arrivo+1):
                d[keywords[k]] += int(test_data['passenger_count'][i])
    fasce_orarie[bor] = d

fasce_orarie['Total'] = dict.fromkeys(keywords, 0)
for bor in boroughs:
    for i in keywords:
        fasce_orarie['Total'][i] += fasce_orarie[bor][i]

ending = pd.DataFrame.from_dict(fasce_orarie)
ending.to_csv('./prova_febbraio.csv')
t2 = time.time()
print(t2-t1)