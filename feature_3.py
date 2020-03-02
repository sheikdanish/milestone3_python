# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:26:34 2020

@author: sheikd
"""
# import web browser capabilities
import webbrowser
# import library for working on large, multi-dimensional arrays and matrices.
import numpy as np
# import library for plotting.
import matplotlib.pyplot as plt
# PLEASE RUN THIS COMMAND IN CONSOLE IF GMPLOT NOT INSTALLED:
# pip install gmplot
# import gmplot package
import gmplot

def feature3(data, path_lats, path_long):
    """Feature 3: Detect and Plot Bad Road Condition"""
    # Plot Acceleration values in Z axis.
    plt.plot(data['Acceleration Sensor(Z axis)(g)'], '.')
    plt.title('Acceleration(Z)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('G value', fontdict=None, labelpad=None)
    plt.show()
    # Extract data of accelerations in Z axis exceeding 1.1
    # or below 0.7 magnitudes.
    bad_roadsu = data[data['Acceleration Sensor(Z axis)(g)'] < 0.7]
    print(bad_roadsu)
    bad_roadsl = data[data['Acceleration Sensor(Z axis)(g)'] > 1.1]
    print(bad_roadsl)
    # Extract different latitude and longitude points.
    badroad_latsu = np.array(bad_roadsu[' Latitude'])
    badroad_latsl = np.array(bad_roadsl[' Latitude'])
    badroad_longu = np.array(bad_roadsu[' Longitude'])
    badroad_longl = np.array(bad_roadsl[' Longitude'])
    # Declare the center of the map, and how much we want the map zoomed in.
    gmap3 = gmplot.GoogleMapPlotter(data[' Latitude'].mean(),
                                    data[' Longitude'].mean(), 14)
    # Start and stop plot on map.
    gmap3.scatter(list([path_lats[0]]), list([path_long[0]]),
                  '#00FF00', size=15, marker=False)
    gmap3.scatter(list([path_lats[-1]]), list([path_long[-1]]),
                  '#FF0000', size=15, marker=False)
    # Plot method Draw a line in between given coordinates.
    gmap3.plot(path_lats, path_long, 'blue', edge_width=3.0)
    # Plot Bad Road Condition Points.
    gmap3.scatter(list(badroad_latsu)+list(badroad_latsl),
                  list(badroad_longu)+list(badroad_longl), '#9000FF',
                  size=50, marker=False)
    # Google_API_Key.
    # GMAP3.apikey = "AIzaSyAXPL2nQcPiXhSkhHTwoSFXm6Vn6hyeB3Y"
    # Save to html.
    gmap3.draw(r"Badroads.html")
    webbrowser.open('Badroads.html', new=2)
