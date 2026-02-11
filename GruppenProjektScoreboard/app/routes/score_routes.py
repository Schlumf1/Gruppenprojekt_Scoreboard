from flask import Blueprint, render_template, request, redirect, url_for
from app.models.database import Database
from app.models.scores import Scores

score_bp = Blueprint('score', __name__)

db = Database()
scores = Scores(db)

@score_bp.route("/")
def index():
    return render_template("pages/index.html")

@score_bp.route("/scores")
def show_scores():
    rows = db.load_scores_sorted()
    return render_template("pages/scores.html", scores=rows)

@score_bp.route("/add", methods=["GET", "POST"])
def add_score():
    if request.method == "POST":
        name = request.form["name"]
        score = int(request.form["score"])
        scores.score_speichern(name, score)
        return redirect(url_for("score.show_scores"))

    return render_template("pages/add_score.html")