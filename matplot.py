import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from postprocessing import *
from condizioni import *

def grafici(data,m,anno,fascia_oraria):
    if isinstance(data, dict):
        t = 1
        b = []
        a = np.array((list(data.keys())))
        b.append((list(data[a[0]].keys()))) 
        b = np.array(b)
        c = []
        for k in a:
                c.append((list(data[k].values())))
        c = np.array(c)    
        label = []
        for i in range(len(b[0])):
            label.append((str(b[0][i].split(':')[0]) + ' -' + str(b[0][i].split(':')[1].split('-')[1])))
    elif isinstance(data, list):
        t = 2
        a = np.array(data[0].columns)
        b = np.array(data[0].reset_index()['index'])
        c = []
        for k in a:
            c.append((list(data[0].loc[:, k])))
        c = np.array(c)
        label = []
        for i in range(len(b)):
            label.append((str(b[i].split(':')[0]) + ' -' + str(b[i].split(':')[1].split('-')[1])))
    elif isinstance(data, pd.DataFrame):
         t = 3
         data = data.dropna(axis=1)
         a = np.array(list(data.columns))
         b = np.array(data.reset_index()['index'])
         c = np.array(data[a])
         c = c.T
         label = []
         for i in range(len(b)):
             label.append((str(b[i].split(':')[0]) + ' -' + str(b[i].split(':')[1].split('-')[1])))
    if (len(a) != 1):
        if (len(label) < 7):
            pieplot_per_fascia(a,c,label,m,anno)
    if len(a) == 8:
        if (len(label)>7):
            barplot(a,b,c,label,m,anno,fascia_oraria,t)
    if (len(label) < 7):
        pieplot_per_zona(a,c,label,m,anno,fascia_oraria)
        
def barplot(a,b,c,label,m,anno,fascia_oraria,t):
    for i in range(len(a)):
        fig, ax = plt.subplots(figsize=(8,5))
        if t==1:
            bars = plt.bar(b[0],c[i], width = 0.8)
        else:
            bars = plt.bar(b,c[i], width = 0.8)
        titolo = 'Risultati - ' + a[i]
        plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        ax.set_xticks(range(len(c[i])))
        ax.set_xticklabels(label, rotation=45, fontsize = 6)
        plt.xlabel('FASCE ORARIE')
        plt.ylabel('NUMERO DI PASSEGGERI')
        plt.subplots_adjust(wspace=115)
        plt.savefig(f'results/barplot/bar_plot_{m}_{anno}_fasce_da_{fascia_oraria}_{a[i]}.png', dpi=300)


def pieplot_per_zona(a,c,label,m,anno,fascia_oraria):
    for i in range(len(a)):
        weights = []
        for j in range(len(c[i])):
            weights.append(c[i][j])
        plt.figure(figsize=(8,5))
        plt.style.use('ggplot')
        titolo = 'Risultati - ' + a[i]
        plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        plt.pie(weights, labels=label, wedgeprops={'linewidth': 2, 'edgecolor': 'black'},pctdistance=0.8, autopct='%.2f %%')
        plt.savefig(f"results/piegraph_per_zona/pie_graph_per_zona_{a[i]}_fasce_da_{fascia_oraria}_{m}_{anno}.png", dpi=300)
       


def pieplot_per_fascia(a,c,label,m,anno):
    label2 = []
    if ('Total' in a):
        for i in range(len(a)-1):
            label2.append(str(a[i]))
    else:
        for i in range(len(a)):
            label2.append(str(a[i]))
    for i in range(len(label)):
        weights = []
        if ('Total' in a):
            for j in range(len(c[:])-1):
                weights.append(c[j][i])
            plt.figure(figsize=(8,5))
            plt.style.use('ggplot')
            plt.pie(weights, labels = label2 ,pctdistance=0.8, autopct='%.2f %%',wedgeprops={'linewidth': 2, 'edgecolor': 'black'})
            titolo = 'Risultati - ' + 'fascia: ' + str(label[i])
            plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
            plt.savefig(f"results/piegraph_per_fascia/pie_graph_per_fascia_oraria_{label[i]}_{m}_{anno}_{i}", dpi=300)
        else:
            for j in range(len(c[:])):
                weights.append(c[j][i])
            plt.figure(figsize=(8,5))
            plt.style.use('ggplot')
            plt.pie(weights, labels = label2 ,pctdistance=0.8, autopct='%.2f %%',wedgeprops={'linewidth': 2, 'edgecolor': 'black'})
            titolo = 'Risultati - ' + 'fascia: ' + str(label[i])
            plt.title(titolo, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
            plt.savefig(f"results/piegraph_per_fascia/pie_graph_per_fascia_oraria_{label[i]}_{m}_{anno}_{i}", dpi=300)
        

