from postprocessing import Elaborazione
from condizioni import *
from verifyerror import *

numero_anni = int(input('Quanti anni vuoi analizzare? '))
error_verifica_numero_anni = verifica_numero_anni(numero_anni)
if numero_anni > 1:
    anno = input('Inserisci anni da analizzare (separati da spazi): ')
    anno = anno.split(' ')
    error_verifica_anno = verifica_anno(anno)
    error_verifica_piu_anni = verifica_piu_anni(anno)
else:
    anno = [input('Inserisci anno da analizzare: ')]
    error_verifica_anno = verifica_anno(anno)
    error_verifica_unico_anno = verifica_unico_anno(anno)

condizione_mese = input('Vuoi analizzare un mese specifico? [s/n]: ').lower()
error_condizoni_mese = verifica_condizione_mese(condizione_mese)
mesi_in_numero = definizione_mesi(condizione_mese, anno)

condizione_borough = input('Vuoi analizzare un borough specifico? [s/n]: ').lower()
error_condizioni_borough = verifica_condizione_borough(condizione_borough)
borough = definizione_borough(condizione_borough)

fascia_oraria = int(input('Durata della fascia oraria (inserire un valore tra 1,3,8,12): '))
error_fascia_oraria = verifica_fascia_oraria(fascia_oraria)
mesi_in_lettere = {'01': 'Gennaio', '02': 'Febbraio', '03': 'Marzo', '04': 'Aprile', '05': 'Maggio', '06': 'Giugno',
                   '07': 'Luglio', '08': 'Agosto', '09': 'Settembre', '10': 'Ottobre', '11': 'Novembre',
                   '12': 'Dicembre'}

e = Elaborazione(anno, mesi_in_numero, borough, fascia_oraria)

dataframe_mesi = []
indice_anno = 0
tot = []
for a in anno:
    mese = verifica_condizione_su_2022(a,mesi_in_numero)
    mesi = [] # inizializzo ogni volta la variabile e perché i mesi possono variare essendoci la condizione sul 2022
    for m in mese:
        path = f'Datasets/yellow_tripdata_{a}-{m}.parquet'
        temp = e.calcolo_singolo_mese(path, m, borough, indice_anno)
        mesi.append(mesi_in_lettere[m])
        dataframe_mesi.append(e.salvataggio_su_file_mesi_separati(temp, indice_anno, mesi_in_lettere[m], condizione_mese,condizione_borough))
        print('Mese ' + m + '-' + a + ' completato')

    for j in range(1, len(dataframe_mesi)):
        tot.append(dataframe_mesi[0].add(dataframe_mesi[j]))
    e.salvataggio_su_file_mesi_aggregati(tot[indice_anno], indice_anno, mesi, condizione_mese, condizione_borough)
    indice_anno += 1

if numero_anni > 1: #pongo questa condizione perché l'aggregazione per il singolo anno sarebbe inutile in quanto risulterebbe uguale all'aggregazione per mesi
    for i in range(1, len(tot)):
        totale = tot[0].add(tot[i])
    e.salvataggio_su_file_anni_aggregati(totale, mesi, condizione_mese, condizione_borough)
