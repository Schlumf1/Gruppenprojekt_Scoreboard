from hauptmenue import Menue
from app import Database

db = None

try:
    db = Database()
    menue = Menue(db)
    menue.starten()
except Exception as e:
    print(f"Unerwarteter Fehler {e}")
finally:
    if db:
        db.close()