from postprocessing import Elaborazione
from condizioni import *
from verify_error import verifica_fascia_oraria
from calcola_e_salva import *
import sys

numero_anni = int(input('Quanti anni vuoi analizzare? '))
anno = definizione_anno(numero_anni)

condizione_mese = input('Vuoi analizzare un mese specifico? [s/n]: ')
mesi = definizione_mesi(condizione_mese)

condizione_borough = input('Vuoi analizzare un borough specifico? [s/n]: ')
borough = definizione_borough(condizione_borough)

fascia_oraria = int(input('Durata della fascia oraria (inserire un valore tra 1,3,8,12): '))
verifica_fascia_oraria(fascia_oraria)

e = Elaborazione(anno, mesi, borough, fascia_oraria)

if e.verifica_se_ricerca_gia_esistente(condizione_mese,condizione_borough):
    print('Attenzione!!!')
    print('La ricerca richiesta è già stata effettuata, ricerca il file tra i dati salvati')
    sys.exit()

calcolo_e_salvataggio(e,anno,mesi,borough,condizione_mese,condizione_borough)