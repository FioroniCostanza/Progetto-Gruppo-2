def verifica_numero_anni(numero_anni):
    if (numero_anni > 13):
        raise Exception(f'Al momento non sono disponibili {numero_anni} anni. Puoi inserirne al massimo 13!')


def verifica_piu_anni(anno):
    if len(anno) < 2:
        raise Exception(f'Hai inserito solo il {anno}. Inserisci più anni!')


def verifica_unico_anno(anno):
    if len(anno[0]) > 5:
        raise Exception(f' Hai inserito {anno} come anni da analizzare. Inserisci un solo anno!')


def verifica_anno(anno):
    for i in range(len(anno)):
        if int(anno[i]) not in range(2009, 2023):
            raise Exception(f'Anno {anno[i]} non valido, scegliere un anno dal 2009 al 2022')


def verifica_condizione_mese(condizione_mese):
    if (condizione_mese != 's') and (condizione_mese != 'n'):
        raise Exception(f'Opzione {condizione_mese} non disponibile. Scegliere solo tra s o n!')


def verifica_numero_mesi(anno, numero_mesi):
    for i in range(len(anno)):
        if (int(anno[i]) == 2022) and (numero_mesi > 9):
            raise Exception(f'Per il 2022 non sono disponibili {numero_mesi} mesi. Sceglierne massimo 9.')


def verifica_piu_mesi(mese):
    if len(mese) < 2:
        raise Exception(f'Hai inserito solo {mese}. Inserisci più mesi!')


def verifica_unico_mese(mese):
    if len(mese[0]) > 3:
        raise Exception(f' Hai inserito {mese} come mesi da analizzare. Inserisci un solo mese!')


def verifica_condizione_borough(condizione_borough):
    if (condizione_borough != 's') and (condizione_borough != 'n'):
        raise Exception(f'Opzione {condizione_borough} non disponibile. Scegliere solo tra s o n!')


def verifica_numero_borough(numero_borough):
    if (numero_borough > 7):
        raise Exception(f'Non ci sono {numero_borough} borough da analizzare. Puoi inserirne al massimo 7!')


def verifica_borough(borough):
    nome_borough = ['Bronx', 'Brooklyn', 'EWR', 'Manhattan', 'Queens', 'Staten Island', 'Unknown']
    for i in range(len(borough)):
        if borough[i] not in nome_borough:
            raise Exception(f'{borough[i]} non è un nome di un borough valido')


def verifica_fascia_oraria(fascia_oraria):
    fascia = [1, 3, 8, 12]
    if fascia_oraria not in fascia:
        raise Exception(f'La fascia oraria {fascia_oraria} non è valida. Scegliere solo tra 1, 3, 8 o 12')