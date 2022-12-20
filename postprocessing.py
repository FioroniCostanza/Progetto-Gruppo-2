from processing import *
from preprocessing import *
from csv import writer
import pandas as pd
import os

class Elaborazione:
    def __init__(self,anno,mesi,borough,fascia_oraria):
        self.anno = anno
        self.mesi = mesi
        self.borough = borough
        self.fascia_oraria = fascia_oraria

    def calcolo_singolo_mese(self,path,m,bor,index):
        parquet = leggi_parquet(path)
        taxi_zones = carica_zone()
        data = merge_dati(parquet, taxi_zones)
        data = data.dropna(axis=0)
        data = pulizia_dati(data,self.anno[index],m)
        individuazione_ore(data)
        keys = fasce_orarie(self.fascia_oraria)
        d = calcolo_passeggeri(data, keys, bor)
        return d

    def genera_path(self, cond_mese, cond_bor, aggregazione_dati=''):
        if cond_mese == 's' and cond_bor == 's':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
        elif cond_mese == 'n' and cond_bor == 's':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_anno_{self.anno}_borough_{self.borough}.csv'
        elif cond_mese == 's' and cond_bor == 'n':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
        else:
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_anno_{self.anno}.csv'
        return percorso

    def verifica_se_ricerca_gia_esistente(self, cond_mese, cond_bor):
        percorso = self.genera_path(cond_mese,cond_bor)
        if os.path.exists(percorso):
            return True
        else:
            return False

    def scrittura_su_csv(self,path,mese,risultato,index=None):
        with open(path, 'a', newline='') as file:
            writer(file).writerow([''])
            if index != None:
                writer(file).writerow(['Mese','Anno'])
                writer(file).writerow([(', '.join(mese)),self.anno[index]])
            else:
                writer(file).writerow(['Mesi', 'Anni'])
                writer(file).writerow([(', '.join(mese)), (', '.join(self.anno))])
            writer(file).writerow([''])
        risultato.to_csv(path,mode ='a')

    def genera_dataframe_e_ordina_fasce_orarie(self,d):
        temp = list(d.values())[0]
        orari = []
        for keys, values in temp.items():
            orari.append(keys)
        ending = pd.DataFrame.from_dict(d)
        ending = ending.reindex(orari)
        return ending

    def salvataggio_su_file_mesi_separati(self,d,index,m,cond_mese,cond_bor):
        ending = self.genera_dataframe_e_ordina_fasce_orarie(d)
        percorso = self.genera_path(cond_mese,cond_bor) #in questo caso non specifico il tipo di dati poiché non ho dati aggregati nel file per singolo mese
        self.scrittura_su_csv(percorso,[m],ending,index)
        return ending

    def salvataggio_su_file_mesi_aggregati(self,df,index,mesi,cond_mese,cond_bor):
        aggregazione_dati = 'mesi_aggregati_'
        percorso = self.genera_path(cond_mese,cond_bor,aggregazione_dati)
        self.scrittura_su_csv(percorso, mesi, df, index)

    def salvataggio_su_file_anni_aggregati(self, df, mesi, cond_mese, cond_bor):
        aggregazione_dati = 'anni_aggregati_'
        percorso = self.genera_path(cond_mese,cond_bor,aggregazione_dati)
        if cond_mese == 's':
            self.scrittura_su_csv(percorso, mesi, df)
        else:
            self.scrittura_su_csv(percorso, '', df)
        # Questa ultima condizione viene inserita per non generare confusione nel file nel caso in cui si richiedano valori su interi anni,
        # perché, nel caso in cui sia presente il 2022, esso arriva fino a Settembre e non fino a Dicembre, per cui potrebbero essere presenti alcune incongruenze
        # N.B. Ciò non inficia nel calcolo, è semplicemente una correzione grafica all'interno del CSV risultante

#   A lavoro ultimato andrà inserita una verifica in maniera da non dover riscrivere il tutto se è già presente il file corrispondente
#   Ovvero, se è già presente il file, non saranno eseguite le operazioni, ma si stamperà solo un messaggio del tipo "la ricerca è già stata effettuata, controllare tra indice_anno file già generati")