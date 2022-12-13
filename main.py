from processing import *
from preprocessing import *
from csv import writer

def calcolo_singolo_mese(path,m):
    parquet = leggi_parquet(path)
    taxi_zones = carica_zone()
    data = merge_dati(parquet, taxi_zones)
    data = data.dropna(axis=0)
    data = pulizia_dati(data,anno,m)
    individuazione_ore(data)
    keys = fasce_orarie(fascia_oraria)
    #id = genera_identificatore_fascia(keys)
    d = calcolo_passeggeri(data, keys)
    return d

def salvataggio_su_file(d,m):
    ending = pd.DataFrame.from_dict(d)
    if condizione_mese == 's':
        with open(f'dati_ogni_{fascia_oraria}_ore_{mese}-{anno}.csv', 'a') as file:
            writer(file).writerow(['', '', '', '', '', '', '', '', ''])
            writer(file).writerow([m,'','','','','','','',''])
            writer(file).writerow(['', '', '', '', '', '', '', '', ''])
        ending.to_csv(f'dati_ogni_{fascia_oraria}_ore_{mese}-{anno}.csv', mode='a')
    else:
        with open(f'dati_ogni_{fascia_oraria}_ore_anno_{anno}.csv', 'a') as file:
            writer(file).writerow(['', '', '', '', '', '', '', '', ''])
            writer(file).writerow([m,'','','','','','','',''])
            writer(file).writerow(['', '', '', '', '', '', '', '', ''])
        ending.to_csv(f'dati_ogni_{fascia_oraria}_ore_anno_{anno}.csv', mode='a')


anno = input('Inserisci anno da analizzare: ')
condizione_mese = input('Vuoi analizzare un mese specifico? [s/n]: ')
if condizione_mese == 'n' and anno != '2022':
    mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
elif condizione_mese == 'n' and anno == '2022':
    mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
else:
    numero_mesi = int(input('Quanti mesi vuoi analizzare? '))
    if numero_mesi > 1:
        mese = input('Inserisci mesi da analizzare (inserire i numeri separati da spazi, es: 01 02 ...): ')
        mese = mese.split(' ')
    else:
        mese = input('Inserisci mese da analizzare (in numero, es: 01): ')

fascia_oraria = int(input('Durata della fascia oraria (inserire un valore tra 1,3,8,12): '))
mesi_in_lettere = {'01': 'Gennaio', '02': 'Febbraio', '03': 'Marzo', '04': 'Aprile', '05': 'Maggio', '06': 'Giugno',
                   '07': 'Luglio', '08': 'Agosto', '09': 'Settembre', '10': 'Ottobre', '11': 'Novembre', '12': 'Dicembre'}

if condizione_mese == 's':
    if numero_mesi>1:
        for m in mese:
            path = f'yellow_tripdata_{anno}-{m}.parquet'
            temp = calcolo_singolo_mese(path,m)
            salvataggio_su_file(temp, mesi_in_lettere[m])
            print('Mese ' + m + ' completato')

    else:
        path = f'yellow_tripdata_{anno}-{mese}.parquet'
        d = calcolo_singolo_mese(path,mese)
        salvataggio_su_file(d, mesi_in_lettere[mese])
else:
    for m in mese:
        path = f'yellow_tripdata_{anno}-{m}.parquet'
        temp = calcolo_singolo_mese(path,m)
        salvataggio_su_file(temp, mesi_in_lettere[m])
        print('Mese ' + m + ' completato')