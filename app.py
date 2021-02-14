#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Create a base class
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)
# Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to our database
session = Session(engine)

# Create a Flask application called "app."
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Add the routing information for each of the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

if __name__ == "__name__":
    app.run(host="0.0.0.0", debug=True, port=5000)



