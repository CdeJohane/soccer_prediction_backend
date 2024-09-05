import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
'''
cur = connection.cursor()

cur.execute("INSERT INTO player (player_name, player_code, points) VALUES (?, ?, ?)",
            ('Junior Johane', 'JUN', '0')
            )

cur.execute("INSERT INTO player (player_name, player_code, points) VALUES (?, ?, ?)",
            ('Dalitso Da Grey', 'DAL', '0')
            )

connection.commit()
connection.close()
'''

# Insert Player Names
player_names = ["Juju", 
                "Antz", 
                "Jay",
                "Daniel M",
                "Dalitso",
                "Thata S",
                "King M",
                "Naeem",
                "Ngoma",
                "Queen",
                "Israel L"
                ]
player_name_codes = [
    "JUN",
    "ANT",
    "JAY",
    "DAN",
    "DAL",
    "THA",
    "KIN",
    "NAE",
    "NGO",
    "QUE",
    "ISR"
]

cur = connection.cursor()
for player in range(0, len(player_names)):
    cur.execute("INSERT INTO player (player_name, player_code, points) VALUES (?, ?, ?)",
        (player_names[player], player_name_codes[player], 0)
    )

# Insert Teams
teams = [
    ("BOU", "AFC Bournemouth"),
    ("ARS", "Arsenal"),
    ("AVL", "Aston Villa"),
    ("BRE", "Brentford"),
    ("BHA", "Brighton & Hove Albion"),
    ("CHE", "Chelsea"),
    ("CRY", "Crystal Palace"),
    ("EVE", "Everton"),
    ("FUL", "Fulham"),
    ("IPS", "Ipswich Town"),
    ("LEI", "Leicester City"),
    ("LIV", "Liverpool"),
    ("MCI", "Manchester City"),
    ("MUN", "Manchester United"),
    ("NEW", "Newcastle United"),
    ("NFO", "Nottingham Forest"),
    ("SOU", "Southampton"),
    ("TOT", "Tottenham Hotspur"),
    ("WHU", "West Ham United"),
    ("WOL", "Wolverhampton Wanderers"),
]

cur = connection.cursor()

for key, value in teams:
    cur.execute("INSERT INTO team (team_name, team_code) VALUES (?, ?)",
            (value, key)
            )
connection.commit()
connection.close()

