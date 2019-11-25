import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
###

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

###

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date
                        , Measurement.id
                        , Measurement.station
                        , Measurement.prcp
                        ).all()
    session.close()

    # Create a dictionary from the row data and append to a list
    #Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

    precipitationList = []

    for date, id, station, prcp in results:
        perc_dict = {}
        perc_dict[date] = prcp
        precipitationList.append(perc_dict)
    return jsonify(precipitationList)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    


if __name__ == '__main__':
    app.run(debug=True)
