from scores import Scores
from log import Log

class Menue:
    def __init__(self):
        self.log = Log()
        self.scores = Scores(log=self.log)

    def menue_anzeigen(self):
        print("\n--- Scoreboard ---")
        print("1 - Neuen Score speichern")
        print("2 - Alle Scores anzeigen")
        print("3 - Highscore anzeigen")
        print("4 - Top 3 anzeigen")
        print("5 - Durschschnittlicher Score")
        print("6 - Suche nach Spielername")
        print("7 - Scores sortiert anzeigen")
        print("8 - Beenden")

    def score_eingeben(self):
        while True:
            name = input("Name eingeben: ").strip()
            if name == "":
                print("Bitte gib einene Namen ein.")
            else:
                break

        while True:
            score_eingabe = input("Score eingeben: ")
            if not score_eingabe.isdigit():
                print("Bitte gib eine gültige Zahl ein.")
            else:
                score = int(score_eingabe)
                if score < 0:
                    print("Score darf nicht negativ sein.")
                else:
                    break

        self.scores.score_speichern(name, score)
        print("Score gespeichert.")

    def starten(self):
        try:
            while True:
                self.menue_anzeigen()
                auswahl = input("Auswahl: ")

                match auswahl:
                    case "1":
                        self.score_eingeben()
                    case "2":
                        self.scores.scores_anzeigen()
                    case "3":
                        self.scores.highes_scores_anzeigen()
                    case "4":
                        self.scores.top_3_scores()
                    case "5":
                        self.scores.durchschnitt_score()
                    case "6":
                        name = input("Spielername eingeben: ")
                        self.scores.spieler_suchen(name)
                    case "7":
                        self.scores.scores_sortiert()
                    case "8":
                        print("Programm beendet.")
                        break
                    case _:
                        print("Ungültige Auswahl. Bitte 1-4 eingeben.")
        except KeyboardInterrupt:
            print("Programm beendet.")