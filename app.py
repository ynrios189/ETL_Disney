from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import json
from config import postgres_user, portgres_pw

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html", message="Say hello to our API")

@app.route("/api/", defaults={"json_enabled": ""})
@app.route("/api/<json_enabled>")
def api(json_enabled):
    engine = create_engine(f"postgresql://{postgres_user}:{portgres_pw}@localhost/disney_db")
    output_df = pd.read_sql("SELECT * FROM characters.'Movie_Titles'", engine)

    if json_enabled == "json":
        return output_df.to_json(orient='records')

    return render_template("api.html", data=output_df.to_json(orient='records'))

if __name__=="__main__":
    app.run(port=3333, debug=True)