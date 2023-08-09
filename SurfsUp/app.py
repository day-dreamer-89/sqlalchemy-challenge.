from flask import Flask, jsonify

app = Flask(__name__)

# Define the homepage and list of available routes
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

# Define the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Your code to calculate and return the precipitation data as JSON
    
# Define the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
    # Your code to retrieve and return the list of stations as JSON
    
# Define the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Your code to calculate and return the temperature observations for the most-active station as JSON
    
# Define the /api/v1.0/<start> route
@app.route("/api/v1.0/<start>")
def temperature_range_start(start):
    # Your code to calculate and return temperature statistics for a specified start date as JSON
    
# Define the /api/v1.0/<start>/<end> route
@app.route("/api/v1.0/<start>/<end>")
def temperature_range_start_end(start, end):
    # Your code to calculate and return temperature statistics for a specified start-end range as JSON
    
if __name__ == '__main__':
    app.run(debug=True)
