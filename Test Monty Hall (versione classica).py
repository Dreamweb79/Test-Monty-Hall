"""
Problema di Monty Hall.

- Dietro ciascuna di tre porte c'è un'automobile o una capra (due capre, un'automobile in tutto);
  la probabilità che l'automobile si trovi dietro una data porta è identica per tutte le porte;
- Il giocatore sceglie una delle porte; il suo contenuto non è rivelato;
- Il conduttore sa ciò che si nasconde dietro ciascuna porta;
- Il conduttore deve aprire una delle porte non selezionate, e deve offrire al giocatore la possibilità di cambiare la sua scelta;
- Il conduttore aprirà sempre una porta che nasconde una capra;
  Cioè, se il giocatore ha scelto una porta che nasconde una capra, il conduttore aprirà la porta che nasconde l'altra capra;
  Se invece il giocatore ha scelto la porta che nasconde l'automobile, il conduttore sceglie a caso una delle due porte rimanenti;
- Il conduttore offre al giocatore la possibilità di reclamare ciò che si trova dietro la porta che ha scelto originalmente,
  o di cambiare, reclamando ciò che si trova dietro la porta rimasta.
- Le probabilità di vittoria aumentano per il giocatore se cambia la propria scelta?

Spiegazione:
Supponiamo che l'auto sia nella porta B.
Scelgo la porta A, il conduttore apre la C, cambio con B: VINCO
Scelgo la porta B, il conduttore apre la A o la C, cambio con la rispettiva C o A: PERDO
Scelgo la porta C, il conduttore apre la A, cambio con B: VINCO

Spiegazione alternativa:
Supponiamo ci siano 100 porte, in una sola c'è l'auto (ho 1 possibilità su 100 di vincere).
Scelgo una porta, dopodichè il conduttore apre 98 delle altre porte con la capra e ne lascia chiusa solo una.
È più probabile che vinca con la scelta iniziale (1 probabilità su cento) o cambiando la porta?
"""


import random

while True:
    try:
        iterazioni = int(input("Inserisci n. di iterazioni (max 100000): "))
        if 0 < iterazioni <= 100000:
            
            n_vittorie_mantenendo_porta = 0
            n_vittorie_cambiando_porta = 0
            
            for n in range(0, iterazioni):
                
                contenuto_porte = ["auto", "capra_1", "capra_2"]

                # Il concorrente sceglie casualmente una porta.
                scelta_iniziale = random.choice(contenuto_porte)
                
                # Il conduttore sceglie una porta da aprire tra le 2 non scelte dal concorrente.
                # Da notare che è ininfluente che la scelta sia consapevole o casuale, perchè può
                # solo essere una porta con una capra.
                scelta_conduttore = random.choice([x for x in contenuto_porte if x != scelta_iniziale and x != "auto"])

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
