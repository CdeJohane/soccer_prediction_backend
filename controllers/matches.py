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

match_bp = Blueprint("match", __name__)
@match_bp.route('/insert_match', methods = ['POST'])
@cross_origin()
def insert_match(home, away):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO matches (home_team_code, away_team_code, complete, home_team_score, away_team_score, winner, scores_updated) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (home, away, 0, 0, 0, -1, -1, 0)
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@match_bp.route("/update_match",methods = ['POST'])
def update_match(match_id, home_score, away_score, winner):
    conn = get_db_connection()
    conn.execute(
        'UPDATE matches SET complete = ?, home_team_score = ?, away_team_score = ?, winner = ?, scores_updated = ?'
        'WHERE id = ?',
        (1, home_score, away_score,winner, 0)
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True})
