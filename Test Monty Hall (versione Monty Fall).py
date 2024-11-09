"""
Versione "Monty Fall" del problema di Monty Hall.

Il conduttore non sa cosa ci sia dietro le porte.
Dopo la scelta del concorrente, il conduttore apre una delle due porte rimaste.
Poiché non sa cosa c'è dietro, con probabilità 1/3 trova l'auto e il gioco finisce.
Con probabilità 2/3 trova invece la capra e può chiedere al concorrente se vuole effettuare il cambio con la porta rimasta chiusa.
In questo caso accettare lo scambio non fa aumentare al concorrente la sua probabilità di vincere che a questo punto è di 1/2
qualunque sia la sua decisione

È importante notare che il conduttore ha la possibilità di trovare la porta con l'auto, per quanto ai fini del problema sia
specificato che la scelta casuale ricade ipoteticamente sempre in una porta con la capra.
Questa è l'unica differenza rispetto al classico problema di Monty Hall (dove invece la porta con l'auto non viene considerata),
ed è ciò che influenza le successive probabilità per il concorrente.
"""


import random

while True:
    try:
        iterazioni = int(input("Inserisci n. di iterazioni (max 100000): "))
        if 0 < iterazioni <= 100000:
            
            n_vittorie_mantenendo_porta = 0
            n_vittorie_cambiando_porta = 0

            n = 0
            while n < iterazioni:
                
                contenuto_porte = ["auto", "capra_1", "capra_2"]

                # Il concorrente sceglie casualmente una porta.
                scelta_iniziale = random.choice(contenuto_porte)
                
                # Il conduttore sceglie una porta a caso da aprire tra le 2 non scelte dal concorrente.
                scelta_conduttore = random.choice([x for x in contenuto_porte if x != scelta_iniziale])

                # Se la porta scelta dal conduttore è quella in cui c'è l'auto, l'iterazione non viene
                # conteggiata e la scelta viene ripetuta.
                if scelta_conduttore == "auto":
                    continue
                else:
                    n += 1

                    # Rimuoviamo la porta scelta dal conduttore.
                    contenuto_porte.remove(scelta_conduttore)

                    # Assegnazione index alle due porte rimaste.
                    index_porta_scelta_inizialmente = contenuto_porte.index(scelta_iniziale)
                    index_porta_rimanente = 0 if index_porta_scelta_inizialmente else 1
                    contenuto_porta_rimanente = contenuto_porte[index_porta_rimanente]

                    # Vittoria se sulla porta scelta inizialmente troviamo l'auto.
                    if scelta_iniziale == "auto":
                        n_vittorie_mantenendo_porta += 1                 

                    # Vittoria se cambiando porta troviamo l'auto.
                    if contenuto_porta_rimanente == "auto":
                        n_vittorie_cambiando_porta += 1
            
            print(f"Vittorie tenendo la stessa porta: {n_vittorie_mantenendo_porta} ({round((n_vittorie_mantenendo_porta * 100) / iterazioni, 2)} %)")
            print(f"Vittorie cambiando la porta:\t  {n_vittorie_cambiando_porta} ({round((n_vittorie_cambiando_porta * 100) / iterazioni, 2)} %)\n")
            print("-------------------------------------------------")            
            continue        

    except(ValueError):
        continue
