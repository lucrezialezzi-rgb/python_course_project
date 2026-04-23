import math


class Studente:
    def __init__(self, nome: str, cognome: str, eta: int, matricola: str):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    # DEFINIZIONE FUNZIONE PRESENTATI
    def presentati(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}."

    # DEFINIZIONE AGGIUNGI_VOTO
    def aggiungi_voto(self, voto: int):
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(
                f"Voto {voto} registrato correttamente per {self.nome} {self.cognome}."
            )
        elif voto < 18:
            print(f"Esame non superato: il voto {voto} è insufficiente.")
        else:
            print("Errore: un voto non può essere superiore a 30.")

    # DEFINIZIONE CALCOLA_MEDIA
    def calcola_media(self):
        if len(self.voti) == 0:
            return 0
        return round(sum(self.voti) / len(self.voti), 0)

    # DEFINIZIONE FUNZIONE STUDIA
    def studia(self, ore: int):
        print(f"{self.nome} ha studiato per {ore} ore.")


# CREAZIONE DELLE ISTANZE
studente1 = Studente("Mario", "Rossi", 20, "A123")
studente2 = Studente("Giulia", "Bianchi", 22, "B456")

# APPLICAZIONE DELLE FUNZIONI A STUDENTE 1
print(studente1.presentati())
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
studente1.aggiungi_voto(21)
studente1.studia(4)
print(f"Media di {studente1.nome}: {studente1.calcola_media()}")

print("-" * 30)

# APPLICAZIONE DELLE FUNZIONI A STUDNETE 2
print(studente2.presentati())
studente2.aggiungi_voto(24)
studente2.studia(2)
print(f"Media di {studente2.nome}: {studente2.calcola_media()}")
