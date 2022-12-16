from processing import *
from preprocessing import *
from csv import writer
import pandas as pd

class Elaborazione:
    def __init__(self,anno,mesi,borough,fascia_oraria):
        self.anno = anno
        self.mesi = mesi
        self.borough = borough
        self.fascia_oraria = fascia_oraria

    def calcolo_singolo_mese(self,path,m,bor):
        parquet = leggi_parquet(path)
        taxi_zones = carica_zone()
        data = merge_dati(parquet, taxi_zones)
        data = data.dropna(axis=0)
        data = pulizia_dati(data,self.anno,m)
        individuazione_ore(data)
        keys = fasce_orarie(self.fascia_oraria)
        d = calcolo_passeggeri(data, keys, bor)
        return d

    def scrittura_su_csv(self,path,mese,risultato):
        with open(path, 'a', newline='') as file:
            writer(file).writerow([''])
            writer(file).writerow([mese])
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

    def salvataggio_su_file_mesi_separati(self,d,m,cond_mese,cond_bor):

        ending = self.genera_dataframe_e_ordina_fasce_orarie(d)

        if cond_mese == 's' and cond_bor == 's':
            percorso = f'dati_ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
            self.scrittura_su_csv(percorso,m,ending)

        elif cond_mese == 'n' and cond_bor == 's':
            percorso = f'dati_ogni_{self.fascia_oraria}_ore_anno_{self.anno}_borough_{self.borough}.csv'
            self.scrittura_su_csv(percorso,m,ending)

        elif cond_mese == 's' and cond_bor == 'n':
            percorso = f'dati_ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
            self.scrittura_su_csv(percorso,m,ending)

        else:
            percorso = f'dati_ogni_{self.fascia_oraria}_ore_anno_{self.anno}.csv'
            self.scrittura_su_csv(percorso,m,ending)

        return ending

    def salvataggio_su_file_mesi_aggregati(self,df,mesi,cond_mese,cond_bor):

        if cond_mese == 's' and cond_bor == 's':
            percorso = f'dati_aggregati_ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
            self.scrittura_su_csv(percorso,mesi,df)

        elif cond_mese == 'n' and cond_bor == 's':
            percorso = f'dati_aggregati_ogni_{self.fascia_oraria}_ore_anno_{self.anno}_borough_{self.borough}.csv'
            self.scrittura_su_csv(percorso, mesi, df)

        elif cond_mese == 's' and cond_bor == 'n':
            percorso = f'dati_aggregati_ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
            self.scrittura_su_csv(percorso, mesi, df)

        else:
            percorso = f'dati_aggregati_ogni_{self.fascia_oraria}_ore_anno_{self.anno}.csv'
            self.scrittura_su_csv(percorso, mesi, df)

#   A lavoro ultimato andrà inserita una verifica in maniera da non dover riscrivere il tutto se è già presente il file corrispondente
#   Ovvero, se è già presente il file, non saranno eseguite le operazioni, ma si stamperà solo un messaggio del tipo "la ricerca è già stata effettuata, controllare tra i file già generati")