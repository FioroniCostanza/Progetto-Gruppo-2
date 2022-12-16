from collections import OrderedDict

import pandas as pd


def fasce_orarie(f:int):
    if f == 1:
        keys = ['0:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00', '5:00 - 6:00',
                '6:00 - 7:00', '7:00 - 8:00', '8:00 - 9:00', '9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
                '12:00 - 13:00', '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
                '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '22:00 - 23:00', '23:00 - 24:00']
    elif f == 3:
        keys = ['0:00 - 3:00', '3:00 - 6:00', '6:00 - 9:00', '9:00 - 12:00', '12:00 - 15:00', '15:00 - 18:00', '18:00 - 21:00', '21:00 - 24:00']
    elif f == 8:
        keys = ['0:00 - 8:00', '8:00 - 16:00', '16:00 - 24:00']
    else:
        keys = ['0:00 - 12:00', '12:00 - 24:00']
    return keys

def genera_identificatore_fascia(keys):
    id = []
    for i in range(len(keys)):
        id.append([int(keys[i].split(':')[0]),int(keys[i].split(' ')[2].split(':')[0])])
    return id

def calcolo_passeggeri_per_singola_zona(data, bor, keys):
    d = dict.fromkeys(keys,0)
    id = genera_identificatore_fascia(keys)
    data = data[data['Borough']==bor]
    for i in range(len(keys)):
        contatore = 0
        indici = []
        for j in range(id[i][0],id[i][1]):
            test_data = data[(data.tpep_pickup_datetime==j) | (data.tpep_dropoff_datetime==j) & (str(data.index) not in indici)]
            indici.append(str(test_data.index))
            contatore += test_data['passenger_count'].count()
        d[keys[i]] = contatore
    return d

def calcolo_passeggeri(data, keys, bor=None):
    fasce_orarie = {}
    if bor != None:
        for zone in bor:
            fasce_orarie[zone] = calcolo_passeggeri_per_singola_zona(data, zone, keys)
    else:
        boroughs = data['Borough'].unique()
        boroughs.sort()
        for zone in boroughs:
            fasce_orarie[zone] = calcolo_passeggeri_per_singola_zona(data, zone, keys)
        calcolo_passeggeri_totali(data,fasce_orarie,keys)
    return fasce_orarie

def calcolo_passeggeri_totali(data, d: dict, keys):
    boroughs = data['Borough'].unique()
    d['Total'] = dict.fromkeys(keys, 0)
    for bor in boroughs:
        for i in keys:
            d['Total'][i] += d[bor][i]

