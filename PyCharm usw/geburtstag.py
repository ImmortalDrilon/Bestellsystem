from datetime import datetime

geburtsdatum = datetime.strptime("19.09.2022", "%d.%m.%Y")
heute = datetime.now()

alter = heute.year - geburtsdatum.year

if heute.month < geburtsdatum.month or (heute.month == geburtsdatum.month and heute.day < geburtsdatum.day):
    alter -=1

print(alter)