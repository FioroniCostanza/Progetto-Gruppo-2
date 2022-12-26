from calcolo_passeggeri import *
from preprocessing import *
from csv import writer
import pandas as pd
import os

class Elaborazione:
    def __init__(self,anno,mesi,borough,fascia_oraria):
        """
        Costruttore della classe Elaborazione

        Parameters
        ----------
        anno : list of str
        
        mesi : list of str
        
        borough : list of str
        
        fascia_oraria : int
        
        """
        self.anno = anno
        self.mesi = mesi
        self.borough = borough
        self.fascia_oraria = fascia_oraria

    def calcolo_singolo_mese(self,path,m,bor,index):
        """
        Funzione che calcola il numero di passeggeri per ogni borough dato in 
        input per un solo mese. 

        Parameters
        ----------
        path : str
        
        m : str
        
        bor : list of str
        
        index : int

        Returns
        -------
        d : dict

        """
        parquet = leggi_parquet(path)
        taxi_zones = carica_zone()
        data = merge_dati(parquet, taxi_zones)
        data = pulizia_dati(data,self.anno[index],m)
        individuazione_ore(data)
        keys = fasce_orarie(self.fascia_oraria)
        d = calcolo_passeggeri(data, keys, bor)
        return d

    def genera_path(self, cond_mese, cond_bor, aggregazione_dati=''):
        """
        Funzione che in base alle condizioni in input del mese e del borough 
        genera un percorso di un file.

        Parameters
        ----------
        cond_mese : str
        
        cond_bor : str
            
        aggregazione_dati : str 
            Specifica se i dati vengono raggruppatin per anno o per mesi.
            Di default è settato come '' e indica che i dati non vengono raggruppati,
            ma saranno calcolati per singolo mese.

        Returns
        -------
        percorso : str

        """
        if cond_mese == 's' and cond_bor == 's':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}_borough_{self.borough}.csv'
        elif cond_mese == 'n' and cond_bor == 's':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_anno_{self.anno}_borough_{self.borough}.csv'
        elif cond_mese == 's' and cond_bor == 'n':
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_{self.mesi}-{self.anno}.csv'
        else:
            percorso = f'Results/dati_{aggregazione_dati}ogni_{self.fascia_oraria}_ore_anno_{self.anno}.csv'
        return percorso

    def verifica_se_ricerca_gia_esistente(self, cond_mese, cond_bor):
        """
        Funzione che verifica l'esistenza o meno di un percorso, così da non 
        stampare dati in eccesso. 

        Parameters
        ----------
        cond_mese : str
        
        cond_bor : str

        Returns
        -------
        bool
            True: esiste già un percorso -> quindi non genera ulteriori dati
            False: non esiste nessun percorso così -> quindi esegue lo script per generare nuovi dati

        """
        percorso = self.genera_path(cond_mese,cond_bor)
        if os.path.exists(percorso):
            return True
        else:
            return False

    def scrittura_su_csv(self,path,mese,risultato,index=None):
        """
        Funzione che genera un file csv dove stampare i risultati ottenuti, 
        in base a quanti anni e mesi sono stati selezionati.

        Parameters
        ----------
        path : str
        
        mese : str
        
        risultato : DataFrame
        
        index : int

        """
        if not os.path.exists('Results'):
            os.makedirs('Results')
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
        """
        Questa funzione trasforma il dizionario ottenuto in calcolo_singolo_mese 
        in un DataFrame e ordina le fasce orarie.

        Parameters
        ----------
        d : dict

        Returns
        -------
        risultato : DataFrame

        """
        temp = list(d.values())[0]
        orari = []
        for keys, values in temp.items():
            orari.append(keys)
        risultato = pd.DataFrame.from_dict(d)
        risultato = risultato.reindex(orari)
        return risultato

    def salvataggio_su_file_mesi_separati(self,d,index,m,cond_mese,cond_bor):
        """
        Questa funzione salva i dati generati per singolo mese in un file csv.
        Infine restituisce un DataFrame per poter calcolare i dati raggruppati per mesi.

        Parameters
        ----------
        d : dict
        
        index : int
        
        m : str
        
        cond_mese : str
        
        cond_bor : str

        Returns
        -------
        ending : DataFrame
        

        """
        risultato = self.genera_dataframe_e_ordina_fasce_orarie(d)
        percorso = self.genera_path(cond_mese,cond_bor) #in questo caso non specifico il tipo di aggregazione dati poiché non ho dati aggregati nel file per singolo mese
        self.scrittura_su_csv(percorso,[m],risultato,index)
        return risultato

    def salvataggio_su_file_mesi_aggregati(self,df,index,mesi,cond_mese,cond_bor):
        """
        Questa funzione salva i dati aggregati per mesi in un file csv.

        Parameters
        ----------
        df : DataFrame
        
        index : int
        
        mesi : list of str
        
        cond_mese : str
        
        cond_bor : str

        """
        aggregazione_dati = 'mesi_aggregati_'
        percorso = self.genera_path(cond_mese,cond_bor,aggregazione_dati)
        self.scrittura_su_csv(percorso, mesi, df, index)

    def salvataggio_su_file_anni_aggregati(self, df, mesi, cond_mese, cond_bor):
        """
        Questa funzione salva i dati aggregati per anni in un file csv.

        Parameters
        ----------
        df : DataFrame
        
        mesi : list of str
        
        cond_mese : str
        
        cond_bor : str
        
        """
        aggregazione_dati = 'anni_aggregati_'
        percorso = self.genera_path(cond_mese,cond_bor,aggregazione_dati)
        if cond_mese == 's':
            self.scrittura_su_csv(percorso, mesi, df)
        else:
            self.scrittura_su_csv(percorso, '', df)
        # Questa ultima condizione viene inserita per non generare confusione nel file nel caso in cui si richiedano valori su interi anni,
        # perché, nel caso in cui sia presente il 2022, esso arriva fino a Ottobre e non fino a Dicembre, per cui potrebbero essere presenti alcune incongruenze
        # N.B. Ciò non inficia nel calcolo, è semplicemente una correzione grafica all'interno del CSV risultante
