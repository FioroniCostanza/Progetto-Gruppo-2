from verify_error import *

def definizione_anno(numero_anni):
    """
    Funzione che permette di scegliere in input uno o più anni specifici a 
    partire dal 2009 fino al 2022.

    Parameters
    ----------
    numero_anni : int

    Returns
    -------
    anno : list of str

    """
    verifica_numero_anni(numero_anni)
    if numero_anni > 1:
        anno = input('Inserisci anni da analizzare (separati da spazi): ')
        anno = anno.split(' ')
        verifica_anno(anno)
        verifica_piu_anni(anno)
    else:
        anno = [input('Inserisci anno da analizzare: ')]
        verifica_anno(anno)
        verifica_unico_anno(anno)
    anno.sort()
    return anno

def definizione_mesi(condizione_mese):
    """
    Funzione che permette di scegliere in input uno o più mesi specifici oppure l'intero anno. 
    
    Parameters
    ----------
    condizione_mese : str: 's' o 'n'
        Se la condizione scelta è 's' allora ho la possibilità di scegliere uno o più mesi specifici,
        altrimente sceglie tutti i mesi dell'anno dato in ingresso.
    anno : str

    Returns
    -------
    mese : list of str

    """
    verifica_condizione_mese(condizione_mese)
    if condizione_mese == 'n':
        mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    else:
        numero_mesi = int(input('Quanti mesi vuoi analizzare? '))
        if numero_mesi > 1:
            mese = input('Inserisci mesi da analizzare (inserire i numeri separati da spazi, es: 01 02 ...): ')
            mese = mese.split(' ')
        else:
            mese = [input('Inserisci mese da analizzare (in numero, es: 01): ')]
    mese.sort()
    return mese

def definizione_borough(condizione_borough):
    """
    Funzione che permette di scegliere in input uno o più borough specifici oppure tutti.

    Parameters
    ----------
    condizione_borough : str: 's' o 'n'
        Se la condizione scelta è 's' allora ho la possibilità di scegliere un o più borough specifici,
        altrimente sceglie tutti i 7 borough disponibili.
        N.B. per completezza dei risultati si considera 'Unknown' come possibile scelta tra i borough

    Returns
    -------
    borough : list of str

    """
    verifica_condizione_borough(condizione_borough)
    if condizione_borough == 's':
        numero_borough = int(input('Quanti borough vuoi analizzare? '))
        if numero_borough > 1:
            borough = input('Inserisci il nome dei borough (separati da virgole): ')
            borough = borough.split(',')
        else:
            borough = [input('Inserisci il borough da analizzare: ')]
        borough.sort()
    else:
        borough = None
    return borough

def verifica_condizione_su_2022(anno,mese):
    """
    Questa funzione elimina i mesi non attualmente disponibili del 2022.

    Parameters
    ----------
    anno : str
    mese : list of str

    Returns
    -------
    mese : list of str

    """
    if anno == '2022':
        if '10' in mese:
            mese.remove('10')
        if '11' in mese:
            mese.remove('11')
        if '12' in mese:
            mese.remove('12')
    return mese

