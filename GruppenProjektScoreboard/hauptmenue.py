from app import Scores
from app import Log

class Menue:
    def __init__(self, db):
        self.log = Log(db)
        self.scores = Scores(db, log=self.log)

    @staticmethod
    def menue_anzeigen():
        print("\n--- Scoreboard ---")
        print("1 - Neuen Score speichern")
        print("2 - Alle Scores anzeigen")
        print("3 - Highscore anzeigen")
        print("4 - Top 3 anzeigen")
        print("5 - Durchschnittlicher Score")
        print("6 - Suche nach Spielername")
        print("7 - Scores sortiert anzeigen")
        print("8 - Beenden")

    def score_eingeben(self):
        name = input("Name eingeben: ").strip()
        while not name:
            print("Bitte gib einen Namen ein.")
            name = input("Name eingeben: ")

        score = input("Score eingeben: ")
        while not (score.isdigit() and int(score) >= 0):
            print("Bitte gib eine gültige Zahl ein.")
            score = input("Score eingeben: ")

        self.scores.score_speichern(name, int(score))
        print("Score gespeichert.")

    def starten(self):
        try:
            while True:
                self.menue_anzeigen()
                auswahl = input("Auswahl: ").strip()

                try:
                    match auswahl:
                        case "1":
                            self.score_eingeben()
                        case "2":
                            self.scores.scores_anzeigen()
                        case "3":
                            self.scores.highscore_anzeigen()
                        case "4":
                            self.scores.top_3_scores()
                        case "5":
                            self.scores.durchschnitt_score()
                        case "6":
                            name = input("Spielername eingeben: ").strip()
                            self.scores.spieler_suchen(name)
                        case "7":
                            self.scores.scores_sortiert()
                        case "8":
                            print("Programm beendet.")
                            break
                        case _:
                            print("Ungültige Auswahl. Bitte 1-8 eingeben.")
                except Exception as e:
                    print(f"Fehler bei der Aktion: {e}")

        except KeyboardInterrupt:
            print("\nProgramm beendet.")