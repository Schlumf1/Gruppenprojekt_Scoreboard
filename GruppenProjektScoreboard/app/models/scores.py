class Scores:
    def __init__(self, db, log = None):
        self.db = db
        self.log = log

    def score_speichern(self, name, score):
        if self.db.save_score(name, score):
            if self.log:
                self.log.schreiben(f"Neuer Score gespeichert: {name}, {score}")

    def scores_anzeigen(self):
        rows = self.db.load_scores()

        if not rows:
            print("Noch keine Scores gespeichert.")
            return

        print("\n--- Alle Scores ---")
        for i, (name, score) in enumerate(rows, start=1):
            print(f"{i}. {name}: {score}")

    def highscore_anzeigen(self):
        row = self.db.load_high_score()

        if not row:
            print("Noch keine Scores gespeichert.")
            return

        name, score = row
        print(f"Highscore: {name}: {score}")

        if self.log:
            self.log.schreiben("Highscore abgefragt.")

    def top_3_scores(self):
        rows = self.db.load_top_3_scores()

        if not rows:
            print("Noch keine Scores gespeichert.")
            return

        print("\n--- Top 3 Scores ---")
        for i, (name, score) in enumerate(rows, start=1):
            print(f"{i}. {name}: {score}")

    def durchschnitt_score(self):
        avg = self.db.load_average_score()

        if avg is None:
            print("Noch keine Scores gespeichert.")
            return

        print(f"Durchschnittlicher Score: {avg:.2f}")

    def spieler_suchen(self, name):
        rows = self.db.load_scores_by_player(name)

        if not rows:
            print(f"Keine Scores für {name} gefunden.")
            return

        print(f"\nScores von {name}:")
        for i, (_, score) in enumerate(rows, start=1):
            print(f"{i}. {score}")

    def scores_sortiert(self):
        rows = self.db.load_scores_sorted()

        if not rows:
            print("Noch keine Scores gespeichert.")
            return

        print("\n--- Scores sortiert ---")
        for i, (name, score) in enumerate(rows, start=1):
            print(f"{i}. {name}: {score}")