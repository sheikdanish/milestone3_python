# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:18:54 2020

@author: sheikd
"""
# import web browser capabilities
import webbrowser
# import library for working on large, multi-dimensional arrays and matrices.
import numpy as np
# PLEASE RUN THIS COMMAND IN CONSOLE IF GMPLOT NOT INSTALLED:
# pip install gmplot
# import gmplot package
import gmplot
# import library for data manipulation and analysis.

def feature1(data, path_lats, path_long):
    """Feature 1: Plot Path and Trip Details"""
    # Declare the center of the map, and how much we want the map zoomed in.
    gmap3 = gmplot.GoogleMapPlotter(data[' Latitude'].mean(),
                                    data[' Longitude'].mean(), 14)

    # Start and stop plot on map.
    gmap3.scatter(list([path_lats[0]]), list([path_long[0]]),
                  '#00FF00', size=50, marker=False)
    gmap3.scatter(list([path_lats[-1]]), list([path_long[-1]]),
                  '#FF0000', size=50, marker=False)
# Plot method Draw a line in between given coordinates.
    gmap3.plot(path_lats, path_long, 'blue', edge_width=3.0)

    # Google_API_Key.
    # gmap3.apikey = "AIzaSyAXPL2nQcPiXhSkhHTwoSFXm6Vn6hyeB3Y"
    # Save to html.
    gmap3.draw(r"Path.html")
    webbrowser.open('Path.html', new=2)
    started = np.array(data['GPS Time'])
    print('Trip Start:', started[0])
    ended = np.array(data['GPS Time'])
    print('\nTrip End:', ended[-1])
    tim = np.array(data['Trip time(whilst moving)(s)'])
    print('\nTime Taken for trip:', tim[-1], 'seconds')
    dist = np.array(data['Trip Distance(km)'])
    print('\nDistance Taken on trip:', dist[-1], 'kms')
    mileage = np.array(data['Kilometers Per Litre(Instant)(kpl)'].mean())
    print('\nMileage on trip:', mileage, 'kmpl')
    speed = np.array(data['Speed (GPS)(km/h)'].mean())
    print('\nAverage speed on trip:', speed, 'kmph')
    fuel_start = np.array(
        data['Fuel Remaining (Calculated from vehicle profile)(%)'])
    print('\nFuel at start of trip:', fuel_start[0], '%')
    print('\nFuel at end of trip:', fuel_start[-1], '%')
    gforce = np.array(data['Acceleration Sensor(Total)(g)'].mean())
    print('\nAverage G Force experienced on trip:', gforce, 'G')
    emiss = (data.iloc[:, 27].mean())
    print('\nCO emission on trip:', emiss, 'g/km')
