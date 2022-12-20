def fasce_orarie(f:int):
    """
    Funzione che in base alla scelta della fascia oraria crea una lista di 
    stringhe che rappresenta tutte le fasce orarie da analizzare.

    Parameters
    ----------
    f : int

    Returns
    -------
    keys : list of str

    """
    if f == 1:
        keys = ['0:00 - 1:00', '1:00 - 2:00', '2:00 - 3:00', '3:00 - 4:00', '4:00 - 5:00', '5:00 - 6:00',
                '6:00 - 7:00', '7:00 - 8:00', '8:00 - 9:00', '9:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
                '12:00 - 13:00', '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
                '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '22:00 - 23:00', '23:00 - 24:00']
    elif f == 3:
        keys = ['0:00 - 3:00', '3:00 - 6:00', '6:00 - 9:00', '9:00 - 12:00', '12:00 - 15:00', '15:00 - 18:00', '18:00 - 21:00', '21:00 - 24:00']
    elif f == 8:
        keys = ['0:00 - 8:00', '8:00 - 16:00', '16:00 - 24:00']
    elif f == 12:
        keys = ['0:00 - 12:00', '12:00 - 24:00']
    return keys

def genera_identificatore_fascia(keys):
    """
    Creazione di un identificatore del tipo [x y] per ogni fascia, dove x è 
    l'inizio della fascia oraria ed y è la fine. 

    Parameters
    ----------
    keys : list of str

    Returns
    -------
    id : list of int

    """
    id = []
    for i in range(len(keys)):
        id.append([int(keys[i].split(':')[0]),int(keys[i].split(' ')[2].split(':')[0])])
    return id

def calcolo_passeggeri_per_singola_zona(data, bor, keys):
    """
    Funzione che per un borough alla volta controlla quanti passeggeri ci sono 
    per ogni fascia oraria.

    Parameters
    ----------
    data : DataFrame

    bor : str
        .
    keys : list of str

    Returns
    -------
    d : dict
        Restituisce un dizionario dove le chiavi sono le fasce orarie selezionate 
        e i valori sono il numero di passeggeri presenti in quella fascia.

    """
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
    """
    Funzione che in base alle condizioni date in ingresso rispetto ai borough, 
    mi restutisce un dizionario che ad ogni borough associa i passeggeri nelle 
    varie fasce orarie.
    
    Parameters
    ----------
    data : DataFrame
    
    keys : list of str
    
    bor : list of str

    Returns
    -------
    fasce_orarie : list of str

    """
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
    """
    Questa funzione aggiunge una colonna al DataFrame dove viene introdotto 
    il calcolo totale dei passeggeri per i borough selezionati.

    Parameters
    ----------
    data : DataFrame
    
    d : dict
    
    keys : list of str

    """
    boroughs = data['Borough'].unique()
    d['Total'] = dict.fromkeys(keys, 0)
    for bor in boroughs:
        for i in keys:
            d['Total'][i] += d[bor][i]

