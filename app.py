from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Background App Setup
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Poridhi_2 App!"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP"}), 200

# Database Connection
@app.route('/db_ping', methods=['GET'])
def db_ping():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "123456"),
            database=os.getenv("MYSQL_DATABASE", "test_db")
        )
        if connection.is_connected():
            return jsonify({"db_status": "Connection Successful"}), 200
    except Exception as e:
        return jsonify({"db_status": "Connection Failed", "error": str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
