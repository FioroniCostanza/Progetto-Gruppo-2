import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def grafici(data,mese,anno,fascia_oraria):
    """
    Funzione che riceve in ingresso i risultati e li pre-elabora per poi 
    generare i grafici di nostro intresse.

    Parameters
    ----------
    data : dict/list/dataframe
        Il tipo di questo parametro varia a seconda del tipo di analisi che si 
        sta svolgendo. (annuale/mensile)
    m : str
        Una stringa contenente il mese a cui fa riferimento il parametro data
    anno : str
        Una stringa contenente l'anno a cui fa riferimento il parametro data
    fascia_oraria : int
        Rappresenta il tipo di fascia oraria che si sta utilizzando 

    Returns
    -------
    None.

    """
    if isinstance(data, dict): # La funzione isinstance controlla il tipo di data cosi da poter svolgere le operazioni preliminari corrette
        fasce = [] # Inizializzo una variabile b in cui salverò le fasce orarie utilizzate
        bor = np.array((list(data.keys()))) # la variabile bor contiene la lista dei borough analizzati
        fasce.append((list(data[bor[0]].keys()))) 
        fasce = np.array(fasce)
        ris = [] #in ris vengono salvati i risultati che verranno poi plottati
        for i in bor:
                ris.append((list(data[i].values())))
        ris = np.array(ris) 
        label = taglio_stringhe_fasce(fasce[0])
            
    elif isinstance(data, list):
        bor = np.array(data[0].columns)
        fasce = np.array((data[0].reset_index()['index']))
        ris = []
        for i in bor:
            ris.append((list(data[0].loc[:, i])))
        ris = np.array(ris)
        label = taglio_stringhe_fasce(fasce)
   
    elif isinstance(data, pd.DataFrame):
         data = data.dropna(axis=1)
         bor = np.array(list(data.columns))
         fasce = np.array(data.reset_index()['index'])
         ris = np.array(data[bor])
         ris = ris.T # operazione di traspozione, perchè in questo caso ris viene generato come una riga e non come colonna
         label = taglio_stringhe_fasce(fasce)
    
    if (len(bor) != 1): # Non svolgiamo l'analisi per fascia oraria se si sta analizzando un solo borough (avremmo dei barplot con una sola barra)
        if (len(label) < 7): # Per una questione di chiarezza dei grafici, svolgiamo questa analisi solo se il numero di fasce totali è 2 o 3
           barplot_per_fascia(bor,ris,label,mese,anno) #richiamiamo la funzione pieplot_per_fascia
            
    if (len(label)>7): # In tutti i casi in cui pieplot_per_fascia non viene richiamata, eseguiamo invece la funzione barplot, poichè tali grafici funzionano meglio con fasce da 1h o 3h
        barplot_per_zona(bor,ris,label,mese,anno,fascia_oraria)
        
    if (len(label) < 7):
        pieplot_per_zona(bor,ris,label,mese,anno,fascia_oraria)
     
       
     
def taglio_stringhe_fasce(fasce):
    '''
    Avendo, nel caso venga scelta una fascia oraria di 1h, ben 24 label per i nostri plot, si abbrevia 
    la stringa eliminando le parti superflue

    Parameters
    ----------
    fasce : nump array
      Contiene le fasce orarie che si stanno analizzando nel formato 'hh:mm - hh:mm', 
      la funzione restituisce le label nel formato 'hh - hh'

    Returns
    -------
    label : list
    
    '''
    label = []
    for i in range(len(fasce)):
        label.append((str(fasce[i].split(':')[0]) + ' -' + str(fasce[i].split(':')[1].split('-')[1])))
    return label
         
     
