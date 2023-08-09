from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt

app = Flask(__name__)

# Set up database connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement
session = Session(engine)

# Landing page with available routes
@app.route("/")
def home():
    return (
        "Welcome to the Climate App API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/&lt;start&gt;<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).all()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    station_list = [station[0] for station in results]
    return jsonify(station_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)) \
        .group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = (dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    results = session.query(Measurement.date, Measurement.tobs) \
        .filter(Measurement.station == most_active_station) \
        .filter(Measurement.date >= one_year_ago).all()
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in results]
    return jsonify(tobs_list)

# Temperature range route for start date
@app.route("/api/v1.0/<start>")
def temperature_range_start(start):
    temperature_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
        .filter(Measurement.date >= start).all()
    temp_stats_dict = {
        "Min Temperature": temperature_stats[0][0],
        "Average Temperature": temperature_stats[0][1],
        "Max Temperature": temperature_stats[0][2]
    }
    return jsonify(temp_stats_dict)

# Temperature range route for start and end dates
@app.route("/api/v1.0/<start>/<end>")
def temperature_range_start_end(start, end):
    temperature_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
        .filter(Measurement.date >= start) \
        .filter(Measurement.date <= end).all()
    temp_stats_dict = {
        "Min Temperature": temperature_stats[0][0],
        "Average Temperature": temperature_stats[0][1],
        "Max Temperature": temperature_stats[0][2]
    }
    return jsonify(temp_stats_dict)

if __name__ == '__main__':
    app.run(debug=True)
