# Progetto-Gruppo-2

In questo progetto viene svolta un’analisi dei taxi a New York. In particolare, vengono analizzati quanti passeggeri effettuano una corsa in taxi in determinate fasce orarie, andando a suddividerli per borough.

Prima di effettuare una ricerca è necessario:
- Fare il download dei file di Yellow Taxi Trip Records, disponibili su https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Fare il download del file taxi_zone_lookup.csv disponibile sempre su https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page 

Il programma garantisce molta libertà all’utente che può modellare la ricerca inserendo i seguenti input:
- Path della cartella contenente i dataset appena scaricati, così da non obbligare l’utente a crearsi una cartella all’interno del progetto
- N° di anni su cui effettuare la ricerca
- Anno/i scelto/i (N.B. divisi da uno spazio)
- Possibilità di selezionare mesi specifici
- N° di mesi su cui effettuare la ricerca
- Mese/i scelto/i (N.B. divisi da uno spazio)
- Possibilità di selezionare borough specifici
- N° di borough su cui effettuare la ricerca
- Borough scelti (N.B. divisi da una virgola e non da uno spazio)
- Possibilità di selezionare una fascia oraria (N.B. scegliendo tra i valori 1-3-8-12)

Infine, gli output prodotti vengono salvati in una cartella denominata Results che viene generata nella directory in cui è presente il codice.

A seconda degli input, il programma restituisce i seguenti file csv:
- Un file con i dati relativi al totale dei passeggeri suddivisi per singolo mese
- Un file con i dati relativi al totale dei passeggeri aggregati per tutti i mesi
- Un file con i dati relativi al totale dei passeggeri aggregati per tutti gli anni

Inoltre, il programma restituisce i seguenti file png:
- Un grafico a barre per ogni zona che riporta il n° di passeggeri per ogni fascia oraria (se la fascia oraria scelta è 1 o 3)
- Un grafico a barre per ogni fascia oraria che riporta il n° di passeggeri per ogni zona(se la fascia oraria scelta è 8 o 12)
- Un grafico a torta per ogni zona che riporta la percentuale di passeggeri per ogni fascia oraria (se la fascia oraria scelta è 8 o 12)

Esempio di una ricerca:

Input:
![image](https://user-images.githubusercontent.com/117634064/209109218-ba54bab6-4aa6-4110-9031-d3d5a1639d56.png)

Output:
![image](https://user-images.githubusercontent.com/117634064/209109334-ef196c28-ab11-400c-a326-29e20b671965.png)

