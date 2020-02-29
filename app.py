from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import json
from config import postgres_user, portgres_pw

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///disney.db'
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/", defaults={"json_enabled": ""})

@app.route("/api/<json_enabled>")
def api(json_enabled):
    engine = create_engine(f"postgresql://{postgres_user}:{portgres_pw}@localhost:5432/disney_db")
    output_df = pd.read_sql("""SELECT "characters"."Movie_Title", "characters"."Release_Date", "directors"."Director", "movies"."Genre", "movies"."MPAA_Rating", "movies"."Total_Gross", "movies"."Inflation_Adjusted_Gross"
        FROM characters
        JOIN directors ON "characters"."Movie_Title" = "directors"."Movie_Title"
        JOIN movies
        ON "characters"."Movie_Title" = "movies"."Movie_Title";""", engine)
    
    if json_enabled == "json":
        return output_df.to_json(orient='records')
    return render_template("api.html", data=output_df.to_json(orient='records'))

if __name__=="__main__":
    app.run(port=3333, debug=True)