from postprocessing import Elaborazione
from condizioni import *

anno = input('Inserisci anno da analizzare: ')

condizione_mese = input('Vuoi analizzare un mese specifico? [s/n]: ')
mese = definizione_mesi(condizione_mese,anno)

condizione_borough = input('Vuoi analizzare un borough specifico? [s/n]: ')
borough = definizione_borough(condizione_borough)

fascia_oraria = int(input('Durata della fascia oraria (inserire un valore tra 1,3,8,12): '))

mesi_in_lettere = {'01': 'Gennaio', '02': 'Febbraio', '03': 'Marzo', '04': 'Aprile', '05': 'Maggio', '06': 'Giugno',
                   '07': 'Luglio', '08': 'Agosto', '09': 'Settembre', '10': 'Ottobre', '11': 'Novembre', '12': 'Dicembre'}

e = Elaborazione(anno,mese,borough,fascia_oraria)

dataframe_mesi=[]
mesi=[]
for m in mese:
    path = f'yellow_tripdata_{anno}-{m}.parquet'
    temp = e.calcolo_singolo_mese(path,m,borough)
    mesi.append(mesi_in_lettere[m])
    dataframe_mesi.append(e.salvataggio_su_file_mesi_separati(temp, mesi_in_lettere[m], condizione_mese, condizione_borough))
    print('Mese ' + m + ' completato')

for i in range(1,len(dataframe_mesi)):
    tot = dataframe_mesi[0].add(dataframe_mesi[i])
e.salvataggio_su_file_mesi_aggregati(tot, mesi, condizione_mese, condizione_borough)