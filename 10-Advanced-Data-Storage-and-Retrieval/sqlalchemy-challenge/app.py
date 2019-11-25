import numpy as np
import datetime as dt
from datetime import date
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
###

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
    return (f"Welcome to the  Climate App!<br/> <br/>"
    f"Available Routes:<br/><br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/startdate<br/>"
    f"/api/v1.0/startdate/enddate"

    )

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
    results = session.query(Station.id
                        , Station.station
                        , Station.name
                        , Station.latitude
                        ,Station.longitude
                        ,Station.elevation
                        ).all()
    session.close()
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    ### Calculating dates
    LatestDate=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    LatestDate=datetime.strptime(LatestDate[0], '%Y-%m-%d')
    yr_ago = LatestDate - dt.timedelta(days=365)

    ### Querying for data of last 12 months

    results = session.query(Measurement.date
                            ,Measurement.tobs
                       ).filter(Measurement.date >= yr_ago).all()
    session.close()
    return jsonify(results)
    
     
@app.route("/api/v1.0/<start>")
  
def start(start):
        session = Session(engine)
        startDate=datetime.strptime(start, '%Y-%m-%d')
        #endDate=datetime.strptime("2016-02-20", '%Y-%m-%d')

        results = session.query(Measurement.date,func.min(Measurement.tobs).label("Min Temp")
         ,func.avg(Measurement.tobs).label("Avg Temp")
         ,func.max(Measurement.tobs).label("Max Temp")).group_by(Measurement.date).filter(Measurement.date >= start).all()
                        
        session.close()
        return jsonify(results)


     
@app.route("/api/v1.0/<start>/<end>")
  
def date(start,end):
        session = Session(engine)
        startDate=datetime.strptime(start, '%Y-%m-%d')
        endDate=datetime.strptime(end, '%Y-%m-%d')

        results = session.query(Measurement.date,func.min(Measurement.tobs).label("Min Temp")
         ,func.avg(Measurement.tobs).label("Avg Temp")
         ,func.max(Measurement.tobs).label("Max Temp")).group_by(Measurement.date).filter(Measurement.date >= startDate,Measurement.date <= endDate ).all()
                        
        session.close()
        return jsonify(results)


    


if __name__ == '__main__':
    app.run(debug=True)
