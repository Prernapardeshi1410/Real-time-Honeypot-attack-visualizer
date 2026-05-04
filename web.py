from flask import Flask, render_template
import json
import os

app = Flask(__name__)

LOG_FILE = "logs.json"

@app.route("/")
def dashboard():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    logs.append(json.loads(line))
                except:
                    pass

    logs = logs[::-1]  # newest first
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
