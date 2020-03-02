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

def feature2(data, path_lats, path_long):
    """Feature 2: Detect and Plot harsh Accelerations"""
    # Plot Acceleration values in Y axis.
    plt.plot(data['Acceleration Sensor(Y axis)(g)'], '.')
    plt.title('Acceleration(Y)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('G value', fontdict=None, labelpad=None)
    plt.show()
    # Extract data of accelerations in Y axis exceeding threshold of 0.4 magnitude.
    harsh_drive = data[data['Acceleration Sensor(Y axis)(g)'] < -0.4]
    print(harsh_drive)
    # Extract different latitude and longitude points.
    harshpath_lats = np.array(harsh_drive[' Latitude'])
    harshpath_long = np.array(harsh_drive[' Longitude'])
    # Declare the center of the map, and how much we want the map zoomed in.
    gmap3 = gmplot.GoogleMapPlotter(data[' Latitude'].mean(),
                                    data[' Longitude'].mean(), 14)
    # Start and stop plot on map.
    gmap3.scatter(list([path_lats[0]]), list([path_long[0]]), '#00FF00',
                  size=15, marker=False)
    gmap3.scatter(list([path_lats[-1]]), list([path_long[-1]]), '#FF0000',
                  size=15, marker=False)
    # Plot method Draw a line in between given coordinates.
    gmap3.plot(path_lats, path_long, 'blue', edge_width=3.0)
    # Plot harsh Acceleration Points.
    gmap3.scatter(list(harshpath_lats), list(harshpath_long), '#FFFF00',
                  size=50, marker=False)
    # Google_API_Key.
    # GMAP3.apikey = "AIzaSyAXPL2nQcPiXhSkhHTwoSFXm6Vn6hyeB3Y"
    # Save to html.
    gmap3.draw(r"Harsh.html")
    webbrowser.open('Harsh.html', new=2)
