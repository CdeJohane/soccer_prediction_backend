from flask import Blueprint, request, jsonify
import json
from flask_cors import cross_origin 
import pandas as pd
import sqlite3
from players import update_points

# Get Connection
def get_db_connection():
    conn = sqlite3.connect('../database.db')
    conn.row_factory = sqlite3.Row
    return conn


predict_bp = Blueprint("predict", __name__)
@predict_bp.route("/add_prediction", method =['POST'])
@cross_origin
def add_prediction(player_id, match_id, home_or_away):
    conn = get_db_connection()
    # Check if prediction is added
    check = conn.execute(
        "SELECT * FROM prediction WHERE player_id = ? AND match_id = ?",
        (player_id, match_id)
    ).fetchall()
    # If none, add entry and commit
    if not check:
        conn.execute(
            "INSERT INTO prediction (player_id, match_id, home_or_away, win_or_lose, player_stats_updated) VALUES = (?, ?, ?, ?, ?)",
            (player_id, match_id, -1, -1, 0)
        )
        conn.commit()
    elif check['home_or_away'] != home_or_away:
        conn.execute(
            "UPDATE prediction SET home_or_away = ? WHERE player_id = ? AND match_id = ?",
            (home_or_away, player_id, match_id)
        )
        conn.commit()
    conn.close()
    return jsonify({"success": True})
