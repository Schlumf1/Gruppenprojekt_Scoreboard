from database import save_score, load_scores

class Scores:
    def __init__(self, log = None):
        self.log = log

    def score_speichern(self, name, score):
        save_score(name, score)

        if self.log:
            self.log.schreiben(f"Neuer Score gespeichert: {name}, {score}")

    def score_laden(self):
        return load_scores()

    def scores_anzeigen(self):
        scores = self.score_laden()

        if not scores:
            print("Noch keine Scores gespeichert.")
            return

        print("\n--- Alle Scores ---")
        for i, (name, score) in enumerate(scores, start=1):
            print(f"{i}. {name}: {score}")

    def highes_scores_anzeigen(self):
        scores = self.score_laden()

        if not scores:
            print("Noch keine Scores gespeichert.")
            return

        name, score = max(scores, key=lambda x: x[1])
        print(f"Highscore: {name}: {score}")

        if self.log:
            self.log.schreiben("Highscore abgefragt.")

    def top_3_scores(self):
        scores = self.score_laden()

        if not scores:
            print("Noch keine Scores gespeichert.")
            return

        scores.sort(key=lambda x: x[1], reverse=True)

        print("\n--- Top 3 Scores ---")
        for i, (name, score) in enumerate(scores[:3], start=1):
            print(f"{i}. {name}: {score}")

    def durchschnitt_score(self):
        scores = self.score_laden()

        if not scores:
            print("Noch keine Scores gespeichert.")
            return

        durchschnitt = sum(score for _, score in scores) / len(scores)
        print(f"Durchschnittlicher Score: {durchschnitt:.2f}")

    def spieler_suchen(self, suchname):
        scores = self.score_laden()

        treffer = [score for name, score in scores if name.lower() == suchname.lower()]

        if not treffer:
            print(f"Keine Scores für {suchname} gefunden.")
            return

        print(f"\nScores von {suchname}:")
        for i, score in enumerate(treffer, start=1):
            print(f"{i}. {score}")

    def scores_sortiert(self):
        scores = self.score_laden()

        if not scores:
            print("Noch keine Scores gespeichert.")
            return

        scores.sort(key=lambda x: x[1], reverse=True)

        print("\n--- Scores sortiert ---")
        for i, (name, score) in enumerate(scores, start=1):
            print(f"{i}. {name}: {score}")