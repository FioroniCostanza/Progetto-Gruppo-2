from condizioni import *
from matplot import *

def calcolo_e_salvataggio(e,anno,mesi_in_numero,borough,cond_mese,cond_borough,fascia_oraria):
    mesi_in_lettere = {'01': 'Gennaio', '02': 'Febbraio', '03': 'Marzo', '04': 'Aprile', '05': 'Maggio', '06': 'Giugno',
                       '07': 'Luglio', '08': 'Agosto', '09': 'Settembre', '10': 'Ottobre', '11': 'Novembre',
                       '12': 'Dicembre'}
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
            dataframe_mesi.append(e.salvataggio_su_file_mesi_separati(temp, indice_anno, mesi_in_lettere[m], cond_mese,cond_borough))
            if len(anno) == 1:
                if len(mese) == 1:
                    grafici(temp,mesi_in_lettere[m],a,fascia_oraria)
            print('Mese ' + m + '-' + a + ' completato')
        if len(dataframe_mesi)>1:
            for j in range(1, len(dataframe_mesi)):
                tot.append(dataframe_mesi[0].add(dataframe_mesi[j]))
            if (len(anno) == 1):
                grafici(tot,'Aggregato_Mensile',a,fascia_oraria)
            e.salvataggio_su_file_mesi_aggregati(tot[indice_anno], indice_anno, mesi, cond_mese, cond_borough)
            indice_anno += 1


    # if len(anno) > 1: #pongo questa condizione perché l'aggregazione per il singolo anno sarebbe inutile in quanto risulterebbe uguale all'aggregazione per mesi
    #     for i in range(1, len(tot)):
    #         totale = tot[0].add(tot[i])
    #     e.salvataggio_su_file_anni_aggregati(totale, mesi, cond_mese, cond_borough)
    #     grafici(totale,'Aggregato_annuale',a,fascia_oraria)

    if len(anno) > 1:
            totale = tot[0]
            for i in range(1, len(tot)):
                totale.add(tot[i])
            e.salvataggio_su_file_anni_aggregati(totale, mesi, cond_mese, cond_borough)
            grafici(totale,'Aggregato','annuale',fascia_oraria)