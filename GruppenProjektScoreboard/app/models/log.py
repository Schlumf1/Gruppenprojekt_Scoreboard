class Log:
    def __init__(self, db):
        self.db = db

    def schreiben(self, text):
        self.db.save_log(text)