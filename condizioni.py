from verifyerror import *

def definizione_mesi(condizione_mese,anno):
    if condizione_mese == 'n' and anno != '2022':
        mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    else:
        numero_mesi = int(input('Quanti mesi vuoi analizzare? '))
        error_numero_mesi = verifica_numero_mesi(anno,numero_mesi)
        if numero_mesi > 1:
            mese = input('Inserisci mesi da analizzare (inserire i numeri separati da spazi, es: 01 02 ...): ')
            mese = mese.split(' ')
            error_piu_mesi = verifica_piu_mesi(mese)
        else:
            mese = [input('Inserisci mese da analizzare (in numero, es: 01): ')]
            error_unico_mese = verifica_unico_mese(mese)
    mese.sort()
    return mese

def definizione_borough(condizione_borough):
    if condizione_borough == 's':
        numero_borough = int(input('Quanti borough vuoi analizzare? '))
        error_numero_borough = verifica_numero_borough(numero_borough)
        if numero_borough > 1:
            borough = input('Inserisci il nome dei borough (separati da virgole): ')
            borough = borough.split(',')
            error_borough = verifica_borough(borough)
        else:
            borough = [input('Inserisci il borough da analizzare: ')]
            error_borough = verifica_borough(borough)
    else:
        borough = None
    return borough

def verifica_condizione_su_2022(anno,mese):
    if anno == '2022':
        if '10' in mese:
            mese.remove('10')
        if '11' in mese:
            mese.remove('11')
        if '12' in mese:
            mese.remove('12')
    return mese