def barplot_per_zona(bor,ris,label,mese,anno,fascia_oraria):
    '''
    Funzione che genera i barplot

    Parameters
    ----------
    bor : numpy array
    
    ris : numpy array
    
    label : list of str
     
    mese : str
       
    anno : str
       
    fascia_oraria : int
       

    Returns
    -------
    None.

    '''
    if not os.path.exists('results/barplot_per_zona'):
        os.makedirs('results/barplot_per_zona')
        
    for i in range(len(bor)):
        fig, ax = plt.subplots(figsize=(8,5)) # Creo una nuova figura
        plt.bar(label,ris[i], width = 0.8) # Creo le barre
        titolo = 'Risultati - ' + bor[i] # Creo il titolo del grafico concatenando il Borough analizzato
        plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        ax.set_xticks(range(len(ris[i])))
        ax.set_xticklabels(label, rotation=45, fontsize = 6) # Inserisco le label sotto le sbarre, rotation serve a farle ruotate
        plt.xlabel('FASCE ORARIE')
        plt.ylabel('NUMERO DI PASSEGGERI')
        plt.subplots_adjust(wspace=115)
        plt.savefig(f'results/barplot_per_zona/bar_plot_{mese}_{anno}_fasce_da_{fascia_oraria}_{bor[i]}.png', dpi=300) 


def pieplot_per_zona(bor,ris,label,mese,anno,fascia_oraria):
    '''
    Funzione che genera un pieplot per ogni zona analizzata

    Parameters
    ----------
    bor : numpy array
       
    ris : numpy array
      
    label : list
       
    mese : str
       
    anno : str
      
    fascia_oraria : int
    

    Returns
    -------
    None.

    '''
    if not os.path.exists('results/piegraph_per_zona'):
        os.makedirs('results/piegraph_per_zona')
        
    for i in range(len(bor)):
        weights = [] # Contiene i valori degli spicchi
        for j in range(len(ris[i])):
            weights.append(ris[i][j])
        plt.figure(figsize=(8,5))
        plt.style.use('ggplot')
        titolo = 'Risultati - ' + bor[i]
        sottotitolo = 'Numero passeggeri: ' + str(sum(weights)) # Avendo fatto un pieplot percentuale, andiamo ad inserire in un sottotiolo il numero di passeggeri totali, cosi che sia possibile ottenere informazioni reali e non solo percentuali
        plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        plt.suptitle(sottotitolo, y=0.87, fontsize=10)
        plt.pie(weights, labels=label, wedgeprops={'linewidth': 2, 'edgecolor': 'black'},pctdistance=0.8, autopct='%.2f %%')
        plt.savefig(f"results/piegraph_per_zona/pie_graph_per_zona_{bor[i]}_fasce_da_{fascia_oraria}_{mese}_{anno}.png", dpi=300)
       
    
def barplot_per_fascia(bor,ris,label,mese,anno):
    '''
    Genera un barplot per ogni fascia.

    Parameters
    ----------
    bor : numpy array

    ris : numpy array

    label : list

    mese : str

    anno : str


    Returns
    -------
    None.

    '''
    if not os.path.exists('results/barplot_per_fascia'):
        os.makedirs('results/barplot_per_fascia')
        
    label2 = [] # Per questi plot le label sono i borough considerati
    if ('Total' in bor): # Non ci serrvono i valori totali per questi grafici per cui eliminiamo l'ultima riga dall'array ris
        last_row = ris.shape[0] - 1  # Indice dell'ultima riga
        ris = np.delete(ris, last_row, axis=0)
    if ('Total' in bor):
        for i in range(len(bor)-1):
            label2.append(str(bor[i]))
    else:
        for i in range(len(bor)):
            label2.append(str(bor[i]))
    for i in range(len(label)):
        weights = [] 
        for j in range(len(ris[:])):
                 weights.append(ris[j][i])
        plt.figure(figsize=(8,5))
        plt.style.use('ggplot')
        plt.bar(label2,weights, width = 0.8) # Creo le barre
        titolo = 'Risultati - ' + 'fascia: ' + str(label[i])
        sottotitolo = 'Numero passeggeri: ' + str(sum(weights))
        plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        plt.suptitle(sottotitolo, y=0.87, fontsize=10)
        plt.savefig(f"results/barplot_per_fascia/barplot_per_fascia_oraria_{label[i]}_{mese}_{anno}_{i}", dpi=300)

