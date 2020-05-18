from flask import Flask
from flask import render_template
from flask import request
from config import config
import time
import sqlite3 as lite


def getLastRow():
    con = lite.connect(config['DB_NAME'])
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        print(result)
        return result

app = Flask(__name__)
@app.route("/")
def landing_page():
    last_row = getLastRow()
    if not (last_row):
        return "No data found in the database. Waiting for GPS."
    context = {'last_row' : last_row}
    return render_template('landing_page.html', **context)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
