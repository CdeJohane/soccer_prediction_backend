from flask import Flask, jsonify
from flask_cors import CORS
from controllers.matches import match_bp
from controllers.players import player_bp
from controllers.predict import predict_bp

app = Flask(__name__)
CORS(app)
app.config.from_object("config.DevelopmentConfig")
app.register_blueprint(match_bp)
app.register_blueprint(player_bp)
app.register_blueprint(predict_bp)
if __name__ == "__main__":
    app.run(debug=True)