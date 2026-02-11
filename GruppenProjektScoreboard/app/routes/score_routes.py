from flask import Blueprint, render_template, request, redirect, url_for
from app.models.database import Database
from app.models.scores import Scores

score_bp = Blueprint('score', __name__)

db = Database()
scores = Scores(db)

@score_bp.route("/")
def index():
    return render_template("pages/index.html")

@score_bp.route("/add", methods=["GET", "POST"])
def add_score():
    if request.method == "POST":
        name = request.form["name"]
        score = int(request.form["score"])
        scores.score_speichern(name, score)
        return redirect(url_for("score.show_scores"))

    return render_template("pages/add_score.html")

@score_bp.route("/scores")
def show_scores():
    rows = db.load_scores_sorted()
    return render_template("pages/scores.html", scores=rows)

@score_bp.route("/scores_sorted")
def scores_sorted():
    rows = db.load_scores_sorted()
    return render_template("pages/scores.html", scores=rows, title="Scores sorted")

@score_bp.route("/highscore")
def highscore():
    row = db.load_high_score()
    return render_template("pages/highscore.html", score=row)

@score_bp.route("/top3")
def top3():
    rows = db.load_top_3_scores()
    return render_template("pages/scores.html", scores=rows, title="Top 3 scores")

@score_bp.route("/average")
def average():
    avg = db.load_average_score()
    return render_template("pages/average.html", average=avg)

@score_bp.route("/search", methods=["GET", "POST"])
def search():
    results = None
    name = ""
    if request.method == "POST":
        name = request.form["name"]
        results = db.load_scores_by_player(name)
    return render_template("pages/search.html", results=results, name=name)