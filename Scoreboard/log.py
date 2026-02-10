from database import save_log

class Log:
    def schreiben(self, text):
        save_log(text)