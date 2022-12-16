def definizione_mesi(condizione_mese,anno):
    if condizione_mese == 'n' and anno != '2022':
        mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    elif condizione_mese == 'n' and anno == '2022':
        mese = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    else:
        numero_mesi = int(input('Quanti mesi vuoi analizzare? '))
        if numero_mesi > 1:
            mese = input('Inserisci mesi da analizzare (inserire i numeri separati da spazi, es: 01 02 ...): ')
            mese = mese.split(' ')
        else:
            mese = [input('Inserisci mese da analizzare (in numero, es: 01): ')]
    return mese

def definizione_borough(condizione_borough):
    if condizione_borough == 's':
        numero_borough = int(input('Quanti borough vuoi analizzare? '))
        if numero_borough > 1:
            borough = input('Inserisci il nome dei borough (separati da virgole): ')
            borough = borough.split(',')
        else:
            borough = [input('Inserisci il borough da analizzare: ')]
    else:
        borough = None
    return borough

