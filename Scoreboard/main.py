from hauptmenue import Menue
from database import init_db

init_db()

menue = Menue()
menue.starten()