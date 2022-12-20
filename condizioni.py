from verify_error import *
def definizione_anno(numero_anni):
    verifica_numero_anni(numero_anni)
    if numero_anni > 1:
        anno = input('Inserisci anni da analizzare (separati da spazi): ')
        anno = anno.split(' ')
        verifica_anno(anno)
        verifica_piu_anni(anno)
    else:
        anno = [input('Inserisci anno da analizzare: ')]
        verifica_anno(anno)
        verifica_piu_anni(anno)
    anno.sort()
    return anno

def definizione_mesi(condizione_mese):
    verifica_condizione_mese(condizione_mese)
    if condizione_mese == 'n':
        mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    else:
        numero_mesi = int(input('Quanti mesi vuoi analizzare? '))
        if numero_mesi > 1:
            mese = input('Inserisci mesi da analizzare (inserire indice_anno numeri separati da spazi, es: 01 02 ...): ')
            mese = mese.split(' ')
        else:
            mese = [input('Inserisci mese da analizzare (in numero, es: 01): ')]
    mese.sort()
    return mese

def definizione_borough(condizione_borough):
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
    if anno == '2022':
        if '10' in mese:
            mese.remove('10')
        if '11' in mese:
            mese.remove('11')
        if '12' in mese:
            mese.remove('12')
    return mese

