from datetime import datetime

def tage_bis_geburtstag(geburtstag):
    heute = datetime.now()
    geburtstag_dieses_jahr = datetime(heute.year, geburtstag.month, geburtstag.day)
    
    if geburtstag_dieses_jahr < heute:
        geburtstag_dieses_jahr = datetime(heute.year + 1, geburtstag.month, geburtstag.day)
    
    tage_bis = (geburtstag_dieses_jahr - heute).days + 1
    return tage_bis

# Beispiel: Geburtstag am 30. Januar
geburtstag = datetime(2005, 1, 30)
print(f"Tage bis zum nächsten Geburtstag: {tage_bis_geburtstag(geburtstag)}")

