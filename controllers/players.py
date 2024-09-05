from flask import Blueprint, request, jsonify
import json
from flask_cors import cross_origin 
import pandas as pd
import sqlite3

# Get Connection
def get_db_connection():
    conn = sqlite3.connect('../database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Update Scores
def update_points(match_id, score_diff):
    # Tweak Scorediff to represent home or away win
    if score_diff > 0:
        score_diff = 1
    elif score_diff < 0:
        score_diff = 2
    conn = get_db_connection()
    # Lets Assume the scores were not added yet, for now
    # Get all the predictions associated with that match
    predictions = conn.execute(
        "SELECT * FROM prediction WHERE match_id = ?",
        (match_id)
    ).fetchall()
    for prediction in predictions:
        w_or_l = 0
        # Check If Prediction is correct
        if score_diff == prediction['home_or_away']:
            w_or_l = 1
            # Get Players record to update match statistic
            player_stat = conn.execute(
                "SELECT * FROM player WHERE id = ?",
                (prediction['player_id'])
            ).fetchone()
            player_stat["points"] = player_stat["points"] + 2
            conn.execute(
                "UPDATE player SET points = ? WHERE id = ?",
                (player_stat['points'], player_stat['id'])
            )
            conn.commit()
        # Update player_stats_updated
        conn.execute(
            "UPDATE prediction SET win_or_loss = ?, player_stats_updated = ? WHERE id = ?",
            (w_or_l, 1, prediction['id'])
        )
        conn.commit()
    conn.close()