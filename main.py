from elaborazione import Elaborazione
from condizioni import *
from verify_error import *
from calcola_e_salva import *
import sys

# Possibilità di inserire:
# - N°anni da analizzare e anno/i specifico/i
# - N°mesi da analizzare e mese/i specifico/i
# - N°borough da analizzare e borough specifico/i
# - Tipologia di fascia oraria che voglio analizzare

cartella = input('Inserisci il path della cartella in cui sono presenti i dataset: ')
numero_anni = int(input('Quanti anni vuoi analizzare? '))
anno = definizione_anno(numero_anni)

condizione_mese = input('Vuoi analizzare un mese specifico? [s/n]: ')
mesi = definizione_mesi(condizione_mese)
verifica_numero_mesi(anno, mesi)

condizione_borough = input('Vuoi analizzare un borough specifico? [s/n]: ')
borough = definizione_borough(condizione_borough)

fascia_oraria = int(input('Durata della fascia oraria (inserire un valore tra 1,3,8,12): '))
verifica_fascia_oraria(fascia_oraria)

# Richiamo la classe elaborazione passandogli in ingresso tutti gli input inseriti
e = Elaborazione(anno, mesi, borough, fascia_oraria)

# Condizione che controlla se è stata effettuata la stessa ricerca, così da non salvare ulteriormente i dati
if e.verifica_se_ricerca_gia_esistente(condizione_mese,condizione_borough):
    print('Attenzione!!!')
    print('La ricerca richiesta è già stata effettuata, ricerca i file tra i dati salvati')
    sys.exit()

calcolo_e_salvataggio(e,anno,mesi,borough,condizione_mese,condizione_borough,fascia_oraria,cartella)
