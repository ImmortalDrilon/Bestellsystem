from datetime import datetime

def tage_ohne_schaltjahre(tag, monat, jahr):
    heute_tag = 17
    heute_monat = 9
    heute_jahr = 2024

    # Berechne die Tage im aktuellen Jahr bis zum heutigen Datum
    tage_im_jahr_bis_heute = (datetime(heute_jahr, heute_monat, heute_tag) - datetime(heute_jahr, 1, 1)).days

    # Berechne die Tage im Geburtsjahr ab dem Geburtsdatum
    tage_im_geburtsjahr_ab_geburt = (datetime(jahr, 12, 31) - datetime(jahr, monat, tag)).days + 1

    # Berechne die Tage in den Jahren dazwischen
    tage_in_jahren = (heute_jahr - jahr - 1) * 365

    # Gesamtanzahl der Tage
    gesamt_tage = tage_im_jahr_bis_heute + tage_im_geburtsjahr_ab_geburt + tage_in_jahren

    return gesamt_tage

# Beispiel: Geburtsdatum 29. Februar 2004
geburtsdatum_tag = 29
geburtsdatum_monat = 2
geburtsdatum_jahr = 2004

differenz = tage_ohne_schaltjahre(geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr)

print(f"Die Differenz in Tagen vom heutigen Datum bis zum 29.02.2004 beträgt {differenz} Tage.")