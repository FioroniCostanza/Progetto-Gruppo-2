import pandas as pd

def leggi_parquet(path: str):
    """
    Funzione che legge file parquet e lo trasforma in DataFrame.

    Parameters
    ----------
    path : str

    Returns
    -------
    parquet : DataFrame

    """
    parquet = pd.read_parquet(path, engine='pyarrow')
    return parquet

def carica_zone():
    """
    Funzione che legge file csv e lo trasforma in DataFrame.

    Returns
    -------
    taxi_zones : DataFrame

    """
    taxi_zones = pd.read_csv('taxi+_zone_lookup.csv')
    return taxi_zones

def merge_dati(parquet, taxi_zones):
    """
    Funzione che fa un merge tra il DataFrame parquet e il DataFrame taxi_zones.

    Parameters
    ----------
    parquet : DataFrame
    
    taxi_zones : DataFrame

    Returns
    -------
    data : DataFrame

    """
    a = parquet[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'PULocationID', 'DOLocationID', 'fare_amount']]
    b = taxi_zones[['LocationID', 'Borough']]
    data = pd.merge(a, b, left_on='PULocationID', right_on='LocationID', how='left')
    return data

def pulizia_dati(data,anno,mese):
    """
    Funzione che elimina dati in eccesso.

    Parameters
    ----------
    data : DataFrame
    
    anno : str
    
    mese : str

    Returns
    -------
    data : DataFrame

    """
    if '0' in mese[0]:
        mese = int(mese.split('0')[1])
    else:
        mese = int(mese)
    data = data[['Borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count']]
    data = data[data['passenger_count'].notna()]
    data['passenger_count'] = data['passenger_count'].astype('int8')
    data = data[(data.tpep_pickup_datetime.dt.year == int(anno)) | (data.tpep_dropoff_datetime.dt.year == int(anno))]
    data = data[(data.tpep_pickup_datetime.dt.month == mese) | (data.tpep_dropoff_datetime.dt.month == mese)]
    return data

def individuazione_ore(data):
    """
    Funzione che trasforma i valori di pickup e dropoff in ore.

    Parameters
    ----------
    data : DataFrame

    """
    start = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour
    end = pd.to_datetime(data['tpep_dropoff_datetime']).dt.hour
    data['tpep_pickup_datetime'] = start
    data['tpep_dropoff_datetime'] = end
