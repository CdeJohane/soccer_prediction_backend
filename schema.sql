DROP TABLE IF EXISTS player;

CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    player_code TEXT NOT NULL,
    points INTEGER NOT NULL
);

DROP TABLE IF EXISTS team;

CREATE TABLE team (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    team_code TEXT NOT NULL
);

DROP TABLE IF EXISTS matches;

CREATE TABLE matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_team_code TEXT NOT NULL,
    away_team_code TEXT NOT NULL,
    complete INTEGER NOT NULL,
    home_team_score INTEGER,
    away_team_score INTEGER,
    winner TEXT NOT NULL,
    scores_updated INTEGER NOT NULL
);

DROP TABLE IF EXISTS prediction;

CREATE TABLE prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    match_id INTEGER NOT NULL,
    home_or_away INTEGER NOT NULL,
    win_or_loss INTEGER NOT NULL,
    player_stats_updated INTEGER NOT NULL
);
