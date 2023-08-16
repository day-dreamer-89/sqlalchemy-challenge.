# sqlalchemy-challenge.
SQLAlchemy Climate Analysis and Flask API

Project Structure
SurfsUp/
climate_starter.ipynb: Jupyter Notebook containing climate analysis and data exploration.
hawaii.sqlite: SQLite database containing climate data.
app.py: Flask API script for serving climate data.
Part 1: Analyze and Explore Climate Data
In the climate_starter.ipynb notebook, we use Python, SQLAlchemy, Pandas, and Matplotlib to perform a basic climate analysis and data exploration of the climate database.

Precipitation Analysis
Find the most recent date in the dataset.
Retrieve the previous 12 months of precipitation data.
Plot the precipitation data using Matplotlib.
Print summary statistics for the precipitation data.
Station Analysis
Calculate the total number of stations.
Find the most active station (highest observation count).
Calculate lowest, highest, and average temperatures for the most active station.
Retrieve the previous 12 months of temperature observation (TOBS) data.
Plot a histogram of TOBS data.
Part 2: Design Your Climate App
In the app.py script, we design a Flask API based on the analysis and queries developed in Part 1.

Available Routes
/: Homepage with a list of available routes.
/api/v1.0/precipitation: Retrieve and return precipitation data in JSON format.
/api/v1.0/stations: Retrieve and return station data in JSON format.
/api/v1.0/tobs: Retrieve and return temperature observation data for the most active station in JSON format.
/api/v1.0/<start>: Retrieve and return temperature data (TMIN, TAVG, TMAX) for a specified start date in JSON format.
/api/v1.0/<start>/<end>: Retrieve and return temperature data (TMIN, TAVG, TMAX) for a specified date range in JSON format.
Usage
Clone this repository to your local machine.
Open and run the climate_starter.ipynb notebook for data analysis.
Run the Flask API using python SurfsUp/app.py.
Access the different routes to retrieve climate data.