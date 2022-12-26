def verifica_numero_anni(numero_anni):
    """
    Verifica la quantità di anni da analizzare.

    Parameters
    ----------
    numero_anni : int

    """
    if (numero_anni > 14):
        raise Exception(f'Al momento non sono disponibili {numero_anni} anni. Puoi inserirne al massimo 14!')


def verifica_piu_anni(anno):
    """
    Verifica numero di anni inseriti, nel caso in cui si abbia scelto 
    l'opzione di analizzare più anni.

    Parameters
    ----------
    anno : list of str

    """
    if len(anno) < 2: #in questo caso anno=['anno1', anno2'] quindi si puo' controllare direttamente la lunghezza di anno. 
        raise Exception(f'Hai inserito solo il {anno}. Inserisci più anni!')


def verifica_unico_anno(anno):
    """
    Verifica numero di anni inseriti, nel caso in cui si abbia scelto 
    l'opzione di analizzare un unico anno.

    Parameters
    ----------
    anno : list of str

    """
    if len(anno[0]) > 4: #in questo caso anno=['anno1 anno2'] quindi si deve controllare la lungezza della PRIMA stringa di anno.
        raise Exception(f' Hai inserito {anno} come anni da analizzare. Inserisci un solo anno!')


def verifica_anno(anno):
    """
    Verifica per tutti gli anni dati in input che l'anno scelto sia un anno 
    compreso tra il 2009 e il 2022.

    Parameters
    ----------
    anno : list of str

    """
    for i in anno:
        if int(i) not in range(2009, 2023):
            raise Exception(f'Anno {i} non valido, scegliere un anno dal 2009 al 2022')


def verifica_condizione_mese(condizione_mese):
    """
    Verifica opzione scelta.

    Parameters
    ----------
    condizione_mese : str

    """
    if (condizione_mese != 's') and (condizione_mese != 'n'):
        raise Exception(f'Opzione {condizione_mese} non disponibile. Scegliere solo tra s o n!')


def verifica_numero_mesi(anno, mesi):
    """
    Verifica la quantità di mesi del 2022 da analizzare.

    Parameters
    ----------
    anno : list of str
    
    numero_mesi : int

    """
    
    for i in anno:
        if (int(i) == 2022) :
            if (len(mesi) > 9):
                raise Exception(f'Per il 2022 non sono disponibili {len(mesi)} mesi. Sceglierne massimo 9.')
            for m in ['10','11','12']:
                if m in mesi:
                    raise Exception(f'Per il 2022 non è disponibile il mese {m}. Scegliere massimo fino a 09.')


def verifica_piu_mesi(mese):
    """
    Verifica numero di mesi inseriti, nel caso in cui si abbia scelto 
    l'opzione di analizzare più mesi.


    Parameters
    ----------
    mese : list of str

    """
    if len(mese) < 2: #in questo caso mese=['mese1', mese2'] quindi si puo' controllare direttamente la lunghezza di mese. 
        raise Exception(f'Hai inserito solo {mese}. Inserisci più mesi!')


def verifica_unico_mese(mese):
    """
    Verifica numero di mesi inseriti, nel caso in cui si abbia scelto 
    l'opzione di analizzare un unico mese.

    Parameters
    ----------
    mese : list of str

    """
    if len(mese[0]) > 2: #in questo caso mese=['mese1 mese2']  quindi si deve controllare la lungezza della PRIMA stringa di mese.
        raise Exception(f' Hai inserito {mese} come mesi da analizzare. Inserisci un solo mese!')


def verifica_condizione_borough(condizione_borough):
    """
    Verifica opzione scelta.

    Parameters
    ----------
    condizione_borough : str

    """
    if (condizione_borough != 's') and (condizione_borough != 'n'):
        raise Exception(f'Opzione {condizione_borough} non disponibile. Scegliere solo tra s o n!')


def verifica_numero_borough(numero_borough):
    """
    Verifica la quantità di borough da analizzare.

    Parameters
    ----------
    numero_borough : int

    """
    if (numero_borough > 7):
        raise Exception(f'Non ci sono {numero_borough} borough da analizzare. Puoi inserirne al massimo 7!')


def verifica_borough(borough):
    """
    Verifica per tutti i borough dati in input che il borough scelto faccia 
    parte della lista di borough disponibili.

    Parameters
    ----------
    borough : list of str

    """
    nome_borough = ['Bronx', 'Brooklyn', 'EWR', 'Manhattan', 'Queens', 'Staten Island', 'Unknown']
    for i in borough:
        if i not in nome_borough:
            raise Exception(f'{i} non è un nome di un borough valido')


def verifica_fascia_oraria(fascia_oraria):
    """
    Verifica che la tipologia di fascia oraria scelta sia disponibile.

    Parameters
    ----------
    fascia_oraria : int

    """
    fascia = [1, 3, 8, 12]
    if fascia_oraria not in fascia:
        raise Exception(f'La fascia oraria {fascia_oraria} non è valida. Scegliere solo tra 1, 3, 8 o 12')
        
